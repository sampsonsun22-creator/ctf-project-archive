# 星巴克 EP 1.0 · 需求变更评估报告
## 新店状态与预测逻辑增强：新增「SSP Submitted」状态（CR-2026-0618）

| 项 | 内容 |
|---|---|
| 客户 / 项目 | 星巴克中国 · EP 1.0（企业经营计划智能预测，基于 Planiverse，已交付达标 MLC 93%/店 86%，7500+ 店）|
| 需求来源 | Jack Peng Ou（星巴克 Finance Tech Manager）邮件「EP需求变更评估【紧急】」2026-06-18 16:41 |
| 抄送/干系 | 程明/姚佳旭（杉数）；王子卓(CTO)/赵峰/孟飞/Ivy Zhou/Gavin Li 等 |
| 需求编号 | CR-2026-0618 |
| 目标窗口 | 用于 **FY27 FP**；期望 **2026-07-10 前上线**；**6.22 前**给可行性确认 + 报价 |
| 报告性质 | 杉数内部**可行性 + 改造点 + 风险 + 报价框架**评估（v0，含待澄清项）|
| 编制 | 杉数 EP 项目组 · 2026-07-02 · v0（待需求澄清会后转 v1）|

> 依据：金库沉淀的 EP 1.0 真源（新店逻辑/系统状态枚举/字段规则/操作/验收口径），方法遵 M-004 方案设计 / M-007 数据可行性 / M-009 范围管理。**含"待核/假设"显式标注，零编造；具体人天/金额待内部资源评估。**

---

## 0. 执行摘要（先读）

- **结论：可行，属"低–中复杂度"增量改造，7.10 上线窗口可达**（前提是 6.22 前澄清 3–4 个开口项）。
- **核心判断**：SSP Submitted = **ADT 走「No SSP」路径（机器学习不依赖 SSP ADT）+ Store Days 走「SSP Approved」路径（从 Plan_open_date 起算）的正交组合**。**两条子逻辑均已在 EP 1.0 上线**，本 CR 无需新建算法模型，本质是"**新增一个门店状态枚举 + 把它正确路由到两条已有分支**"。
- **主要工作**：数据/枚举层（Status 加值 + 上传校验）＋ 算法层（Status→分支路由新增一个 case，复用已有 ADT/StoreDays 分支）＋ 系统层（下拉/校验/展示/发布联动回归）＋ 全回归测试。
- **量级锚定**（参照 08 商务 CR 台账）：远小于 Core/LTO CR（¥83.6万/53+96+54 人天，涉及 subcat 下探重构），量级更接近或小于 Anaplan 对接 CR（¥8.7万/约 28 人天）。**建议报价按"算法分支 + 系统枚举/校验 + 测试上线"分层估，具体人天待内部确认。**
- **最大风险**：不是技术难度，而是 ①需求细节未澄清即开发的**返工风险**（Weekly Open Days 是否必填 / 状态流转规则 / Qty 逻辑）；②与并行 CR（Anaplan 对接替换 EP Adjust、Core/LTO）**共享 Storelist/算法代码的发布协调**；③7.10 硬窗口 + 6.22 报价的**时间挤压**。

---

## 1. 需求背景与目标

- **业务背景**：新店计划管理复杂度进一步加强。EP 1.0 现有新店状态为 3 种（No SSP / SSP Approved / Opened），无法刻画"**已提交选址提案（SSP submitted）但尚未审批通过**"这一中间态——这类门店已有明确 Plan Open Date，但 SD 尚未给出 SSP ADT 估值。
- **需求目标**：在 Storelist 新店状态中**新增第 4 种「SSP Submitted」**，并为其定义 ADT 与 Store Days 的预测逻辑，使 FY27 FP 能纳入这类门店做更精细的财务计划。
- **约束**：紧急；FY27 FP（P9 启动）为硬 deadline；7.10 前上线；6.22 前出可行性 + 报价。

---

## 2. 现状基线（As-Is）：EP 1.0 新店三状态逻辑

> 真源：金库 `03_算法方案与可解释性 §1`、`07_数据字典与假设`、`09_系统功能与架构 §2`。

**SSP 语义**：SSP = 新店选址/审批关口；**SSP's ADT** = SD 部门给出的新店首年 ADT 预估（来源 SD One / Storelist 的 `SSP's ADT` 字段）。新店按审批漏斗推进：**No SSP → SSP Approved → Opened**。

| 门店状态 | 人工录入 | ADT 预测逻辑 | Store Days 逻辑 |
|---|---|---|---|
| **Opened** | >3月无 SSP ADT；≤3月有 SSP ADT + Actual Open Date | 机器学习（≤3月依赖 SSP ADT）| 从录入的 **Actual_open_date** 起算 |
| **No SSP** | 无 SSP ADT，有 Plan Open Date | 机器学习（**不依赖** SSP ADT）| **基于规则，首月平均 11 天**（不依赖 Plan Open Date）|
| **SSP Approved** | 有 SSP ADT，有 Plan Open Date | 机器学习（**依赖** SSP ADT）| 从录入的 **Plan_open_date** 起算 |

**相关系统/字段现状**（07/09）：
- Storelist `Status` 枚举 = {No SSP, SSP Approved, Opened}；字段条件必填：`SSP's ADT`（SSP Approved 必填 / Opened <3月必填）、`Plan Open Date`（No SSP / SSP Approved 必填）、`Weekly Open Days`（SSP Approved 必填 5~7 / No SSP 非必填 / Opened <1月必填）、`Actual Open Date`（Opened 必填）。
- 新店经 **New Storelist-SD** 上传（整表替换、仅 CY 店）；无 Global ID 自动生成 **Dummy ID**（不可回收）；有 Global ID 则 hierarchy 自 DMP 带出。
- 算法按 Status 分流到不同预测路径（新店 ADT 已演进为机器学习）；Store Days 走 §2.3 的 Base − dayloss 逻辑；三服务器（209/210/211）半自动跑。
- 版本发布联动、Scorecard、RMIP 拆分、推 BI（Dataphin）、BI Cube Store 维度均按现有 CY 新店处理。

---

## 3. 需求详细分析与拆解

### 3.1 需求本质（一句话）
**SSP Submitted 是两条已有逻辑分支的"正交拼装"**：

| 维度 | SSP Submitted 取值 | = 复用哪个已有状态的逻辑 |
|---|---|---|
| 人工录入 | 无 SSP ADT，有 Plan Open Date | = **No SSP** 的录入口径 |
| ADT 预测 | 机器学习（不依赖 SSP ADT）| = **No SSP** 的 ADT 路径 |
| Store Days | 从录入的 Plan_open_date 起算 | = **SSP Approved** 的 StoreDays 路径 |

> 即：**ADT 侧 = No SSP，StoreDays 侧 = SSP Approved**。这是本 CR 复杂度可控的根本原因——不引入任何新算法/新公式，只是把两条已上线分支按新状态重新组合。

### 3.2 业务价值
- 让"已交提案未获批"的门店（有计划开店日期、但无 SD 的 ADT 估值）能被更合理地纳入 FY27 FP：ADT 不硬凑一个不存在的 SSP ADT（走 No SSP 的 ML），Store Days 又能按真实计划开店日精确起算（而非 No SSP 的粗规则 11 天）——比"暂按 No SSP 处理"更贴近该类门店的真实营业节奏。

### 3.3 需求拆解（原子能力级）
| # | 层 | 需求 | 复用/新增 |
|---|---|---|---|
| R1 | 数据/枚举 | `Status` 枚举增加 `SSP Submitted`；必填规则=Plan Open Date 必填、SSP's ADT 为空 | 增量（枚举+校验）|
| R2 | 算法·ADT | SSP Submitted 的 ADT 走"No SSP 的 ML 不依赖 SSP ADT"路径 | **复用**已有分支 |
| R3 | 算法·StoreDays | SSP Submitted 的 StoreDays 走"SSP Approved 的从 Plan_open_date 起算"路径 | **复用**已有分支 |
| R4 | 算法·路由 | 按 `Status=SSP Submitted` 把门店路由到 R2+R3 的正确组合 | 新增一个 case 分支 |
| R5 | 系统/上传 | 上传模板/页面下拉/校验更新；Dummy ID/Global ID/hierarchy 与其他 CY 新店一致 | 增量 |
| R6 | 下游一致性 | 版本发布联动、Scorecard、RMIP、推 BI、BI Cube 维度对新状态透明兼容 | 回归/兼容 |

---

## 4. 需求设计方案

### 4.1 数据层设计（R1、R5）
- Storelist `Status` 下拉/枚举增加 `SSP Submitted`（4 值）。
- 字段条件必填规则新增一行：**SSP Submitted → Plan Open Date 必填、SSP's ADT 应为空（不录/置空）**；`Weekly Open Days` 是否必填**【待核 Q1】**——因 Store Days 从 Plan_open_date 起算需要"每周营业天数"规则（SSP Approved 侧必填 5~7；No SSP 侧非必填）。倾向：**SSP Submitted 需按 SSP Approved 口径要求 Weekly Open Days**（否则从 Plan open date 起算缺营业日历）。
- 数据字典/枚举表、上传模板说明、（若仍走 MDS 通道）storelist-cy schema 同步。

### 4.2 算法层设计（R2/R3/R4）
- 在算法"按 Status 分流"的逻辑中**新增 SSP Submitted 分支**：
  - `ADT`：调用现有 **No-SSP ADT 预测路径**（ML，不依赖 SSP ADT）。
  - `StoreDays`：调用现有 **SSP-Approved StoreDays 路径**（从 Plan_open_date 起算，而非 No SSP 的规则 11 天）。
- **无新模型、无新特征**；三服务器（209/210/211）代码同步更新并发布；跑一版回归确认既有 3 状态结果不变、新状态输出符合预期。
- Qty/RSP/Discount：新店的 Qty 现按同城同商圈邻店 UPT×预测 txn 估、Discount 取邻店均值——**SSP Submitted 是否沿用 No SSP 的 Qty/RSP/Discount 逻辑【待核 Q2】**（邮件仅给了 ADT+StoreDays 两列）。倾向沿用 No SSP。

### 4.3 系统层设计（R5/R6）
- 前端：New Storelist-SD 页 `Status` 下拉增值、条件必填校验、列表/详情展示。
- Dummy ID / Global ID / hierarchy：SSP Submitted 属 CY 未开新店，**与现有 CY-No SSP/SSP Approved 同处理**（无 Global ID → 生成 Dummy ID；有则带 DMP）。
- 版本发布联动、Dayloss for Forecast/Scorecard、RMIP 拆分、推 BI（bi_dw_fcst_txn_storedays 等）、BI Cube Store/Age Class 维度：**新状态归 CY 新店，复用现有链路**，需回归验证不破坏联动。

### 4.4 状态流转设计（R1，隐含需求）
- SSP Submitted 会随审批推进流转：**SSP Submitted → SSP Approved**（拿到 SSP ADT）/ **→ Opened**（实际开业）。流转时 ADT/StoreDays 逻辑切换、Dummy→Global ID 绑定、跨预测版本一致性、dayloss 沿用规则**【待核 Q3】**。建议在设计阶段明确迁移规则并纳入测试用例。

---

## 5. EP 1.0 改造点清单（分层）

| 层 | 改造点 | 说明 | 复杂度 |
|---|---|---|---|
| **数据/Storelist** | ① Status 枚举增 `SSP Submitted` | 枚举 + 前端下拉 | 低 |
| | ② 上传模板 + 页面校验（Plan Open Date 必填、SSP's ADT 空、Weekly Open Days 规则）| 条件必填联动 | 低–中 |
| | ③（若走 MDS 通道）storelist-cy 校验 | 数字化前的历史通道 | 低 |
| | ④ 数据字典/枚举表/模板说明更新 | 文档 | 低 |
| **算法(forecast.ai)** | ⑤ Status→分支路由增 SSP Submitted case | 组合已有两分支 | 中 |
| | ⑥ ADT 复用 No SSP 路径、StoreDays 复用 SSP Approved 路径 | **无新模型** | 低 |
| | ⑦ 209/210/211 三服务器代码同步 + 发布 + config | 半自动运维 | 中 |
| | ⑧ 回归（3 状态不变）+ 新状态正测 | 算法回测 | 中 |
| **系统(planiverse)** | ⑨ 前端 Status 展示/校验/下拉 | UI | 低 |
| | ⑩ Dummy ID/Global ID/hierarchy 对新状态（应与 CY 新店一致，需验证）| 兼容 | 低 |
| | ⑪ 版本发布状态联动 + Scorecard/Dayloss for Forecast 对新状态 storeday 计算 | 回归 | 中 |
| **下游** | ⑫ 推 BI/Dataphin（表结构不变，storeday 值变）| 兼容 | 低 |
| | ⑬ BI Cube Store/Age Class 维度、RMIP 拆分对新状态门店 | 归 CY 复用 | 低–中 |
| | ⑭ SCO/ARP 等下游（quantity 透明）| 透明 | 低 |
| **测试/文档** | ⑮ 端到端（上传→算法→scorecard→推 BI）+ 状态流转用例 | SIT/UAT | 中 |
| | ⑯ 蓝图/算法方案/数据字典/用户手册/操作手册(金库12) 更新 | 交付文档 | 低 |

---

## 6. 风险评估（Risk × 等级 × 缓解）

| # | 风险 | 等级 | 说明 | 缓解 |
|---|---|---|---|---|
| Risk-1 | **需求细节未澄清即开发** | 🔴 高 | Weekly Open Days 是否必填、状态流转、Qty 逻辑、验收口径未定，直接开发易返工 | **6.22 前召开需求澄清会**敲定 Q1–Q4，再排期 |
| Risk-2 | **StoreDays×ADT 组合此前不存在** | 🟡 中 | "无 SSP ADT 的 ML + 从 Plan_open_date 起算 StoreDays"是新组合，需验证 storeday×ADT×qty 联动无异常（尤其新店 ramp-up）| 专项回归 + 抽样门店人工核对（参照门店 78825 数据质量教训）|
| Risk-3 | **数据质量（Plan Open Date / Weekly Open Days）** | 🟡 中 | Store Days 从 Plan_open_date 起算，输入不准则 storeday 失真 | 明确 SD 录入规范；上传强校验；数据质量决定准确率 |
| Risk-4 | **状态流转一致性** | 🟡 中 | SSP Submitted→SSP Approved/Opened 迁移时逻辑切换、Dummy→Global、跨版本/actualize 一致性 | 设计阶段定迁移规则 + 覆盖测试用例 |
| Risk-5 | **与并行 CR 的发布冲突** | 🟡 中 | Anaplan 对接（将替换 EP Adjust）、Core/LTO CR 共享 Storelist/算法代码 | 与两 CR 协调发布窗口与代码分支；确认 SSP Submitted 是否走 Anaplan 后新流程【Q5】 |
| Risk-6 | **系统枚举变更的连带回归面** | 🟡 中 | Status 变更牵动上传校验/版本发布联动/Scorecard/RMIP/BI Cube | 全回归；三服务器代码同步；发版走 Golive checklist |
| Risk-7 | **时间挤压** | 🟡 中 | 6.22 报价 → 7.10 上线约 2–3 周（含开发+SIT+UAT+发版），且 FY27 FP 硬 deadline | 澄清前置 + 范围锁定不外溢 + 复用为主；必要时分阶段（先枚举+算法，后可视化增强）|
| Risk-8 | **范围外溢** | 🟢 低–中 | 邮件仅给 ADT/StoreDays 两列，Qty/RSP/Discount/验收未提，易被追加 | M-009 范围管理：以本邮件两列为基线，其余走变更单 |

---

## 7. 可行性结论 · 工作量与报价框架 · 实施建议

### 7.1 可行性结论
**可行，低–中复杂度增量改造**。核心是"新增状态枚举 + 路由到两条已上线子逻辑的正交组合"，非架构级变更、无新算法模型。7.10 上线窗口**可达**，成败取决于 6.22 前的需求澄清与范围锁定。

### 7.2 工作量与报价框架（量级锚定，具体待内部估）
> 依据 08 商务 CR 台账的**人天单价**（含 6% 税）：解决方案架构师 ¥4,748.8 / 算法架构师 ¥5,088 / 算法工程师 ¥3,731.2 / 开发·测试工程师 ¥2,544。

| 阶段 | 主要工作 | 角色 | 人天（待内部估）|
|---|---|---|---|
| 方案设计 | 需求澄清 + 分支/枚举设计 + 测试方案 | 解决方案架构师 + 算法架构师 | 待估 |
| 开发 | 算法路由分支 + 系统枚举/校验/展示 | 算法工程师 + 开发工程师 | 待估 |
| 测试上线 | 回归 + 新状态正测 + SIT/UAT + 发版 | 开发/测试工程师 | 待估 |

- **量级判断**：本 CR 远小于 Core/LTO CR（¥83.6万，subcat 下探重构、53+96+54=203 人天），**量级更接近或小于 Anaplan 对接 CR（¥8.7万，约 28 人天）**——因为是"组合已有逻辑"而非新建。**建议报价按上述三阶段分层，人天在内部资源评估后填入。**（本报告不编造具体金额。）

### 7.3 实施建议
1. **6.22 前召开需求澄清会**，敲定 Q1–Q4（见 §8），把两个开口列（Weekly Open Days、Qty 逻辑）与状态流转、验收口径定死，再报价排期。
2. **以"复用已有分支"为设计铁律**，控制范围不外溢（M-009）；邮件两列（ADT/StoreDays）为基线，其余走变更单。
3. **与 Anaplan / Core&LTO CR 协调**发布窗口与算法/Storelist 代码分支，避免相互覆盖。
4. **回归为主**保障既有 3 状态与 MLC 93%/店 86% 不劣化；新状态**参照 Core/LTO 口径不单独考核准确率**（建议，待客户确认）。
5. **分层报价**（算法分支 / 系统枚举校验 / 测试上线），并在 SOW 明确验收标准（回归通过 + 新状态逻辑走查确认）。
6. 若 7.10 极紧，可**分阶段**：先上线"枚举+算法分支+校验"（满足 FY27 FP 用），可视化/边界增强随后跟进。

---

## 8. 待澄清开口项（6.22 需求澄清会议题，零编造前提）

| # | 待核问题 | 影响 |
|---|---|---|
| Q1 | SSP Submitted 的 **Weekly Open Days 是否必填**？ | Store Days 从 Plan_open_date 起算需营业日历；影响 storeday 计算与校验规则 |
| Q2 | SSP Submitted 的 **Qty/RSP/Discount** 是否沿用 No SSP（邻店 UPT/city average）逻辑？ | 邮件未提；影响算法分支范围 |
| Q3 | **状态流转规则**（SSP Submitted→SSP Approved→Opened）在跨预测版本/actualize 时如何处理？ | 影响迁移设计与测试 |
| Q4 | **验收口径**：是否单独考核该状态准确率？（建议参照 Core/LTO 不单独考核、方案后≥方案前）| 影响 SOW 验收标准 |
| Q5 | 是否走 **Anaplan 对接后新流程**（EP Adjust 被替换），与本 CR 发布窗口是否冲突？ | 影响发布协调与设计 |
| Q6 | **报价的具体人天/金额** 需内部资源评估确认 | 本报告给框架，数字待内部估 |

**关键假设（待澄清会确认）**：①复用现有 No SSP(ADT) + SSP Approved(StoreDays) 子逻辑，无新模型；②新状态归 CY 新店，Dummy ID/Global ID/RMIP/BI 处理与现有 CY 一致；③Weekly Open Days 按 SSP Approved 口径要求填写；④Qty/RSP/Discount 沿用 No SSP。

---

## 附录 · 真源引用（金库 EP 1.0 知识库，只读）
- CR 记录：`04_实例库/项目/星巴克EP/11_需求变更与CR动态.md`（CR-2026-0618）
- 新店 ADT/StoreDays 4 状态逻辑：`03_算法方案与可解释性.md §1`
- Storelist 状态枚举/上传校验/Dummy·Global ID/版本发布：`09_系统功能与架构.md §2`
- 字段条件必填/枚举/数据规模：`07_数据字典与假设.md`
- 操作步骤（上传/校验/发起算法）：`12_EP系统操作手册骨架.md`
- 商务/CR 台账/人天单价/验收口径：`08_商务合同与交付里程碑.md`
- 方法：M-004 方案设计法 / M-007 数据可行性评估法 / M-009 SOW与范围管理法（金库 01_元能力库，引 ID）

---

*需求分析评估报告 · v0 · 2026-07-02 · 杉数 EP 项目组内部评估（含待澄清项）。可行性=低–中复杂度增量改造（复用两条已有分支），7.10 可达；核心风险=需求未澄清即开发的返工 + 并行 CR 发布协调 + 时间挤压。人天/金额待内部资源评估。对客/对上版请据此去内部脚手架（待核/假设/atom 引用）后另出。*
