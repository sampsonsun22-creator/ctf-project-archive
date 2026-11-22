# 恢复项目文件

[首轮快照](https://github.com/sampsonsun22-creator/ctf-project-archive/releases/tag/archive-2026-11-22)是 2026-11-22 的六个 ZIP，含 1,044 个文件。每个压缩包保留原始路径，Release 及 `sync/original-versions.json` 记录 SHA-256。

后续增量以 `sync/original-versions.json` 的 `updates` 为准。按时间顺序应用到首轮解压目录。对单文件版本，读取 `parts` 列表中的 Git 路径并按顺序拼接其原始字节，校验 `sha256` 和 `bytes`，然后放到 `path` 对应的项目目录。旧版本和已从源目录移除的文件继续保留在备份历史里。

`sync/knowledge-versions.json` 记录可直接阅读的 Markdown 的来源和版本。[START_HERE.md](START_HERE.md) 提供阅读入口。
