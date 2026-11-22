#!/usr/bin/env python3
"""Summarize the archive manifests already committed to this repository."""

import argparse
from collections import Counter
from datetime import date, datetime
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from zoneinfo import ZoneInfo


BEIJING = ZoneInfo("Asia/Shanghai")
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
GIT_BLOB = re.compile(r"[0-9a-f]{40}\Z")


def read_object(path):
    with path.open(encoding="utf-8") as source:
        value = json.load(source)
    if not isinstance(value, dict):
        raise ValueError(f"{path.name} must be a JSON object")
    return value


def array(document, key):
    value = document.get(key)
    if not isinstance(value, list):
        raise ValueError(f"{key} must be an array")
    return value


def string(row, key):
    value = row.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key} must be a nonempty string")
    return value


def file_path(value, *, absolute):
    if not isinstance(value, str) or value.startswith("/") != absolute:
        raise ValueError("Invalid manifest file path")
    relative = value[1:] if absolute else value
    if any(part in ("", ".", "..") for part in relative.split("/")):
        raise ValueError("Invalid manifest file path")
    return value


def byte_count(row):
    size = row.get("bytes")
    if type(size) is not int or size < 0:
        raise ValueError("bytes must be a nonnegative integer")
    return size


def fingerprint(*values):
    payload = json.dumps(values, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def project_for(path, roots):
    folder, separator, _ = path[1:].partition("/")
    root = "/" + folder
    return root if separator and root in roots else None


def collect(original, knowledge):
    if original.get("schema") != 1:
        raise ValueError("Unsupported original manifest schema")
    roots = array(original, "sourceRoots")
    if not roots or any(file_path(root, absolute=True).count("/") != 1 for root in roots):
        raise ValueError("sourceRoots must be top-level project folders")
    if len(roots) != len(set(roots)):
        raise ValueError("sourceRoots must be unique")

    baseline = Counter()
    latest = {}
    originals = {}
    historical_versions = set()
    additions = array(original, "updates")
    for entries, is_update in ((array(original, "files"), False), (additions, True)):
        for row in entries:
            if not isinstance(row, dict):
                raise ValueError("Archive entries must be objects")
            source = string(row, "id")
            path = file_path(string(row, "path"), absolute=True)
            project = project_for(path, roots)
            if project is None:
                raise ValueError("Archive file is outside the declared project roots")
            version = string(row, "version")
            size = byte_count(row)
            identity = fingerprint(source)
            if is_update:
                checksum = string(row, "sha256")
                parts = array(row, "parts")
                if not SHA256.fullmatch(checksum) or not parts:
                    raise ValueError("Invalid incremental archive checksum or parts")
                for part in parts:
                    file_path(part, absolute=False)
            else:
                if identity in latest:
                    raise ValueError("Duplicate original manifest identity")
                checksum = string(row, "asset")
                baseline[project] += 1
            latest[identity] = project
            originals[identity] = fingerprint(path, version, size, checksum)
            historical_versions.add(fingerprint(identity, path, version))

    knowledge_counts = Counter()
    knowledge_versions = {}
    for row in array(knowledge, "files"):
        if not isinstance(row, dict):
            raise ValueError("Knowledge entries must be objects")
        identity = fingerprint(string(row, "libraryFileId"))
        path = file_path(string(row, "sourcePath"), absolute=True)
        git_path = file_path(string(row, "gitPath"), absolute=False)
        git_blob = string(row, "gitBlob")
        if identity in knowledge_versions or not GIT_BLOB.fullmatch(git_blob):
            raise ValueError("Duplicate knowledge identity or invalid Git blob")
        knowledge_versions[identity] = fingerprint(path, git_path, git_blob, string(row, "version"), byte_count(row))
        knowledge_counts[project_for(path, roots)] += 1

    pending = original.get("inProgress", [])
    if not isinstance(pending, (list, dict)):
        raise ValueError("inProgress must be an array or object")
    pending_count = 1 if isinstance(pending, dict) and {"id", "path", "version"} <= pending.keys() else len(pending)
    snapshot = {"originals": originals, "versions": sorted(historical_versions), "knowledge": knowledge_versions}
    return roots, baseline, Counter(latest.values()), knowledge_counts, len(additions), pending_count, snapshot


def validate_snapshot(snapshot):
    if not isinstance(snapshot, dict):
        raise ValueError("Invalid checkpoint snapshot")
    for key in ("originals", "knowledge"):
        entries = snapshot.get(key)
        if not isinstance(entries, dict) or any(
            not isinstance(value, str) or not SHA256.fullmatch(fingerprint_id) or not SHA256.fullmatch(value)
            for fingerprint_id, value in entries.items()
        ):
            raise ValueError("Invalid checkpoint identity or fingerprint")
    if any(not isinstance(value, str) or not SHA256.fullmatch(value) for value in array(snapshot, "versions")):
        raise ValueError("Invalid checkpoint version fingerprint")


def checkpoint_date(value):
    if not isinstance(value, str):
        raise ValueError("Invalid checkpoint date")
    parsed = date.fromisoformat(value)
    if parsed.isoformat() != value:
        raise ValueError("Invalid checkpoint date")
    return parsed


def comparison(state_path, today, current):
    if not state_path.exists():
        return None, current
    state = read_object(state_path)
    if state.get("schema") != 1:
        raise ValueError("Unsupported daily checkpoint schema")
    existing_date = checkpoint_date(state.get("date"))
    if existing_date > today:
        raise ValueError("Daily checkpoint is newer than the current Beijing date")
    if existing_date < today:
        snapshot = state.get("snapshot")
        validate_snapshot(snapshot)
        return existing_date.isoformat(), snapshot
    previous_day = state.get("comparisonDate")
    if previous_day is not None and checkpoint_date(previous_day) >= today:
        raise ValueError("Comparison checkpoint must predate the current Beijing date")
    snapshot = state.get("comparisonSnapshot")
    validate_snapshot(snapshot)
    return previous_day, snapshot


def delta(previous, current):
    return (len(current.keys() - previous.keys()),
            sum(previous[key] != current[key] for key in current.keys() & previous.keys()),
            len(previous.keys() - current.keys()))


def render(today, comparison_day, previous, current, roots, baseline, archived, knowledge, updates, pending):
    if comparison_day is None:
        comparison_label = "以首次运行记录为比较起点。"
    else:
        comparison_label = f"与北京时间 {comparison_day} 的检查点比较。"
    original_delta = delta(previous["originals"], current["originals"])
    knowledge_delta = delta(previous["knowledge"], current["knowledge"])
    new_versions = len(set(current["versions"]) - set(previous["versions"]))
    rows = [
        "# CTF 项目每日摘要",
        "",
        f"北京时间 {today.isoformat()}。{comparison_label}",
        "",
        "## 自比较起点以来的变动",
        "",
        "| 范围 | 新增记录 | 更新记录 | 清单中移除 |",
        "| --- | ---: | ---: | ---: |",
        f"| 原件 | {original_delta[0]} | {original_delta[1]} | {original_delta[2]} |",
        f"| 知识 | {knowledge_delta[0]} | {knowledge_delta[1]} | {knowledge_delta[2]} |",
        "",
        f"新增归档版本 **{new_versions}** 个。",
        "",
        "## 当前归档状态",
        "",
        "| 项目 | 初始原件数 | 原件记录数 | 知识记录数 |",
        "| --- | ---: | ---: | ---: |",
    ]
    for root in roots:
        label = root[1:].replace("|", "\\|").replace("\n", " ").replace("\r", " ")
        rows.append(f"| {label} | {baseline[root]} | {archived[root]} | {knowledge[root]} |")
    if knowledge[None]:
        rows.append(f"| 项目目录外的共享知识 | 0 | 0 | {knowledge[None]} |")
    rows.extend([
        f"| **合计** | **{sum(baseline.values())}** | **{sum(archived.values())}** | **{sum(knowledge.values())}** |",
        "",
        f"原件清单记录 **{updates}** 条已归档增量，**{pending}** 条归档进行中。",
        "",
        "数据来源为当前仓库的[原件版本清单](original-versions.json)和[知识版本清单](knowledge-versions.json)。",
        "查看[备份恢复说明](../BACKUP.md)或[知识库入口](../START_HERE.md)。",
    ])
    return "\n".join(rows) + "\n"


def write_if_changed(path, value):
    data = value.encode("utf-8")
    if path.exists() and path.read_bytes() == data:
        return
    handle = tempfile.NamedTemporaryFile(dir=path.parent, prefix=path.name + ".", delete=False)
    temp = Path(handle.name)
    try:
        with handle:
            handle.write(data)
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def generate(root, today):
    sync = root / "sync"
    summary = collect(read_object(sync / "original-versions.json"), read_object(sync / "knowledge-versions.json"))
    *counts, current = summary
    state_path = sync / "daily_digest_state.json"
    comparison_day, previous = comparison(state_path, today, current)
    markdown = render(today, comparison_day, previous, current, *counts)
    state = {"schema": 1, "date": today.isoformat(), "comparisonDate": comparison_day,
             "comparisonSnapshot": previous, "snapshot": current}
    state_json = json.dumps(state, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    write_if_changed(sync / "DAILY_DIGEST.md", markdown)
    write_if_changed(state_path, state_json)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="repository root")
    args = parser.parse_args()
    try:
        generate(args.root, datetime.now(BEIJING).date())
    except (OSError, ValueError) as error:
        print(f"Daily digest generation failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
