# Sampson Sun（孙洋）工作记忆导出 · 周大福 Financial Systems

- 导出时间：2026-11-10（Asia/Shanghai）；取代 2026-11-05 版
- 来源：Claude 记忆库（memory files），共 66 个文件：账号级 36 个 + 5 个项目文件夹 30 个
- 版本：完整版（未脱敏）
- 范围：只含"记忆文件"。各 claude.ai Project 里上传的知识文档、项目指令、聊天记录、Obsidian／Linear 里的原始资料都不在本导出内。

## 给读取本文件的模型：阅读规则

1. **主体**：文中"用户／user／Sampson／Samson／孙洋／Sun Yang"都是同一人——Sampson Sun，周大福（Chow Tai Fook, CTF）Finance System Manager，2026-09-14 入职，常驻上海，直属上级 Vivian。
2. **`[stated]`**：表示该条是用户本人陈述或要求记录的内容（含用户转述的会议、邮件信息），不是模型推断。原文里的"待核／待定／未决／草案／计划"都要保留原意，**计划不等于已完成**。
3. **`[[name]]`**：指向 frontmatter 里 `name` 相同的另一个文件（人物、项目或主题）。同名文件可能同时存在账号级版本和项目副本。
4. **账号级 vs 项目副本**：Part A 是账号级（全局）记忆，Part B 是各项目文件夹里的记忆。同一主题两边都有时，**以 `updated` 日期较新、内容更细的那份为准**；较旧那份保留作背景。比如 AI SF 以项目 01 副本（2026-11-04）为准，账号级 AI SF（2026-10-29）较旧。
5. **两个 Ivy**：Ivy Cheng（鄭凱因，Finance VP、AI SF 项目负责人、PT Sponsor）和 Ivy 黄凯仪（Financial Systems 团队同事）是两个人，不能合并。
6. **星巴克（SBUX）内容**只作参考，不是 CTF 的需求、决定或待办（见 SBUX for AI SF 项目的边界规则）。
7. **preferences 文件**是用户希望 AI 怎样工作的要求（审阅标准、翻译格式、Excel 样式、交叉复核规则等），可直接采纳为工作方式。
8. 项目文件夹名称是根据各文件内容和用户的 Project 列表对应出来的；"04 Project Connections" 没有独立的记忆文件夹，相关内容在账号级 `/areas/project-connections.md` 和项目 01 的副本里。
9. 已去掉记忆系统的技术元数据（版本号、字节数），保留每个文件的 frontmatter 和 `updated` 时间（UTC）。

## 导出时观察到的跨文件差异（只作提示，未经用户裁定）

- **PT UAT 上线标准里 Low 的上限**：项目 02 的 10/27 记录写"fewer than 3 open Low"；项目 05 的 v8.1 记录写用户 10/29 更正为"每模块 Low 最多 3 个"（原记为 2 个）；Go-Live deck v3 写 "max 3 Low per subject"。
- **Karen 的 FY28 Topline 评审**：账号级 planning-tool、karen 写 2027-01-11；项目 02 记录 10/26 更新为改到 2027-01-08。
- **PT 库存价格带**：账号级文件写"20 万"；项目 02 记录 10/27 Elsie 改为 100k。AI SF 的 SF001 里"10 万"只是示例，项目 01 明确与 Elsie 跟进表的"20 万以下"分开保留、不自动统一。
- **Monologue**：账号级 project-connections 写"中国四大区与 Monologue 分列"；项目 03／05 记录 10/1 起已并入东南西北四区。
- **DSC Release 1 计划**：账号级 dsc-o9（10/22）较旧；项目 03（10/29–10/30）为 11/06 前完成 UAT、11/13 前签收、11/18 Go/No-Go、11/27–30 切换上线，且 1.6 财务视角成品 OTB 滚动已按"在范围内"处理。
- **团队周会／1:1 时间**：账号级写团队周会 10/14、10/21 在周三上午、固定时间待核；项目 05 写通常周一 11:00–12:00、与 Vivian 的 1:1 为周二 9:30–10:00。
- **AI SF 上线时间**：孙永琨的准确率 KPI 底稿写"2027.03 上线"，kick-off 时间轴和意臣 WBS 都是 2027 年 8 月上线（项目 01 文件内已标待核）。
- **三供应商集成对接会**：各文件日期说法不一（10 月、11 月、12/7 或 12/14 当周）；项目 02 的 Go-Live deck v3 写 11 月底至 12 月初，具体日期待定；项目 01 的 11/6 周会记录写"仍按 12 月初"，意臣称数据需求约 11/20 明确后再约。

## 相对 2026-11-05 版的变化

- 新增 1 个文件：`/areas/finance-legal-forum.md`（11/6 财务法务季度 Forum）
- 更新 11 个文件：账号级 ai-sales-forecast、anita、karen；项目 01 的 ai-sales-forecast（准确率 KPI 维度讨论、意臣第 1 周调研总结、11/6 周会、门店类型 6 类）、project-connections、sbux-reference；项目 02 的 planning-tool（Workday 科目结构与模板维度）、planning-tool-uat-golive（11/5 场景讨论、v1.8 场景表）；项目 03 的 dsc-project（11/5 周例会、11/9 库存扣减与 back test）、elsie-follow-up；SBUX 项目的 starbucks-reference

## 目录

- Part A 账号级（全局）记忆
- Part B · 01 AI Sales Forecast（9 个文件）
- Part B · 02 Planning Tool（11 个文件）
- Part B · 03 DSC Project（5 个文件）
- Part B · 05 Catch up with VV（4 个文件）
- Part B · SBUX for AI SF（1 个文件）

---

## Part A 账号级（全局）记忆

### /profile.md

- 原始路径：`/profile.md`
- updated (UTC)：2026-10-22T21:49:26Z

````markdown
---
name: profile
description: Who the user is — works at Chow Tai Fook (周大福), reports to Vivian; key colleagues Ivy, Karen, Anita, Elsie
sources: [chat]
aliases: [me, user]
---

- [stated] works at Chow Tai Fook (周大福); direct boss is [[vivian]]
- [stated] key colleagues: [[ivy]] (VP, senior to Vivian), [[karen]] (CFO), [[anita]] (key user of AI SF), [[elsie]]
- [stated] name: Sampson Sun（孙洋，Sun Yang；会议转写里常被识别为 Samson）
- [stated] title: Finance System Manager（Financial Systems 团队）
- [stated] city: 上海
- [stated] timezone: Asia/Shanghai
- [stated] working_language: 日常用中文；给管理层的正式材料多用英文
````

### /areas/ctf-finance-systems-role.md

- 原始路径：`/areas/ctf-finance-systems-role.md`
- updated (UTC)：2026-10-27T09:42:46Z

````markdown
---
name: ctf-finance-systems-role
description: The user's job at Chow Tai Fook — scope and boundaries across the three finance-system projects, cadence with Vivian, team meeting, tools
sources: [cowork]
aliases: [Finance System Manager, 财务系统经理, 工作职责, 五个工作入口]
---

- [stated] 2026-09-14 加入周大福，任 Finance System Manager（Financial Systems 团队，上海），直属上级 [[vivian]]
- [stated] 定位：企业内部财务系统经理（不再是以往的售前顾问角色），连接财务需求、业务流程、数据口径、系统交付、供应商沟通与用户验收
- [stated] 三个交付项目：[[ai-sales-forecast]]、[[planning-tool]]、[[dsc-o9]]；另有两个管理视图 [[project-connections]] 和 Catch up with Vivian，合称五个工作入口，但不是五个独立系统；SOW 治理归在 AI SF 里
- [stated] AI SF：在项目架构里属"财务小组"，负责需求与预测口径确认、蓝图评审、UAT 及业务验收、准确率复盘，是 FP&A 与 ICC／供应商之间的财务桥梁；阶段成果由项目负责人 [[ivy]] 确认，用户不是最终批准人
- [stated] Planning Tool：支持 Phase 1 整合、需求澄清和 UAT，关注 Phase 2；2026-10-21 Vivian 表示会逐步把更多 PT 工作移交给用户，具体边界待对齐
- [stated] DSC：关注财务目标、库存／周转口径、财务 UAT 和系统间依赖；不是 DSC 总体 PM。Vivian 9/29 明确：不希望用户变成三系统数据集成负责人，也不接 ICC 原负责的 AI SF 会议纪要
- [stated] 优先级：9 月正式口径 AI SF 第一、PT 第二、DSC 持续参与；2026-10-13 Vivian 指示未来 4–6 周主要投入 Planning Tool（阶段性重心，不改正式优先级）
- [stated] 与 Vivian 每周一次 1:1（9/22、9/29、10/13 在周二，10/21 在周三）；10/21 她提议改双周，会议结束时决定仍保持每周
- [stated] 每周五给 Vivian 发进展与下一步邮件；每周做 Finance Systems 周报，见 [[finance-systems-weekly-report]]
- [stated] Finance Systems 团队周会：10/14、10/21 两次都在周三上午，Vivian 主持，Keith、Ivy（黄凯仪）、方萍、蔡鲲和用户依次汇报；日历邀请里出现过周一／周二 11:00，固定时间待核
- [stated] 知识与证据放在 Obsidian vault（经 GitHub 同步），行动与风险放在 Linear（团队 SAM，按工作流 issue 归并，不一事一 issue）；Notion 不是主工作台
- [stated] 一个业务对象只有一个主归属，跨项目页面只引用、分析影响，避免重复任务和互相覆盖的状态
- [stated] 此前同时用 ChatGPT 协作；2026-10-22 把 ChatGPT 侧积累的项目记忆导出并导入 Claude
- [stated] 当前要 Elsie 跟进的事项见 [[elsie-follow-up]]
- [stated] 用户维护自己的每日疑问清单（Sampson daily issue list）：五个工作入口里凡是不懂的问题都记录，格式仿照 Elsie 跟进清单，每天 17:30 更新
````

### /areas/ai-sales-forecast.md

- 原始路径：`/areas/ai-sales-forecast.md`
- updated (UTC)：2026-11-09T08:42:37Z

````markdown
---
name: ai-sales-forecast
description: AI Sales Forecast (AI SF) project — governance, SOW/contract status, scope, acceptance terms and key corrections, current Rolling Forecast findings
sources: [cowork]
aliases: [AI SF, AISF, AI Sales Forecast, 销售预测项目, 销售预测]
---

## 定位与治理
- [stated] 目标：做出可解释、可调整、可追溯的销售预测，承接财务调整和门店指标分配（RMIP），衔接 [[planning-tool]]、[[dsc-o9]]、数据湖与 Power BI
- [stated] 供应商意臣（Yichen）；系统建在 CTF 现有的 o9 平台上，环境由 CTF 提供；o9 合同另签
- [stated] 治理：ICC 与 Finance 双 PM 共同负责；[[ivy]] 是项目负责人（业务目标、范围、阶段成果确认、SOW sign-off）；Finance PM [[vivian]]；ICC PM [[li-xinhong]]；ICC 侧项目总监胡志军／任波；用户在"财务小组"
- [stated] 分工（Vivian 9/29 提出，无异议）：ICC 负责技术与数据交付、算法、系统集成、供应商管理、信息安全；Finance 负责需求管理、预测流程设计、业务数据核验、UAT 组织、收益评估；蓝图确认、里程碑签收、准确率 KPI、上线准备由双方共同承担
- [stated] [[anita]] 的 FP&A 团队是关键用户；高层为 [[karen]] 和 [[patrick]]；9 月曾有 Vivian、Karen、Patrick 的双周会，10/13 纪要记为已取消

## 合同与时间线
- [stated] 2026-10-08 版 SOW 是当前合同审阅基线：意臣已对 clean 版重新 sign off，Vivian 10/13 表示已确认；文件名含 sign-off 不代表已盖章
- [stated] 2026-10-12 用户已把 SOW clean 版、cross-check、英文逐段对照、蓝图细化清单四件套发给 Vivian 并抄送 Ivy
- [stated] 截至 2026-10-23：开发合同盖章原计划 10/20–10/30，状态仍待确认；o9 合同盖章、kick-off 拟 11 月，未定日期（10/19 初步说法是 10 月底／11 月初）；10/22 Elsie 说项目还没真正启动
- [stated] 三供应商对接会：10/20 倾向 12/7 或 12/14 当周，未定（早先说 11 月）
- [stated] Vivian 2026-10-29 明确要求：三供应商集成对接会召开并对齐之前，不得签收（sign off）AI SF 用户需求；这一条本身也要写进用户需求
- [stated] Ivy 要用户掌握 kick-off 日期，并提前锁定她的时间（10/19）
- [stated] 工期都是估计，不是承诺：历史讨论约 10–11 个月；ICC 9/29 说 9–10 个月、2027-07 上线；10/13 估 UAT 在 2027 年 5–6 月；SOW 约定签署后 140 个工作日内部署试运行
- [stated] 阶段：签署启动 → 蓝图 → 开发 → 试运行（含 UAT 并部署到生产；合同稿约 3 个月，1008 SOW 未写时长）→ 上线 → 陪跑 3 个月 → 质保 12 个月；试运行、陪跑、质保都考核准确率底线
- [stated] 签约主体待核：SOW 甲方写深圳，ICC 9/29 说是香港

## 范围与口径（1008 SOW）
- [stated] 范围：中国大陆线下门店，含钟表，不含电商（10/14 访谈中一度说不含钟表，随即更正）；首阶段只做内地，港澳及国际的门店目标来源待定
- [stated] 预测约 18 个月／78 周，周／月颗粒度；输出 RSV、QTY、ASP、Discount；各层级须满足 RSV = QTY × ASP，汇总 ASP = 汇总 RSV ÷ 汇总 QTY
- [stated] 1008 文本：ASP = RSP − Discount（折扣金额）；9/16 旧术语表"RSP × 折扣率"已被取代，折扣用率还是金额待蓝图统一
- [stated] 预测 = Baseline + Drivers；Adjustment 承接 PT／DSC 的调整；RMIP 门店指标分配以 DSC 组货和库存为约束，区域复核后经 CTF 确认锁定再推下游，最终门店指标要与 PT 对齐
- [stated] 库存和组货只在第二阶段（目标分解、拆门店）作为约束，不直接改 Baseline；但意臣本期仍须接入这些输入
- [stated] System／Adjusted／Consensus 三类版本分开保存；正式预测须 FP&A／管理层确认后才推下游；会员因子是 Nice-to-have；因子清单在蓝图阶段书面确认，可配置可扩展

## 验收与准确率
- [stated] 准确率 = 1 − |预测 − 实际| ÷ 实际（实际为 0 而预测不为 0 时记 0）；底线：全国全货类 ≥92%、门店全货类 ≥85%，均取前三个月单月准确率的算术平均
- [stated] 过去 12 个预测点的全部值里至少 75% 达标；SOW 示例 12 × 6,000 = 72,000 个值、至少 54,000 个达标——72,000／54,000 是考核值的数量，不是门店数，6,000 只是示例门店数；75% 是达标占比，不是整体准确率 75%，也不等于 MAPE（原文"即 MAPE"有歧义，要在蓝图里用算例澄清）
- [stated] 重大例外须证明全国范围内 >10% 的可直接归因影响，并经双方书面确认；10% 只是启动评估的门槛；金价波动不适用；正常业务变化带来的调优属于质保，不算变更
- [stated] 单版本运行 ≤3.5 小时，前提是数据按时完整、算力满足蓝图配置

## 蓝图准备与现行滚测
- [stated] 蓝图细化清单（10/12 版）：75 项蓝图事项（18 项是 SOW 逐项明示，57 项属总括条款下的细化）＋13 项其他确认；不要退回旧的 154 项清单
- [stated] 2026-10-14 访谈 FP&A 现行滚动预测（以 FY27 6+6F 为样本），拿到九份模型底稿并画了中英文流程图，待业务反向确认；这是蓝图前的准备，不是蓝图启动
- [stated] 现行滚测 = 选定的上一版 + 本轮变化（6+6F 对 3+9F，7+5F 对最新 6+6F）；上一版滚测不等于 AI Baseline。大滚测（3+9／6+6／9+3）拆地区和门店目标入系统，小滚测（如 7+5）主要给管理层参考
- [stated] Excel 模型：1.0 中间模型（RSV／QTY／ASP）、2.0 级联（三个调整入口 flow_fromRSV／flow_fromREV／flow_plugin）、地区 review、3.0 Scorecard、4.0 重点系列（可直接取 1.0）——不是固定的 1→2→3→4 串行
- [stated] 条件性风险：一次性因素如果已在 AI 历史基线里，再加对应 Driver 会重复计算；建议 FP&A 与 ICC 明确历史特殊因素的识别、清洗和验证规则
- [stated] 情景数量、假设和基线选择留待需求调研（10/21 Vivian 说"选中间情景"只是举例）
- [stated] 用户自己的 Driver 治理设计思路（不是合同字段）：Must-have／Nice-to-have、用途标记、验证状态、适用范围、对应 SOW driver group
- [stated] 2026-10-27：预计供应商下周一（11/2）开始用户需求调研，此前尚未讨论需求；用户要维护一份 AI SF 用户需求收集清单（格式仿照 Elsie 跟进清单），每天下午 5 点后根据投喂的资料、会议记录和文件自动识别更新
- [stated] 2026-11-09：随意臣需求调研推进，用户要求根据投喂的纪要和资料继续每日更新需求清单，并每天出一份中文《AI SF 业务逻辑、规则与流程说明》Word 文档（每天都发，持续迭代、细化）
````

### /areas/planning-tool.md

- 原始路径：`/areas/planning-tool.md`
- updated (UTC)：2026-10-27T09:42:44Z

````markdown
---
name: planning-tool
description: Planning Tool (Workday Adaptive Planning, vendor Novus) — Phase 1/2 scope, reporting and naming rules, CAPEX, templates, UAT plan, data-source mapping
sources: [cowork]
aliases: [PT, Planning Tool, Workday Adaptive, WAP, Submission Tool, 财务规划工具]
---

## 基本
- [stated] 基于 Workday Adaptive Planning；实施方 Novus：[[dennis]] 主导，[[issac-lau]] 是技术负责人（报表／OfficeConnect），[[andy-wu]] 负责资源与估算，Fiona 是讲粤语的顾问、可做现场支援；Vivian 是 PM，Ivy 是 Sponsor；Submission Tool 是旧称
- [stated] Phase 1：各市场按模板上传，Actual 和 Forecast 都是人工上传，系统做集中汇总和版本管理；不含数据集成，不能承接 AI SF 的调整回传；有基础汇总和比率，但 BS／CF 与 P&L 不联动，只有汇率调整由系统计算
- [stated] Phase 2：driver-based 模型＋从源系统取 actual＋接口；最早 2027-04-01 才能 kick off（前提是 FY28 预算获批并签约，Vivian 10/8、10/13 口径）——是启动不是上线；9/16 Dennis 说的"2027 年 1 月启动、8–9 月上线"已被取代
- [stated] Phase 2 候选：三年战略规划、门店级 P&L、AI SF 衔接、实际数据集成（DSC、SAP 等）、Approved Budget 集成等；10/20 请 Andy 以原 Phase 2 报价为基线粗估新增项，用于向 Patrick 和 Karen 做预期管理，不等于预算获批
- [stated] Planning Tool 会议纪要默认用 Vivian 的四列表：Ref. | Key requirements | Follow-up actions / open items | PIC（中文：序号｜关键要求｜后续行动／待确认事项｜PIC），每种语言各一页
- [stated] 模块 tracker 由 Vivian 分享现有版本（10/8），不另建平行的签收表

## 报表与 Dashboard
- [stated] P&L、BS/CF 用 Webform；CFO P&L Scorecard 用 OfficeConnect
- [stated] Ivy 要先看年度全貌和关键差异，再按需下钻到季度／月份、市场／品类；下钻在主表原位展开，不另设下方"差异定位"区或弹窗
- [stated] 比较：Current Forecast 对比 PY、Budget（固定比较版本）和 Previous version；Previous 不等于 PY
- [stated] P&L 有千元／百万元两版，默认看概要、按需下钻；金额按元填报，门店数按个数
- [stated] Workday 里 Dashboards 是输入页，Reports 是输出报表，两边命名必须一致；Dashboard 改名：HY → Half Year、RSV and Volume → Topline；SG&A 顶部参考行由 NOP 改为 Revenue
- [stated] Phase 1 标签统一用英文（中文／双语留到后续阶段）；业务数据可以含中文，A&P UAT 要测繁体、简体、英文混合文本
- [stated] 时间维度要纠正月份对应的财年，自然年月／季度／半年标签统一并兼容 Excel（Dennis 与 Issac 核对重载方案）
- [stated] 库存报告（10/21 下午第一场会）：主要货类直接展示，支持自营／加盟比较；层级、成品／原料、版本用选择器；先做 Value、Quantity 两份报告，财务主看 Value；库存调整／拨备和 Gold Loan Balance 只在集团视图
- [stated] 库存输入页／Dashboard（10/21 17:00 会）：同一页显示数量、金额、单位成本和 KPI，周转天数与月数同时显示——与上面的报告是不同对象，不要混为一个要求
- [stated] 库存预算新增"单价 20 万以下"的库存金额和周转目标（ASP Range 是暂名）；两档分别上传再汇总，还是 Total＋低价档用动态公式补差，尚未决定；币种和边界待定；Elsie 征询各市场后反馈 Dennis，争取在 UAT 前
- [stated] Cash Flow（Karen 要求）：区分经营与融资／投资现金流、生产用金与归还黄金借贷用金的采购；Arthur／Jay 出修订稿（目标 10/22），Vivian 把关，Dennis 重载模板并重设汇率调整；未见完成证据
- [stated] OTB 成品分类保留 Watch，去掉 Service Income、Jewellery Trading 等不适用项；原料按物料分类、含 Gold、按产品用途细分
- [stated] 门店数：保留分类与总数、期末口径；Business Model Change 拆成转入、转出两行；自营／加盟填报后生成内地 SSSG、ASP
- [stated] Store Concept（原称 Image）：Fashion（最高端）／Luxury／Main，Watch 是否也算内地的 concept 待确认；只需按 concept 拆期末门店数；concept 视图显示两位小数，用来提醒用户把百分比分配出来的小数取整后再上传
- [stated] 10/21 会议：除 Cash Flow 外，输入模板和 Dashboard 格式获认可，B/S 无新增修改；库存／OTB 仍有调整——不等于功能签收
- [stated] 评审节点（10/21 纪要）：最终 P&L／CFO Scorecard 评审由 10/23 改到 10/26，库存报告 10/27 评审

## 命名标准化（2026-10-22 Vivian 交办）
- [stated] Vivian 已在 P&L detail 和 CFO Scorecard 两张 sheet 里标出要改名的项（空白表示不用改，不是不要这一行）；用户负责整理成完整的 to-be 版本（用颜色区分改动）发给 Dennis 并跟进，力争在 10/26 评审前改完，下周五 FP&A 最终 demo 前全部一致；用户要向 Dennis 申请 Workday 权限以便核对
- [stated] 规则：参照年报用词和英式拼写（Karen 偏好，如 Normalised）；尽量用 long form；标题／分组每个词首字母大写，具体费用项只大写第一个词；"/" 前后加空格（如 F / IF / TF）；产品顺序在所有 dashboard 和 report 里保持一致
- [stated] 具体改名：Store Count（不加 s）、Closing → Closure、Wholesale 大写、Watch → Watches、NGP → Normalised Gross Profit、Finance Costs、含糊的"Others"改为 Other SG&A Expenses／Other Income 等
- [stated] Region 单独出现用全称（China、Hong Kong and Macau、International）；后面还接其他词时用短名（如 CN e-commerce、HKM e-commerce；International 的短名以 Vivian 文件为准）
- [stated] Capex Subsidy 是 SAP 将来新增的科目，先在 P&L 里加上；Share of Profits and Loss of Associates 因有 JV 要拆分

## CAPEX、IT Spend 与模板
- [stated] CAPEX 展示层级（10/16 最新截图）：Store／IT／Office → Approved／Budgeted → Region，尽量下钻到项目；Approved = BD committee 已批准，Budgeted = 预算假设／申请项目；两者是否互斥、能否相加未定；PSC 仍在范围内
- [stated] CAPEX 按 A 单审批金额、项目开始日期归期；折旧从资本化日期起算；付款按各期付款月进现金流；Office 折旧进 SG&A，PSC 折旧进 COGS（会中要求，待核系统与政策）
- [stated] IT Spend 同一张表填 CAPEX 和 OPEX，按 Expense Type 映射；付款日期拟按"开始日期＋标准间隔"自动算（2／3／4／5 个月只是试算），会中方案最多 4 期
- [stated] Dennis 已提供 Store、IT、Office、PSC、A&P、Professional Fee 六份原生导入模板，不要再列为待索取
- [stated] 各模板共同字段放前面，名称和顺序一致：Level/Market、Grouping/CXO、Department Name、Cost Center、COA；模块专属字段放后面；报表可以按需定制
- [stated] Cost center 四列：Name、Code、Parent、Short Name；没有依据时 Parent 留空；用户正与 [[cai-kun]] 补 EAS 成本中心的 parent 层级供导入

## UAT 与上线
- [stated] 19 项 UAT 主题（Ivy 10/20 总体认可）要转成业务场景和脚本：Dennis 先列场景 → FP&A 检查 → 写脚本；保留清数／清零和 Actual overlay 测试；P&L 为主线，同时覆盖库存、BS／CF
- [stated] 排期草案（未锁定，待 Vivian 发邮件确认）：Ivy 10/20 希望小专场和 BS／CF 尽量在 11/15 前、P&L 端到端避开 HQ 11/16–18；Vivian 与 Dennis 草拟 CF／BS／NOP→NP 约 11/17、P&L 端到端 11/19–20、11/23–24 不排、11/30 当周签收（也提到 12/3–4），之后测 SSO、约两周部署；10/21 Ivy 改为先测现金流，拟 11/10 半天
- [stated] 排期约束：市场 P&L 11/13 提交、库存 11/17 提交；Karen 评审在 11/18 和 11/20
- [stated] 参与方：核心是 China、香港、HQ；International 由用户模拟上传（不代表排除）；小专场和端到端都需 Novus 现场支持；UAT 用非 SSO 临时账号，上线前另测 SSO；每场 UAT 前做 10–15 分钟培训，用户在 UAT 前先自测流程（草案）
- [stated] UAT 代表草案（10/21，约 5–8 人）：China P&L 陈丹娜（待定）、库存 Nana、现金流 Jay、香港 Zoe、HQ Yetta，International 由用户代表
- [stated] 用户要了解中国区预测的实际流程来协助测试（可能要去香港／深圳支持，待排期）
- [stated] 首次业务使用：FY27 9+3 线下定稿，圣诞前后装进系统；2027 年 1 月第一周实际化 12 月 Topline 并上传 FY28 Topline，赶在 2027-01-11 Karen 的 Topline 评审前用系统完成汇总；Ivy 要求那一周 HQ 有 Novus 现场支持
- [stated] UAT 数据：可考虑用 FY26 历史真实数据并复用到生产（维度要齐全）；如果用 dummy 数据，正式主数据必须在上线前补齐
- [stated] 首轮上线只开少数代表上传（每个市场／团队一人），稳定后扩面；Dennis 负责 UAT 和正式培训，按角色分场；SCM 的上线上传人向 Elsie 确认

## 数据来源与自动化（为 Phase 2 估算做准备）
- [stated] 用户维护《Planning Tool 数据来源与自动化 Overview + Mapping》（10/22 为 v5），回应 Ivy 10/19 的要求（D01 数据来源、D02 自动化路线图、D03 集成估算，Ivy 提议约 2–3 周后集中讨论）；科目取自 Workday Account Structure；第一批 P&L＋Inventory，第二批 BS & CF
- [stated] 10/22 Dennis 建议按系统反查字段（而不是逐个字段找来源），并把 Actual 来源和 Forecast 逻辑分开——Forecast 多由 baseline 和假设算出，颗粒度与 Actual 不同
- [stated] Dennis 10/22 的记录和判断（未经 ICC 确认）：Actual 在 SAP 与 Lucanet，供应链在 DSC（o9），Approved budget 在 EAS（EAS 与 PT 之间的数据方向未定）；AI SF trendline 拟作 RSV／Qty 预测基准；AI SF 不覆盖库存
- [stated] 2026-10-27：讨论 Phase 1 时用户（业务方）提出了很多 Phase 2 需求；用户要单独维护一份只含 Phase 2 的用户需求收集清单（与 Phase 1 无关，格式仿照 Elsie 跟进清单），每天下午 5 点后自动识别更新
````

### /areas/dsc-o9.md

- 原始路径：`/areas/dsc-o9.md`
- updated (UTC)：2026-10-22T21:50:38Z

````markdown
---
name: dsc-o9
description: DSC / o9 digital supply chain project (MFP/OTB) — finance-side role, Release 1 finance UAT status, the user's own actions, open business-logic issues, plan dates
sources: [cowork]
aliases: [DSC, o9, O9, MFP/OTB, 数字化供应链, DSC-O9]
---

## 定位与计划
- [stated] 数字化供应链项目，平台 o9，由供应链与 ICC 主导；Finance 关注财务目标、数据输入输出、库存与周转口径和财务 UAT；用户不是 DSC 总体 PM，也不对全部测试负责
- [stated] DSC 项目 PM 是 [[sun-fangyu]]；财务侧对口是 [[elsie]]
- [stated] 计划（CTF 计划页，未注明日期；10/09 时间线标"基线待复核"）：MFP／OTB 2026-11-30 上线 → 12 月试运行 → 编 FY28 MFP／OTB；AP 组货计划、DP 需求计划 2027-01-31 上线 → 2 月试运行 → 约 3 月启用
- [stated] 10/15 o9 口径：Release 1 UAT 10 月底前完成，11 月底技术上线、12 月可用——都是计划

## 范围与 UAT 状态
- [stated] Release 1 不含 1.4 门店目标和 1.7 最终成品／原料 OTB（属 Release 2）；1.5.3／1.5.4 原料 OTB 在工作簿里列为"满足前提才测"，10/15 o9 明确本阶段不含；1.0.4 零售日历、1.0.5 汇率本期不测；1.6.3 财务视角成品 OTB 滚动是否在本期，工作簿与 10/15 邮件冲突，至今未裁定
- [stated] 财务 UAT 10/19 开始，Release 1 财务相关测试正在进行；只测了自上而下，自下而上要等 DP 配置，异常输入未测；没有整体通过、缺陷关闭或财务签收的证据
- [stated] 10/22 财务问题清单 22 条是混合状态：产品 bug 只有 1 条（Rita 财务目标上传部分成功、失败行未进 bad records，已提 ADO，未见关闭），其余是 UI／模板、暂列 CR、数据和澄清类；目标仍是 Excel 人工上传，接口要另行联调
- [stated] 会上要求 o9 的进度材料分清已完成／pending／待决，不要用"100%"；CR 只是暂列
- [stated] 财务 UAT 分工（10/16 矩阵）：[[shen-na]] 对接内地目标；[[rita]]（张晶）提供数据与参数；阿环在顺德实操港澳及海外目标上传，[[zoe]] 复核；[[yuan-feng]] 核验成品 OTB 链路；[[caroline]]（商品计划）负责 1.2、1.3（与 Elsie）、1.6.2 并做 MFP 系列拆分；Elsie 协调；用户组织 1.5.5 场景和财务跨模块统筹；最终签收人未定
- [stated] Rita 的首版数据已交 o9（10/19 说由 o9 代导入）；她自行上传、账号、参数正确性和实测通过都还没有回执

## 用户在 DSC 的行动（10/22 起，未见完成证据）
- [stated] 主持 17:30 的 UAT 收尾会（10/19、10/20 已开）并汇总报给 Elsie；收尾会上提出补测场景和手改成本的联动
- [stated] 提出三层验收：关键测试通过、缺陷处置及修复后复测、关键用户签收；Elsie 支持，并要求明确 P1／P2 和遗留问题比例；由用户联系孙方雨，推动项目组、ICC、业务统一标准（85%／90%／10% 只是讨论时的举例）
- [stated] 确认财务 1.1–1.5 之间是否已联动；端到端要验证内地／港澳输入、集团汇总、后续调整，以及 Caroline 的 MFP 拆分对上游和 OTB 的影响；Elsie 建议约半天联合测试（未排）
- [stated] 修改三系统数据流图，三方会议前约 Elsie、Ivy 过一遍流程（见 [[project-connections]]）

## 业务逻辑未决（10/22 核心逻辑会）
- [stated] 最优先：RO 已占预算、但还没转成 ICS PO／O3 在产订单的那部分差额；如果只按 O3 预计到货倒推 OTB，会重复释放额度、导致超买；要梳理差额、防止遗漏和重复扣减，算法和主责未定
- [stated] 大量 RO 长期未转 PO，清理制度没执行；"RO 应一周内发出"只是流程改善方向，不能替代解决差额；RO／PO／O3 简化只在讨论；DP 的输出就是 RO，两者要衔接
- [stated] 财务要求期初库存保留实际成本，未来流量可以估算；o9 同意用同一批历史数据对比线上牌面价折算和线下成本两套逻辑，先与黄元凤、沈娜对齐再同步 Elsie；未决定切换算法，线下测算人待落实
- [stated] 加盟库存：财务库存不含已卖给加盟商的货（其 COGS 已体现）；为加盟备货但还没转移的货仍属 CTF；供应链按牌面价算的周转与财务按成本算的周转，要先统一范围才能比较
- [stated] 原料 OTB 层级"缺数据"的原因未明：o9 说部分原料主数据要手工上传，Elsie 认为 ICS 应有底层物料，可能缺映射／汇总／集成；要拿样本和取数路径，确定人工下载、加工、上传的责任
- [stated] 预计到货日已过的在产订单，暂定滚入下一周继续滚动——临时方向，待验证
- [stated] 线上成本率取值优先级（o9 当场演示，未经 UAT 验证）：计价类 近一月销售成本率 → 近三月 → 业务分类成本率；定价类 近一月入库成本率 → 近三月 → 业务分类成本率；手工维护值可覆盖
- [stated] 原料 Mapping：复用 SAP 现行原料采购预算分类，由黄元凤重发、项目组核验——重发、匹配、验证、解除阻塞是不同状态
- [stated] 1.5.5 场景分析优先验证基线、金价、销售目标和组合变化，观察 ASP、件数、库存、周转、OTB；计价类与定价类分开；补测批发率、成本取值规则和手工调整
- [stated] 门店目标接口：Vivian 要求 DSC 沿用 AI SF 的门店目标，但 o9 认为只接 PT、不接 AI SF；Elsie 记得 MFP 蓝图只到区域；港澳／国际门店目标来源未定，可能成为 CR
- [stated] 口径：RO = demand order，PO = purchase order，提前期分 RO→PO 和 PO→receipt；WOC 不等于财务周转或 DII（见 [[ctf-business-glossary]]）
- [stated] 当前要 Elsie 跟进的事项见 [[elsie-follow-up]]
````

### /areas/project-connections.md

- 原始路径：`/areas/project-connections.md`
- updated (UTC)：2026-10-22T21:50:46Z

````markdown
---
name: project-connections
description: How AI SF, Planning Tool and DSC/o9 connect — E1–E5/X1 flows, granularity, store-target source dispute, model chain, Phase 2 timing gap
sources: [cowork]
aliases: [Project Connections, 三系统关系, 跨项目, E1-E5, 三方会议, 三系统数据流]
---

- [stated] E1：AI SF → PT，预测／趋势线，用于与 driver-based 目标比较
- [stated] E2：PT → AI SF，相对指定基线的调整差额（例：目标 120 对预测 100，差额 20），由 AI SF 按产品和门店重新分配（PT 没有门店层级）；同一差额只用一次，需冻结基线 ID、批准版、维度、期间和重传规则
- [stated] E3：AI SF → DSC，门店×产品目标（趋势＋调整＝目标，总额与 PT 一致）
- [stated] E4：DSC → PT，库存结果（库存余额／KPI）
- [stated] E5：PT → DSC，下一周期修订后的库存 KPI／目标（9/15 v3 图里的构想，10/21 数据流 15.2 同向）；X1：Finance → DSC 财务目标，只见于早期手册，PT 是否承接待确认
- [stated] 以上都是目标态的业务关系，目前没有任何已上线接口
- [stated] 门店目标来源仍有冲突：Vivian 10/21 要求 DSC 门店销售目标沿用 AI SF 的门店×周×货类分配结果，不要从 PT 大区数另拆，需与 Elsie 等核对原始 Excel 并在三方会议确认；o9 认为只接 PT、不接 AI SF；Elsie 记得 DSC 蓝图只到区域
- [stated] 颗粒度：PT 规划到区域×货类，不到门店（中国四大区与 Monologue 分列，正式层级名称待核）；AI SF 到门店×周×货类；目标按日入系统——需统一财历和跨月周，不能简单月 ÷ 4
- [stated] 10/21 审阅的数据流版本：10.3 暂保留（货类分配及 RGM 审阅后变化的回传校验），15.2 把管理层批准的期末库存用于下一轮预测；编号只适用于该版本
- [stated] 期初库存来源未查清：DSC 实际从哪取数、Lucanet 是否有门店粒度、是否已有集成、Excel 是否是中间加工步骤、谁维护
- [stated] 三系统数据流图约两个月前画的，早于 AI SF 供应商演示；三方会议前要请 Ivy、Elsie 重审，标出仍有效／已变化／未决
- [stated] 集团／市场财务目标原则上以 PT 为准；PT 和 o9 覆盖内地、港澳、国际，AI SF 首阶段只做内地，其他市场的门店目标来源待定（是否涉及 CR 未定）
- [stated] 模型链（CTF 页面，日期未知）：M1 预测（门店×周×货类／系列）→ 业务调整 → M2 门店目标分配（门店×周×货类，参考 M3 组货计划 AP）→ 门店级 MFP → M4 DP（门店×周×SKU，26 周）→ 驱动 OTB；M1／M2 属 AI SF，M3／M4 属 DSC／o9，SKU 级在 M3
- [stated] 上线时间差：AI SF 上线时 PT Phase 2 未必就绪；当前方向是在 PT 内做简易数字调整及回传、以后再扩展 driver（10/10 交 Vivian 审阅，未获批）；Excel 备用方案用户已于 10/9 删除，不要恢复；1008 SOW 里"PT Phase 1 调整通过模板导入"的合同条款仍在
````

### /areas/finance-systems-weekly-report.md

- 原始路径：`/areas/finance-systems-weekly-report.md`
- updated (UTC)：2026-10-22T21:50:58Z

````markdown
---
name: finance-systems-weekly-report
description: The user's weekly Finance Systems portfolio report to Vivian — fixed structure, confirmed visual baseline, language order
sources: [cowork]
aliases: [Finance Systems Weekly, 财务系统周报, 周报模板]
---

- [stated] 每周五给 [[vivian]] 的财务系统项目周报：固定三行 AI Sales Forecast、Planning Tool Phase 1、DSC / o9；四列：项目与状态／本周进展／风险与依赖／下周重点及近期计划
- [stated] 专项区只在用户当期提前指定时才加，不沿用上一期（10/16 是 Rolling FC，10/23 是三系统数据流）
- [stated] 先出中文 PNG＋原生可编辑 PPT（文字和表格都可编辑）；中文确认或用户要求翻译后，再出英文 PNG＋PPT；两种语言的日期、状态、内容一致
- [stated] 已确认的视觉基线（10/16 红灰版）：主红 #CA001B、表头浅灰 #F4F2F1、风险列底色 #FCF7F8、网格 #D7D4D2、正文 #111216、辅助文字 #626978；中文 Noto Sans CJK SC，英文 Noto Sans；不再用早期蓝金／酒红金线版；不固定 16:9
- [stated] 分享版不恢复已删掉的顶部目标摘要、信息截止时间行、底部说明／来源行；来源和刷新时间放备注
- [stated] 近期 10／11 月计划和"下周承诺"分开写；预计盖章、计划上线不能写成已完成
````

### /areas/elsie-follow-up.md

- 原始路径：`/areas/elsie-follow-up.md`
- updated (UTC)：2026-10-22T21:50:54Z

````markdown
---
name: elsie-follow-up
description: The cross-project follow-up list the user keeps for Elsie — fields, inclusion rule, current items
sources: [cowork]
aliases: [Elsie tracker, Elsie 跟进清单, Elsie follow-up list]
---

- [stated] 2026-10-22 用户要建一份 Elsie 跨项目跟进清单，放在线上、每天更新；字段：Item、Topic、Description、Priority、Status、Solution proposal、Raised date、Target date、Last updated；现有 Excel 版是中英双 sheet
- [stated] 只收与 [[elsie]] 相关、需要她跟进的事项，按 MECE 去重和复核
- [stated] 10/22 的 4 项：① RO／PO 预算占额缺口（P1，待确认）② 实际成本与周转验证（P1，待验证）③ Planning Tool 库存报告的集团／市场视图（P2，待确认）④ Planning Tool 20 万价位段（P2，待确认）；目标日期都还空着
- [stated] 在线表放在哪里、每日更新机制，都还没有确认建立
````

### /areas/fy28-budget.md

- 原始路径：`/areas/fy28-budget.md`
- updated (UTC)：2026-11-05T07:39:14Z

````markdown
---
name: fy28-budget
description: FY28 Budget FX and gold-price guidance from HQ (Yetta, Aaron Fung): RMB 0.8516, gold 4,200–4,400 USD/oz agreed with Karen; restricted circulation
sources: [chat]
aliases: [FY28 Budget, FY28 预算, FY28 预算假设, FY28 汇率指引, FY28 金价指引, FX Guidance, Gold Price Guidance]
---

## 来源与分发
- [stated] 2026-11-04 Aaron Fung（馮家朗）发出 FY28 Budget FX Guidance；11-05 [[yetta]] 回复全组：RMB 汇率假设更新为 0.8516，并附经 [[karen]] 确认的 FY28 黄金价格指引（4,200–4,400）；附件为《FY28 Budget FX guidance - sent v2》《FY28 Budget 黄金价格指引 Gold Price Gudiance v3》
- [stated] 收件人包括内地、香港市场财务同事（如 [[anita]]、[[zoe]]）、[[vivian]] 和用户；抄送 [[ivy]]、[[elsie]]、Arthur 等
- [stated] 邮件要求只在当前收件范围内使用，不向其他团队转发或传达

## 汇率（FY28 Budget；表中为 1 港元折合的外币，金价表按 RMB/g = HKD/g × 0.8516 换算）
- [stated] CNY 0.8516、USD 0.1277（约 7.83 HKD/USD）、MOP 1.0309、TWD 4.0621、MYR 0.52、SGD 0.1628、BWP 1.75、EUR 0.113、JPY 20.2、AUD 0.183、GBP 0.097、NZD 0.22、CAD 0.18、KRW 172.7116、PHP 7.8、THB 4.2786、AED 0.467、VND 0.0003、IDR 0.00043、MXN 0.41
- [stated] CNY 历史：FY24 均值 0.9067、FY25 0.9151、FY26 0.9077、FY27 4–9 月均值 0.8655、FY27 9 月末 0.8544

## 金价（Market gold price，USD/oz）
- [stated] FY28 Budget：期初 4,200（承接 FY27 7+5F 的 2027 年 3 月期末），每月线性 +50/3，到 2028 年 3 月期末 4,400；全年均价 4,300，Q1–Q4 均价 4,225／4,275／4,325／4,375
- [stated] 换算：HKD/g = USD/oz × 7.8 ÷ 31.1035，RMB/g = HKD/g × 0.8516；FY28 全年均价约 HKD 1,078/g、RMB 918/g
- [stated] 对比：FY27 Budget 5,000→5,500（均价 5,250）；FY27 7+5F 均价约 4,404、期末 4,200；FY26 Actual 均价约 3,788、期末 4,504
- [stated] 工作簿里另有隐藏的 FY27 各版滚动预测 sheet（1+11F、2+10F／3+9F、4+8F、5+7F、6+6F、7+5F）；FY26、FY27 Budget 行的 RMB/g 仍按旧汇率 0.9169 换算
````

### /areas/finance-legal-forum.md

- 原始路径：`/areas/finance-legal-forum.md`
- updated (UTC)：2026-11-09T01:51:31Z

````markdown
---
name: finance-legal-forum
description: Quarterly Finance & Legal team forum at Chow Tai Fook — 2026-11-06 session: Karen's review, T&E policy, Flora's international plan, new joiners, recognitions
sources: [chat]
aliases: [财务法务 Forum, 财务法务团队会议, Finance Forum, 季度 Forum]
---

- [stated] Karen 主持的财务法务季度 Forum，已连续三个季度举办，包含 recognition 环节；Karen 本人的发言要点记在 [[karen]]
- [stated] 2026-11-06（15:04–16:58）一场：用户作为财务系统新同事被介绍（线上参加）；同场介绍 Rebecca Chu（朱秋华）新任集团 VP Controller，此前在 Hutchison 等，熟悉海外、内控和共享服务；上海 FP&A 新人含黄慧、张晶、陈鑫、乔宏达
- [stated] 员工调研行动（Ben、荣英为文化大使）：弹性上班、加班空调、阿福 AI 答疑（下单、报销等）、FP&A 服务岗对口业务、每月更新内部职位、季度发展对话、与 HR 建胜任力模型；团建等 FY28 预算定后再推
- [stated] 小林姐介绍 9 月出台的新 T&E 政策：出差餐费归 T&E；职级简化为两档；取消每日交通限额；改实报实销；报销时限改 30 天内；优先用差旅平台和集团推荐酒店；公司统一买出差险；内控、内审会检查执行
- [stated] Flora 讲国际业务：覆盖 13 个国家，四种模式（直营、travel retail、franchise、MSA）；10 月新开美国、迪拜，卡塔尔机场在开；FY28 去越南，净开店目标 18 家
- [stated] 表彰：Ivy 带 FP&A 搭三年目标和 FY28 目标，她感谢 Anita（China）、Elsie（inventory）、Arthur（cash flow），并称 Yetta 从零搭了这个模型；Frank 带小组做财务数据验证，让 Power BI 报表数据一致，现在帮 LC 在 BI 里做 inventory standardization
- [stated] Vivian 表扬财务系统团队（蔡坤等）：靠 AI 阿福和自动化，9–10 月人工处理的 EAS 查询同比降约 47%；SAP S4 于 4 月上线后团队承担更多系统维护
- [stated] Legal（Maggie）：集团合同管理政策已发布；线上合同管理平台 9–10 月香港上线，内地约 12 月上线，之后海外
- [stated] 茶歇时有同事聊 AI SF 准确率：现按全国 92%、门店 85%，提出可能还要按 product mix 等场景评估，想先内部讨论一版 proposal 再给对方（说话人未确认身份）
````

### /areas/colleague-observation.md

- 原始路径：`/areas/colleague-observation.md`
- updated (UTC)：2026-10-18T14:49:37Z

````markdown
---
name: colleague-observation
description: Weekly working-style observation of Chow Tai Fook stakeholders (Vivian, Ivy focus) built from user's meeting notes
sources: [chat]
aliases: [协作观察, 关键人物协作观察, weekly people analysis]
---

- [stated] wants an ongoing weekly analysis of how [[vivian]], [[ivy]], [[karen]], [[elsie]], [[anita]] work, fed by their meeting notes/chats/tasks, continuously iterated; focus on Vivian and Ivy
````

### /topics/ctf-business-glossary.md

- 原始路径：`/topics/ctf-business-glossary.md`
- updated (UTC)：2026-10-22T21:51:05Z

````markdown
---
name: ctf-business-glossary
description: CTF business terms, metric definitions and product-category codes the user works with — read before interpreting RSV/REV/ASP/NGP/WOC/RO/PO or category codes
sources: [cowork]
---

- [stated] RSV（零售销售额）不等于 REV（公司收入）：直营、加盟寄售、加盟批发下的转换逻辑不同，不能用单一比例换算
- [stated] NGP：10/22 命名标准化定为 Normalised Gross Profit；不是净利润
- [stated] ASP：同口径 ASP = 总 RSV ÷ 总 QTY，不能把各子项 ASP 相加或简单平均；AI SF 1008 SOW 写 ASP = RSP − Discount（折扣金额）
- [stated] SSSG：同店 RSV 相对同店基数的增长，不等于全店同比；门店数是期末存量，不能逐月相加
- [stated] Forecast、Budget、Target、RMIP（门店指标分配）用途不同，不互相替换；Current 和 Previous 是具体的预测版本，PY 是上年比较
- [stated] WOC、DII、库存周转次数／天数／月数不能互换；比较前要统一期间、数量还是金额、币种、售价还是成本、平均还是期末库存、所有权范围
- [stated] RO = demand order（需求单），PO = purchase order（采购单），O3 = 在产订单；提前期分 RO→PO 和 PO→receipt；franchisee stock collection 指加盟商取货，不是收款
- [stated] Sign-off、合同审批、双方用印、文件命名是不同的事；SIT、UAT、缺陷关闭、业务签收也要分开
- [stated] 主类代码（product nature 字典，主组字段 material_nature_group）：F 饰品／工艺品黄金、R 定价黄金、RU 黄金镶钻、A 钻石、K 玉类、J 宝石、C 珍珠、E 西金、PT 铂金、B 素金其他、MX 镶嵌其他、PA 包类、M 手表、M2 钟表配件、H 修理单、OX 展品、OZ 藏品、Z 赠品、ZZ 不适用、ZX 礼券、IF 工艺金条／金章、TF 投资黄金
- [stated] 报表层级不等于字典代码：报表的"Gem-set (A)"是镶嵌类父层（含钻石、RU、和田玉、宝石、玉、珍珠、镶嵌其他）；"K gold"是西金标签，不是代码 K；stock_type 是详细编码，不能凭首字母推主类；部分滚测模型把 IF、TF 并入 F
- [stated] 重点系列（Signature Collection）：传承／HUA、故宫／Palace Museum、传福／Rouge、传喜／JOIE、万相／Dawn、传颂／Project S
- [stated] Store Concept（原称 Image）：Fashion（最高端）、Luxury、Main
````

### /topics/work-learning.md

- 原始路径：`/topics/work-learning.md`
- updated (UTC)：2026-10-22T21:51:08Z

````markdown
---
name: work-learning
description: The user's ongoing learning goals around the CTF job — business fundamentals, daily learning reports, work English, Cantonese, other languages
sources: [cowork]
---

- [stated] 入职后想系统补齐珠宝零售和财务经营的业务常识与底层逻辑（数据从哪来、怎么算、谁用、对项目有什么影响），不满足于术语定义或摘要
- [stated] 2026-10-14 起要每天一篇结合近期项目和疑问的中文 Word 业务学习报告；已完成的主题：10/14 业务闭环、10/15 一轮滚动预测、10/16 一家珠宝店的钱货利润、10/17 买设备的钱怎样进入报表、10/18 从销售额算到备货资金
- [stated] 每天练工作英语口语（向英文经理汇报、工作沟通、请假等场景），希望即时纠正发音和语法，并做课后总结
- [stated] 2026-10-10 起从零学粤语（从发音开始），目标是听懂并参与 Vivian 的粤语／英文会议
- [stated] 也在慢速练韩语（配中文解释）；曾定过两周日语强化目标
````

### /people/andy-wu.md

- 原始路径：`/people/andy-wu.md`
- updated (UTC)：2026-10-22T21:51:17Z

````markdown
---
name: andy-wu
description: Andy Wu — Novus management contact for Planning Tool resourcing and estimates
sources: [cowork]
aliases: [Andy, Andy Wu]
---

- [stated] Andy Wu，Novus 管理层，负责 Planning Tool 的资源与估算／可行性
- [stated] 10/20 负责以原 Phase 2 报价为基线粗估新增范围，用于向 Patrick 和 Karen 做预期管理；咨询他的可行性不等于交付承诺
````

### /people/anita.md

- 原始路径：`/people/anita.md`
- updated (UTC)：2026-11-09T01:51:33Z

````markdown
---
name: anita
description: Anita — Chow Tai Fook colleague, one of the key users of AI SF
sources: [chat]
aliases: [Anita]
---

- [stated] one of the key users of AI SF at Chow Tai Fook
- [stated] 全名 Anita Lu Ying Jun（陆颖君），常驻上海，带中国区 FP&A topline 团队；"Anitah"是旧拼写
- [stated] 2026-11-06 Forum 上表扬团队的沈娜（搭库存模型、统一集团库存追踪报告）和 Bella（weekly sales review 统一模板；周报完成时间从凌晨提前到约晚 8 点）；Ivy 感谢她在三年目标里支持 China 部分
- [stated] 10/8 由她向 Vivian 提供初版 Scorecard；Rolling Forecast 访谈要按她团队的时间安排；指定 [[rita]] 参与 DSC 参数工作
````

### /people/cai-kun.md

- 原始路径：`/people/cai-kun.md`
- updated (UTC)：2026-10-22T21:51:31Z

````markdown
---
name: cai-kun
description: 蔡鲲 — leads mainland finance-system operations and master data
sources: [cowork]
aliases: [蔡鲲, 蔡坤, Cai Kun]
---

- [stated] 蔡鲲（Cai Kun，转写常作蔡坤），深圳，带内地财务系统运维／主数据小组，AMS 转交后承接 L1／L2 支持，也管权限
- [stated] 正与用户补 EAS 成本中心的 parent 层级，供 Planning Tool 导入
````

### /people/caroline.md

- 原始路径：`/people/caroline.md`
- updated (UTC)：2026-10-22T21:51:43Z

````markdown
---
name: caroline
description: Caroline — merchandise planning; DSC MFP testing and series split
sources: [cowork]
aliases: [Caroline]
---

- [stated] Caroline，商品计划；在 DSC 负责 1.2、1.3（与 Elsie）、1.6.2 的测试，并做 MFP 系列拆分；她的拆分对上游和 OTB 的影响需要验证
````

### /people/dennis.md

- 原始路径：`/people/dennis.md`
- updated (UTC)：2026-10-22T21:51:13Z

````markdown
---
name: dennis
description: Dennis Chen — Novus lead consultant implementing the Planning Tool
sources: [cowork]
aliases: [Dennis, Dennis Chen, Denis]
---

- [stated] Dennis Chen，Novus 顾问，Planning Tool（Workday Adaptive）实施主导：模板、报表、UAT 场景与脚本、培训；"Denis"是转写里的变体
- [stated] 已提供六份原生导入模板；FP&A 要求 UAT 和正式培训由他本人主讲
- [stated] 10/22 建议数据来源映射按系统反查字段，并区分 Actual 与 Forecast；他说明 Phase 1 的所有输入都是人工上传
- [stated] 同事：[[issac-lau]]（技术负责人）、[[andy-wu]]（资源与估算）、Fiona（讲粤语，可现场支援）
````

### /people/elsie.md

- 原始路径：`/people/elsie.md`
- updated (UTC)：2026-10-22T21:51:11Z

````markdown
---
name: elsie
description: Elsie Wong — finance-side DSC counterpart and data-governance contact at Chow Tai Fook; read before preparing anything for her
sources: [cowork]
aliases: [Elsie, Elsie Wong, 黃靖燕, Wong Ching Yin]
---

- [stated] Elsie Wong Ching Yin（黃靖燕），CTFHK；财务侧 DSC 对口，协调财务 UAT，带用户进入 DSC 工作；也是数据治理的财务对口，与 [[weng-jieyi]] 对接
- [stated] 不是 DSC 总体业务负责人，也不是所有模块的最终批准人
- [stated] 她很忙：给她的汇报控制在三点以内，只留需要她关注、协调或决策的事项（用户 10/22）
- [stated] 10/16 要用户梳理财务同事的 UAT 分工、拉通跨市场信息、提出 UAT 可接受标准；跨市场问题先由专业同事讨论，解决不了再升级给她
- [stated] 跟进事项见 [[elsie-follow-up]]
````

### /people/fang-ping.md

- 原始路径：`/people/fang-ping.md`
- updated (UTC)：2026-10-22T21:51:25Z

````markdown
---
name: fang-ping
description: 方萍 — Financial Systems teammate and the user's onboarding mentor
sources: [cowork]
aliases: [方萍, Fang Ping, mentor, 导师, 方评]
---

- [stated] 方萍，Financial Systems 团队同事，用户的入职 mentor（9/29 Vivian 提到）；导出的旧记忆曾写作"方评"，会议原件都写"方萍"
- [stated] 9/14 入职纪要记载：深圳，副总监，负责 SAP 主数据、财务流程与业务咨询
- [stated] 团队周会上汇报 OA、物料、权限等事项；10/21 这些事项没有转派给用户
````

### /people/frank.md

- 原始路径：`/people/frank.md`
- updated (UTC)：2026-10-22T21:51:35Z

````markdown
---
name: frank
description: Frank Zhou — colleague on Planning Tool report data and template mapping
sources: [cowork]
aliases: [Frank, Frank Zhou, 周帮云]
---

- [stated] Frank Zhou Bang Yun（周帮云），负责 Planning Tool 报表取数和模板映射相关工作；了解门店临时 ID、转营历史等实操
````

### /people/issac-lau.md

- 原始路径：`/people/issac-lau.md`
- updated (UTC)：2026-10-22T21:51:15Z

````markdown
---
name: issac-lau
description: Issac Lau — Novus technical lead on the Planning Tool (spelled Issac; often transcribed as Isaac)
sources: [cowork]
aliases: [Issac, Issac Lau, Isaac]
---

- [stated] Issac Lau，Novus 的 Planning Tool 技术负责人（报表／OfficeConnect 开发）
- [stated] 拼写是 Issac：10/8 屏幕账号显示 Issac Lau，用户当天更正"不是 Isaac"；转写和 AI 纪要里常误作 Isaac
- [stated] 与 Dennis 一起核对时间维度的重载方案
````

### /people/ivy-huang.md

- 原始路径：`/people/ivy-huang.md`
- updated (UTC)：2026-10-22T21:51:27Z

````markdown
---
name: ivy-huang
description: Ivy (黄凯仪) — Financial Systems teammate, a different person from Finance VP Ivy Cheng
sources: [cowork]
aliases: [黄凯仪, Ivy 黄凯仪]
---

- [stated] Ivy（黄凯仪），Financial Systems 团队同事（9/14 介绍为 CTFHK Manager，负责系统／流程项目、PMO 及协同）；与 Keith 一起负责 SAP 相关事项，团队周会上汇报 PwC 问询、SAP 权限、供应商付款等
- [stated] 与 Finance VP [[ivy]]（Ivy Cheng，鄭凱因）是两个人，不能合并
````

### /people/ivy.md

- 原始路径：`/people/ivy.md`
- updated (UTC)：2026-10-22T21:49:29Z

````markdown
---
name: ivy
description: Ivy — VP at Chow Tai Fook, senior to the user's boss Vivian
sources: [chat]
aliases: [Ivy, VP]
---

- [stated] VP at Chow Tai Fook; ranks above [[vivian]], the user's boss
- [stated] 全名 Ivy Cheng（鄭凱因），Finance VP；Planning Tool Sponsor；AI SF 项目负责人（业务目标、范围、阶段成果确认、SOW sign-off）
- [stated] 与 Financial Systems 团队的 Ivy（黄凯仪，[[ivy-huang]]）是两个人，不能合并
````

### /people/karen.md

- 原始路径：`/people/karen.md`
- updated (UTC)：2026-11-09T01:51:20Z

````markdown
---
name: karen
description: Karen — CFO heading Finance & Legal at Chow Tai Fook; her stated H2 priorities (inventory, cash flow, AR/AP/DPO, efficiency, SAP, international) and FY30 vision
sources: [chat]
aliases: [Karen, CFO, Kevin, 凯伦, Carrie, Karon]
---

- [stated] CFO at Chow Tai Fook; one of the user's key stakeholders
- [stated] P&L、CFO Scorecard、Topline 等管理报表的最终审阅人；2027-01-11 有 Topline 评审；与 [[patrick]] 同为 AI SF 高层，Planning Tool 成果和新增费用要提前向两人说明
- [stated] 很多偏好是经 Ivy／Vivian 转述的，不能都当成 Karen 本人表态；据 Vivian（10/22），她偏好英式拼写
- [stated] 统管财务＋法务团队；会议转写常把她识别为 Kevin／凯伦／Carrie／Karon

## 2026-11-06 财务法务 Forum 上 Karen 本人的发言（见 [[finance-legal-forum]]）
- [stated] 上半年回顾（只讲已公开的 top line，利润未公布不展示）：内地珠宝社零连续 6 个月负增长，行业关店、消费者更挑剔、从节庆需求转向 self-reward；CTF 内地 RSV Q1 +10.7%、H1 约 +2%，港澳 H1 约 +40%，国际约 +35%；1–9 月 YoY 持平而主要对手多为负增长，判断为抢到份额、品牌转型（第三年）有效；万象（全年公开目标 20 亿）上半年已做 27 亿，约 3,000 家店在售、要扩店；已发盈喜，净利润约翻倍
- [stated] 下半年继续推：定价珠宝占比（利润高，传颂、庆云等 key collection）、奢华店、高级珠宝（战略定位）、digitalization（自动化／智能化提效带动利润）
- [stated] 对 FP&A：分析不能只停在损益表，要扩到 balance sheet——她最关注库存和现金流；以后每次开会都会问"你对现金流、库存有什么贡献"，不会预测就尽快学
- [stated] 盯紧 AR 逾期；改善要"结构性"——改政策、流程、分工职责，而不是把催款从每周一次改成每天一次；DPO 和 AP 目前不达标，相关团队评分会因此被扣
- [stated] 她的逻辑：零售公司看库存和现金流，revenue → profit → cash；管好 AR、AP、库存就不会没 cash
- [stated] 期望各人作为自己领域的专家主动发现机会点并说出来，不要等她开口
- [stated] 认为财务对国际业务支持"太幼儿园级别"；点名 Flora（FP&A 国际）、Control Rebecca、小林、Tax Anita、法务 Maggie、LC 供应链要支持 Gabby 团队开店；强调税务筹划和最优架构
- [stated] 提效：上半年只是"她出声才走一步"；先改做事方法、财务政策、分工和资源分配，不要一上来就想 AI；同时推 SAP 和 AI 自动化（对账、录单、填表），一直在 push 小莲、小思，要求"跑起来"
- [stated] SAP 路线：HKM 前年先上做试水（遗留很多尾巴，她是预期的），现在 roll out 到 International，之后内地也会准备 SAP roll out
- [stated] Risk management 除风控外要做 process review 提效；Legal 要建海外 new market entry SOP，并与 HR 在劳动诉讼上配合更好
- [stated] FY28 预算流程刚 kick off；愿景：FY30（转型第五年、100 周年）成为"全球奢华品牌"（刻意不说珠宝）；支柱：标志性系列、高级珠宝、国际开店／new market entry、线上线下 omni-channel（已开日本线上，下一步看美国）、提升加盟商经营能力（网格重组）
- [stated] 因此外招了多位有 MNC 背景的同事，要求财务学会支持规模化跨国公司
- [stated] 员工调研回应：推出弹性上下班（8:30–10:00）、加班空调、香港办公室装修；连续三个季度办 Forum 用于 recognition；新世界大厦 33 楼装修后财务有专区
- [stated] 会上表扬 [[ivy]] 带 FP&A 搭出未来三年目标，并深化出 FY28 财务目标已下发各部门、作为各部门 commercial plan 的依据
````

### /people/keith.md

- 原始路径：`/people/keith.md`
- updated (UTC)：2026-10-22T21:51:29Z

````markdown
---
name: keith
description: Keith (曹基荣) — Financial Systems senior manager in Hong Kong, SAP side
sources: [cowork]
aliases: [Keith, 曹基荣]
---

- [stated] Keith（曹基荣），香港，Financial Systems Senior Manager（9/14 介绍）；SAP 经验丰富，负责海外 SAP S/4 及 SAP／银行接口等
- [stated] 9/14 提到用户可以结合以往的 SAP 实施经验支持他
````

### /people/li-xinhong.md

- 原始路径：`/people/li-xinhong.md`
- updated (UTC)：2026-10-22T21:51:18Z

````markdown
---
name: li-xinhong
description: 黎新洪 — ICC project manager on AI Sales Forecast
sources: [cowork]
aliases: [黎新洪, Li Xinhong, 新红, ICC PM]
---

- [stated] 黎新洪，AI Sales Forecast 的 ICC 项目 PM（日常推进、项目计划、ICC 资源、供应商与风险管理），依据 9/29 项目架构；早期摘要误作"新红"，英文名未核实
````

### /people/patrick.md

- 原始路径：`/people/patrick.md`
- updated (UTC)：2026-10-22T21:51:32Z

````markdown
---
name: patrick
description: Patrick — head of ICC (IT); senior stakeholder alongside Karen
sources: [cowork]
aliases: [Patrick, PC]
---

- [stated] Patrick（PC），ICC（IT）最高主管；与 [[karen]] 同为 AI SF 高层
- [stated] Planning Tool Phase 1 成果和新增范围费用，要提前向 Patrick 和 Karen 说明
````

### /people/rita.md

- 原始路径：`/people/rita.md`
- updated (UTC)：2026-10-22T21:51:37Z

````markdown
---
name: rita
description: Rita (张晶) — provides finance parameters and data for DSC
sources: [cowork]
aliases: [Rita, 张晶, 瑞塔]
---

- [stated] Rita（张晶），由 Anita 指定参与 DSC，提供积分率、折扣率、批发率、成本率等财务参数和牌面价换算
- [stated] 首版数据已交 o9（10/19 由 o9 代导入）；10/22 她反馈财务目标上传部分成功、失败行没进 bad records（已提 ADO）
````

### /people/shen-na.md

- 原始路径：`/people/shen-na.md`
- updated (UTC)：2026-10-22T21:51:41Z

````markdown
---
name: shen-na
description: 沈娜 — mainland targets contact in DSC finance UAT
sources: [cowork]
aliases: [沈娜, Shen Na]
---

- [stated] 沈娜，DSC 财务 UAT 中对接内地年度目标（职责不扩大到全部市场）；10/22 参与实际成本回测的对齐
````

### /people/sun-fangyu.md

- 原始路径：`/people/sun-fangyu.md`
- updated (UTC)：2026-10-22T21:51:20Z

````markdown
---
name: sun-fangyu
description: 孙方雨 (Sun Fangyu) — DSC project PM; the user's contact for DSC UAT scenarios and acceptance criteria
sources: [cowork]
aliases: [孙方雨, Sun Fangyu, 方宇]
---

- [stated] 孙方雨（Sun Fangyu），DSC 项目 PM，是 UAT 场景和验收标准的对接人；会议转写里的"方宇"就是孙方雨（用户更正）
- [stated] 10/22 起用户要联系孙方雨，推动项目组、ICC、业务统一 DSC UAT 验收标准
````

### /people/vivian.md

- 原始路径：`/people/vivian.md`
- updated (UTC)：2026-10-22T21:49:27Z

````markdown
---
name: vivian
description: Vivian — user's direct boss at Chow Tai Fook; reports up to Ivy (VP)
sources: [chat]
aliases: [Vivian, boss, 老板]
---

- [stated] user's direct boss at Chow Tai Fook; [[ivy]] (VP) ranks above her
- [stated] 全名 Vivian Lau Man Ming（劉敏明），常驻香港；9/14 入职纪要记载职位为 Associate Director, Financial Systems and FP&A
- [stated] Planning Tool 的 PM；AI SF 的 Finance 侧 PM（与 ICC 共同负责）
- [stated] 开会习惯用粤语和英文
- [stated] 与用户每周 1:1（10/21 决定保持每周）；用户每周五给她发进展邮件和周报
````

### /people/weng-jieyi.md

- 原始路径：`/people/weng-jieyi.md`
- updated (UTC)：2026-10-22T21:51:44Z

````markdown
---
name: weng-jieyi
description: 翁洁仪 — data-governance contact working with Elsie
sources: [cowork]
aliases: [翁洁仪]
---

- [stated] 翁洁仪，与 Elsie 对接数据治理，负责把标准资料分发给财务各科室评审（10/10 财务指标命名与口径会）
````

### /people/yetta.md

- 原始路径：`/people/yetta.md`
- updated (UTC)：2026-11-05T07:39:16Z

````markdown
---
name: yetta
description: Yetta Chiu — HQ colleague tied to the strategic-plan model and the Planning Tool naming review
sources: [cowork, chat]
aliases: [Yetta, Yetta Chiu, 趙紫恩, 椰塔]
---

- [stated] Yetta Chiu Tsz Yan（趙紫恩），现行三年战略规划 Excel 模型相关的业务同事；Planning Tool UAT 的 HQ 代表（10/21 草案）
- [stated] 10/21 起与 Dennis、用户逐页核对 Dashboard 的命名和排序；10/22 Vivian 说命名规则已和她们谈过，不用再找
- [stated] 2026-11-05 向 FY28 预算收件组发出 RMB 汇率更新（0.8516）和经 Karen 确认的金价指引，见 [[fy28-budget]]
````

### /people/yuan-feng.md

- 原始路径：`/people/yuan-feng.md`
- updated (UTC)：2026-10-22T21:51:38Z

````markdown
---
name: yuan-feng
description: 黄元凤 — DSC finished-goods OTB chain and raw-material mapping
sources: [cowork]
aliases: [黄元凤, 袁凤, 元凤, Yuan Feng]
---

- [stated] 黄元凤（转写常作"袁凤"，英文 Yuan Feng），在 DSC 核验成品 OTB 链路，负责重发原料 Mapping
- [stated] 10/22 起，o9 要先和她及沈娜对齐实际成本与牌面价折算的历史回测
````

### /people/zoe.md

- 原始路径：`/people/zoe.md`
- updated (UTC)：2026-10-22T21:51:42Z

````markdown
---
name: zoe
description: Zoe — Hong Kong supervisor reviewing HK/overseas targets; Planning Tool UAT HK representative
sources: [cowork]
aliases: [Zoe, 張鈞婷]
---

- [stated] Zoe，香港主管；DSC 财务 UAT 中复核港澳及海外年度目标；Planning Tool UAT 的香港代表（10/21 草案）；PT 20 万价位段事项要与她对齐
- [stated] 中文名在导出的旧记忆里写作張鈞婷，原件未核实
````

---

## Part B · 项目：01 AI Sales Forecast

- 记忆文件夹：`/projects/01a1470f-ff85-76a8-9052-2edd4b94a69e/`

### 01 AI Sales Forecast · preferences.md

- 原始路径：`/projects/01a1470f-ff85-76a8-9052-2edd4b94a69e/preferences.md`
- updated (UTC)：2026-11-03T11:45:14Z

````markdown
---
name: preferences
description: How the user wants Claude to work on AI SF deliverables — review standard, translation format, versioning and edit rules (from the 2026-10-28 memory export)
sources: [cowork]
---

- [stated] 蓝图类工作严格以最新 SOW 为依据，MECE、第一性原理，不重不漏；同一规则不要拆成重复事项
- [stated] 既关注关键细节，也关注老板关注的重点；语言简练、层次清楚，不啰嗦
- [stated] 全面复核时用多个独立审查再交叉裁定；只有发现实质问题才修订，不为重复复核生成没有变化的新版本
- [stated] 翻译用"每段中文在上、对应英文在下"的对照格式；保留原文逻辑、条件、数字、责任主体、编号和出处；不增删义务、不补造阈值、不扩张范围、不猜测缺失主体；英语平实，不用 de facto 这类词
- [stated] 区分既定要求、支持能力、当前建议、原文示例和蓝图待确认事项；严格区分"天"和"工作日"；原文没解决的歧义保留，不在翻译里擅自修正
- [stated] 用户删改过的内容（如删掉的列、说明、备选方案）在后续版本和翻译中不恢复；后续在最新交付上增量修改，保持结构
- [stated] 通常先出中文审阅，再出英文；给管理层的内容简洁，学习用的解释与管理层材料分开
- [stated] 样式参考只用于版式，不当业务内容依据
- [stated] AI SF 用户需求调研阶段：凡识别到 SBUX（星巴克）项目的设计、逻辑、方案对当前用户需求有帮助，要主动指出
- [stated] 更新记忆时各项目（AI SF、Planning Tool、DSC、Project Connections）要互通有无，跨项目影响一并记
- [stated] 所有交付物都必须可下载：做成 Claude Docs 等在线文档时，同时生成 Word（.docx）文件直接发给用户
````

### 01 AI Sales Forecast · profile.md

- 原始路径：`/projects/01a1470f-ff85-76a8-9052-2edd4b94a69e/profile.md`
- updated (UTC)：2026-10-28T12:27:30Z

````markdown
---
name: profile
description: Who the user is — works at Chow Tai Fook (周大福), reports to Vivian; key colleagues Ivy, Karen, Anita, Elsie (project copy)
sources: [chat, cowork]
aliases: [me, user]
---

- [stated] works at Chow Tai Fook (周大福); direct boss is [[vivian]]; joined 2026-09-14
- [stated] key colleagues: [[ivy]] (VP, senior to Vivian), [[karen]] (CFO), [[anita]] (key user of AI SF), [[elsie]]
- [stated] name: Sampson Sun（孙洋，Sun Yang；会议转写里常被识别为 Samson）
- [stated] title: Finance System Manager（Financial Systems 团队）
- [stated] city: 上海
- [stated] timezone: Asia/Shanghai
- [stated] working_language: 日常用中文；给管理层的正式材料多用英文
````

### 01 AI Sales Forecast · areas/ai-sales-forecast.md

- 原始路径：`/projects/01a1470f-ff85-76a8-9052-2edd4b94a69e/areas/ai-sales-forecast.md`
- updated (UTC)：2026-11-09T14:55:49Z

````markdown
---
name: ai-sales-forecast
description: AI Sales Forecast (AI SF) — governance, SOW/contract, kick-off, scope, acceptance, requirements tracker, blueprint list, 11/3 discovery meeting 1 (Ivy's 5 scenarios, Anita's budget process)
sources: [cowork]
aliases: [AI SF, AISF, AI Sales Forecast, 销售预测项目, 销售预测, 01 AI Sales Forecasting]
---

本文件合并了账号级 ai-sales-forecast 与用户 2026-10-28 要求吸收的《AI Sales Forecasting Memory Export 20261028》（ChatGPT 项目导出，含 Vault/Linear/需求表原文与审计）。导出里"已完成/已确认"的历史说法不等于当前事实，下面按日期保留。

## 定位与治理
- [stated] 目标：做出可解释、可调整、可追溯的销售预测，承接财务调整和门店指标分配（RMIP），衔接 [[planning-tool]]、[[dsc-o9]]、数据湖、Power BI（数据湖与 Power BI 是两件事，不能写成"数据湖（Power BI）"）
- [stated] 供应商上海意臣信息科技有限公司（Yichen），英文注册名未核；系统建在 CTF 现有 o9 平台，环境由 CTF 提供；o9 合同另签
- [stated] 用户 2026-09-14 入职；在 AI SF 中代表 Finance，连接 FP&A、ICC、供应商；不是三系统集成总负责人，Vivian 不希望用户接 ICC 纪要或总集成
- [stated] 治理：ICC 与 Finance 双 PM；[[ivy]] 是项目负责人（业务目标、范围、阶段成果、SOW sign-off）；Finance PM [[vivian]]；ICC PM [[li-xinhong]]；ICC 侧项目总监胡志军／任波；高层 [[karen]]、[[patrick]]；关键用户 [[anita]]（Anita Lu Ying Jun／陆颖君）的 FP&A 团队
- [stated] Co-Lead R&R 草案（2026-09-29 draft，非正式任命）：ICC PM 对技术交付负责（架构、数据集成、技术架构、AI 方案、供应商管理／安全合规、SIT／性能／安全测试、上线基础设施、预算跟踪、项目治理）；Finance PM 对业务结果负责（用户需求收集、预测流程设计、数据验证——哪个销售数是官方口径、退货处理等、协调 FP&A／ICC／供应商、UAT 与准确率验收、预算与销售预测的变更管理、最终用户培训、上线准备、收益跟踪）；双方共担：蓝图确认、里程碑签收、Steering Committee 汇报、准确率 KPI、Hypercare
- [stated] 历史优先级 AI SF 第一；10/13 说未来 4–6 周重心在 PT，只是阶段安排

## 合同、kick-off 与时间线
- [stated] 2026-10-08 版 SOW 是合同审阅基线；意臣 10/8 对 clean 版重新 sign off；10/12 用户把 clean、cross-check、英文逐段对照、蓝图细化清单四件套发给 Vivian 抄送 Ivy
- [stated] 1008 sign-off 版（10/14 上传）与 1008 clean 版正文唯一差异：§3.5.1"数据湖（Power BI）"改为"数据湖、Power BI"（clean 版只改了 §2）；文件名带 sign-off 不等于签署或用印；clean 版仍带修订痕迹
- [stated] 10/13：ICC 确认总人天不减少，询问工时这一步已完成
- [stated] 2026-10-21 Vivian 邮件称与意臣的合同已 signed off（她的状态报告，未见双方用印正本）
- [stated] Kick-off：ICC [[li-xinhong]] 于 2026-10-22 发出会议邀请，2026-10-29（周四）10:00–10:30 香港／中国时间，Finance／ICC／意臣；Karen 接受、Patrick 同意，可能作开场 5–10 分钟致辞；用户负责收集名单和邮件地址并起草，交 Vivian 或新洪发出，并与新洪对接意臣（10/16 周报曾写 11 月 kick-off，已被此邀请取代）
- [stated] 三供应商对接会：10/23 Timeline 写拟于 12 月举行，日期待定（早先说 10 月、11 月）
- [stated] 供应商预计 2026-11-02 开始用户需求调研
- [stated] 工期都是估计：历史约 10–11 个月；ICC 9/29 说 9–10 个月、2027-07 上线；10/13 估 UAT 2027 年 5–6 月；旧 Timeline 的 2027 年 6–8 月上线窗须重新核定；SOW 约定签署后 140 个工作日内部署试运行
- [stated] 阶段：启动 → 蓝图 → 开发 → 试运行（≥3 个月）→ 上线 → 陪跑 3 个月 → 质保 12 个月；试运行、陪跑、质保都考核准确率
- [stated] 0908 版合同付款 5 期：启动 20%、蓝图签收 20%、试运行验收 30%、陪跑验收 15%、质保期满 15%，后 60% 挂在验收上；港币结算＋内地增值税专票；金额和账户只留在 Vault，不外带
- [stated] 0908 合同待统一项（历史）：税率 6% vs 13%、两套里程碑术语（初验／移交／试运行／终验 vs 启动／蓝图／试运行验收／陪跑验收／质保）、启动日期等空白；签约主体待核（SOW 写深圳，ICC 9/29 说香港）
- [stated] 商务前置：10/8 提案 Novus 额外调研参与经 AI SF 与 PT 等额预算调拨、香港侧采购（仅提案）；10/26 会议要 Vivian 向 Lydia 核实 Andy 11 月 T&M 支持需要补合同、PO 还是别的手续

## Kick-off 材料（AI_Sales_Forecast_Kick_Off_v2.4，10/29 会议用，用户 10/28 提供）
- [stated] 17 页：Welcome、Sponsor 致辞、目标与范围、项目成果、High-level Timeline、Team Structure、Governance、Next Steps、Q&A；标题 CTF × Yichen，29 OCT 2026
- [stated] 时间轴（按图读出）：合同签署 ✓、Kick-off 10/29；调研与蓝图 2026-11 至 2027-02 初（M2 蓝图签署约 2 月、春节附近）；开发测试 2027-01 至 05；试运行／UAT 3 个月约 2027-05 中至 08 中（M3 部署约 5 月中）；M4 验收／上线约 2027-08 中；陪跑 3 个月至约 11 月中（M5 陪跑验收）；质保延至 2028；关联依赖 DSC、Planning Tool、Datalake/PowerBI
- [stated] 近期计划：用户需求调研 10/26–11/13——10/27–28 意臣发出用户需求清单；10/30 Anita、Rita 反馈清单修改意见；11/2–6 第 1 轮线上访谈（每天 1–2 小时，Rita、Anita），11/6 第 1 轮总结；11/9 意臣向 Anita 提交第 1 轮报告；11/9–13 第 2 轮线下访谈；11/13 总结报告提交 Ivy／Vivian／Anita；11/16–20 暂无安排；11/23–27 视需要补线上 Q&A；11/27 更新版总结报告
- [stated] 前三个月：第 1 月摸清现状、完成蓝图框架（环境与治理、数据源与接口盘点；里程碑：业务需求清单、蓝图框架）；第 2 月蓝图与方案细化（量价、归因、仿真、版本、RMIP；数据模型／字典、接口契约；权限与审计）；第 3 月验证准备与基线确认（样例数据口径校验与初步回测、关键接口可行性；确认验收指标、建设优先级与实施计划）
- [stated] 会议机制：项目日会（意臣，按需）；项目周例会初定每周五 11:00–11:30 远程，输出《项目周报》；项目评审会、里程碑会议按阶段触发；临时会按需。升级：L1 日常问题当天闭环；L2 进度／跨组分歧双方 PM 24 小时内介入；L3 重大变更／风险由双方 Sponsor 裁决
- [stated] 组织架构（CTF）：项目负责人 Ivy；财务项目 PM Vivian；ICC 项目 PM 黎新洪；项目总监胡志军／任波；项目实施小组王子欣团队（架构、接口、集成、环境、上线）；财务小组 Sampson（需求、预测口径及业务规则确认；蓝图评审、UAT 及业务验收；因子数据管理、准确率监控复盘）；算法小组覃茜／孙永琨；Steering Committee Patrick、Karen
- [stated] 组织架构（意臣）：项目负责人王竞；项目 PM 赵秋红；财务顾问／业务分析戴婷、王敬超；算法专家倪晟宇、胡子欣；数据架构师周涛；数据工程师钱家晨；实施小组朱先坤、张敬轩、赵世杰等；Steering Committee 张辉
- [stated] 范围页：地理层级 全国→大区→省→城市等级→城市→门店；产品 业务大类／小类／子品牌／系列；渠道 直营／批发／寄售，同店／新店／次新店／关店；输出 RSV、QTY、ASP、Discount，衍生 REV、RSP、SSSG；Drivers 列了客流
- [stated] 口径冲突待改：kick-off 第 8 页写 ASP = RSP × (1 − Discount%)，与 1008 SOW 的 ASP = RSP − Discount（金额）不一致
- [stated] 主要交付物：业务蓝图、算法设计、PRD、测试与验收报告、用户手册、算法文档、源代码、数据字典

## 用户需求调研计划（10/30 对齐，取代 kick-off 页上 10/26–11/13 两轮访谈的安排）
- [stated] Vivian 2026-10-29 明确要求：三供应商集成对接会召开并对齐之前，不得签收（sign off）AI SF 用户需求；这一条本身也要写进用户需求
- [stated] 2026-10-30 用户发起会议"AI Sales Forecast – Alignment on User Requirements Gathering Plan"，当天 13:30–14:00，15 楼传喜会议室＋Teams（因冲突改期）；目的：让关键用户了解调研时间线并做好准备；用户要求意臣对每场会说明目标与议题（每场 1–2 小时）、需要的参会方（Finance／ICC／联合）、预期产出
- [stated] 收件：Vivian、黎新洪、孙永琨、覃茜、赵秋红、戴婷、倪晟宇、Rita；抄送 Anita、王子欣、Ivy
- [stated] 意臣 10/30 回复两版计划（约 2 个月 8 周）：戴婷 12:08 英文版写 11/2 开始，W1 数据收集、W2 现状流程；赵秋红随后发给 Ivy 的版本写 11/3 开始，W1、W2 顺序对调，并请 Ivy 补充议题、指出需要亲自参加哪几场，确认后预约她的日历
- [stated] 赵秋红版各周：W1 流程场景（现行手工计划步骤、跨部门协作、审批节点、版本流转 → As-Is 流程图、部门职责矩阵）；W2 手工业务数据收集与导入（手工数据文件清单、字段、来源、频率、负责人 → 手工业务数据清单、数据缺口清单）；W3–W4 Trendline 与版本控制、What-if 仿真（Trendline 生成逻辑含指标／Drivers／区域、重跑机制、版本类型与正式版定义 → Trendline 规则、版本控制规则、What-if 场景设计）；W5 集成与推送（推送 Trendline 到 Planning Tool 的维度、频率、内容，戴婷版还含回流需求 → 集成推送需求说明）；W6 门店／Dummy Store／Adjustment（门店生命周期、新店、翻新、转营、Adjustment 定义与层级 → 新店／翻新／转营预测规则、Adjustment 规则）；W6 RMIP 分配到门店（拆分权重、门店二次调整、直营／寄售／新店／翻新店差异 → RMIP 分配规则、门店分配原型）；W7 SSSG 专题（计算规则，含直营转寄售对 SSSG 的影响 → SSSG 逻辑说明）；W8 汇总（待决事项、流程闭环确认、下一阶段蓝图输入 → 需求调研报告、待决事项清单）
- [stated] W1 流程讨论聚焦：从预算／预测到审批和版本锁定的流程生命周期；各步骤的做法与原因；全部手工文件和数据源；跨部门数据流（销售、财务等）；各阶段发起人和审批人
- [stated] 意臣邮件署名：王静 Jing Wang（kick-off 组织架构页写作"王竞"，以邮件为准待核）、王敬超 Porter Wang、张辉 Reed Zhang、戴婷 Ting Dai、倪晟宇 Shengyu Ni、赵秋红 Qiuhong Zhao，另有 Tom Young；CTF 侧 Ivy 即 Ivy Cheng 鄭凱因，Vivian 即 Vivian Lau 劉敏明

## 准确率 KPI 维度讨论（2026-11-09 周一 13:30–14:00，"Quick Discussion for AI SF Accuracy"）
- [stated] 用户 11/6 发起，Teams＋15 楼传喜会议室；参会 Rita、ICC 孙永琨（Kimberly，算法小组）、黎新洪，抄送覃茜；录音约 13:38–14:15，智能纪要标题"销售预测KPI维度规划会议"；本次只谈了产品 mix，比例数字先不定，先定框架，最后由老板定百分比
- [stated] 底稿是孙永琨的《准确率及验收标准.xlsx》（会后发出，三张表）：①绝对准确率（全品类）：每个 forecast point 算未来第 1/2/3 月（取三个月月均）和未来 4–16 月加总，取过去 12 个 FP 的 25 分位数须达标，即 75% 的 FP×维度点达标；②品类 mix 偏差 = |预测占比 − 实际占比|（各业务大类／小类占总品类），取过去 12 个 FP 的 75 分位数须 ≤ 门槛（例：12 个点里第 9、10 个之间）；③KPI 矩阵
- [stated] KPI 矩阵时间维度：未来第 1–4 周每周、5–8 周每周、9–12 周每周、未来 3 个月月均、未来 1–13 周加总、未来 4–16 月加总；预测指标 QTY／RSV／ASP
- [stated] 绝对准确率草案：全国、子品牌、四大区＋钟表、（四大区＋钟表）×店属性（自营／批发／寄售）、再×店龄（同店）均 92%；门店 85%（4–16 月加总 82%）
- [stated] mix 偏差草案（全部暂填 3%）：5 个业务大类每类、5 个业务小类每类、大价位（10 万以上）、重点系列每系列，各按全国／四大区＋钟表／四大区×店属性／门店；底部另列 discount?、consistency 待定
- [stated] 表内产品清单：业务大类 黄金类、定价金类、镶嵌类、钟表类、西铂金类；业务小类 一般足金類、定價黃金類、工艺金章金条（IF）、黄金镶嵌、其他业务小类加总；重点系列（top8？）传承、传喜、传福、故宫、生肖、锁愿、万相、ING
- [stated] 表内时间窗：回测期（数据开始至 2026-02）→ 盲测期 12 个月（2026-03 起，"应考虑一期已知的近期变化"）→ 验证期（标"2027.03 上线"）→ 质保期一年 → 运维期（与质保期标准和流程一致）；"2027.03 上线"与 kick-off 时间轴的 2027-08 上线不一致，待核
- [stated] 会上 Rita 的意见：业务大类可以；业务小类用前四个（F、R、IF、RU）＋"其他小类加总"兜底（用户提议）；店属性要作为与地理并列的独立维度，并下钻一层到"区 × 店属性"（如东区自营），因为直营和加盟的货类结构差异大、四区也看自己的 mix；维度越细门槛可放宽（如全国 3%、细维度 5%）
- [stated] 会上 Rita 的意见（续）：含钟表、不含电商；钟表没有货类区分；子品牌（如 MONOLOGUE）已归入所在大区，不需单独看 mix；10 万以上大价位要加为产品维度——FP&A 最近的预测已单独拆出 10 万以上，从 RSV 估到 REV、NGP，维度与常规滚测相同，其货类结构（宝石、玉类占比高）与全盘很不同，可能不到门店；TF 金额小，小类不单列
- [stated] Rita 常看"定价珠宝"占 RSV 比：除黄金（F、IF、TF）和钟表以外的所有货类；会上认为业务大类已能体现，不另设
- [stated] 同店：要加同店销售准确率，看总数（如东区自营同店），不看每家同店；KPI 表分两行（含／不含同店）；店龄只看同店，不看次新店、新店；用户认为同店门槛应较高（至少 85%，略低于 92%），按总数还是按门店统计 TBD
- [stated] 直营门店销售占比（约 40%，随直营店增多可能到 43–44%）由店属性维度的绝对准确率覆盖
- [stated] Rita 会后去确认门店背 KPI 是否也按这四个业务大类，以便统一；会后表格发 Rita 交叉复核，看老板关心的角度有没有遗漏
- [stated] Discount：Ivy 似乎要求意臣先预测折扣率／金额再算 RSV；Rita 认为主要看结果，折扣率作参考；用户说以前公司从不直接预测 discount，都是倒算；结论：财务先准备一版，内部再找 Ivy 确认
- [stated] 回测验证难题：Ivy 之前说用回测验证（把所有 what-if 换成真实情况后看模型能否预测准），但实际数含举措／judgement；举措算在 trendline 还是 PT 未定；若剥离要先从实际数里剥出举措，规则难定；孙永琨建议把举措转成真实数字给模型训练；用户倾向让模型学而不是人工剔除；留待周三大讨论
- [stated] 下次会 2026-11-11（周三）：Rita 交叉复核维度；时间维度是否都要考核；回测中 management initiatives／judgement 怎么处理；Discount。孙永琨邮件另加两题：子品牌（SOW 要求供应商做到该维度，是否在总数设 KPI）、重点系列（是否选 top 系列设 KPI）

## 意臣第 1 周需求调研总结（赵秋红 2026-11-09 16:57 发 Anita，抄送 Ivy、Vivian、Rita、Michelle Tam、胡志军、任波、黎新洪、Sampson 等；附中文版《业务调研周总结》）
- [stated] 覆盖 11/3–11/6 三场共约 4.5 小时：11/3 调研框架介绍；11/5 年度预算流程与数据；11/6 季度／月度预测流程、手工调整、trendline 版本管理
- [stated] 写下的共识：四个场景（年度预算 ≥16 个月跨日历年、季度／月度滚测、未来 13 周、金价敏感性），电商不在范围，线下珠宝与钟表流程相同；端到端流程 trendline → Power BI 分析 → PT 录入调整 → 回流 AI 生成目标 → 目标自动进 Power BI（取代逐店手工上传）→ 同步 DSC 支持自动补货；三系统维度与时间对齐是主要集成风险
- [stated] 历史事件标签缺失（翻新、台风、闭店原因无系统标签，靠部门手工台账）；替代方案：AI 先聚类识别异常场景，财务再匹配确认，从"标注全量"降为"审核分类"
- [stated] 拟可冻结的口径：RSV→REV 转换、同店与次新店标准、货类 × 店属性 × 店龄三维拆分；定义草案：同店 = 上一财年之前开业且满一个完整财年，次新店 = 上一年开业（措辞待财务确认）；闭店影响 = 直接损失该店 RSV、约 60% 被周边门店吸收；Flex adjustment（平衡区域汇总与集团目标的调节项）和渠道平衡项（四大区以外，如特卖展）都要求 AI 预测保留人工干预点；批发门店净变动在预测 REV、NGP 时单独考虑；直营与寄售互转暂非重点
- [stated] 四层节奏（总结原文）：年度预算约 3 月完成、自上而下、拆门店；季度滚测 6+6 约在 Q3 前 1.5 个月（8 月初至中）、自下而上无预设总数、拆门店、约 1.5 个月；月度滚测 7+5 约每月 2 号有上月实际、4–5 天、不必拆门店；周滚测全部 TBC；年度预算与季度滚测总数可不同，不强制对平
- [stated] 版本链：V01 初稿 → Rita／Anita 内审版 → 集团提交版；审批：内审 → 深圳同事转集团模板加费用成完整 P&L → 集团（Kevin／Karen）审阅；月度 2 号取数、下周一前提交到毛利层、13 号左右集团 review；季度 5 月中开始、6 月底完成
- [stated] 需求 5 条：新店月均销售按相似商圈和城市等级学习；闭店客流吸收（区域估 40–50%）改为预测周边同店增长变化；预算自动分配；货类 mix 系统建议；trendline 输出 Power BI 并做金价敏感性（如 3,900）
- [stated] 预测层级未决：高层预测后往下分配 vs 多层预测再调和，会上倾向前者，按回测定、需定评估日期；颗粒度到业务大类／小类→子品牌→重点系列，不到 SKU
- [stated] 数据缺口与责任：历史销售 3–5 年、优先疫情后（ICC 提供数据湖样例）；手工 Excel 全套含脱敏实际（Anita／Rita）；翻新记录是工程部手工台账，大小翻新非正式分类、财务 BP 数据缺开工日期（Rita 向工程部确认字段和年份）；开关店翻新计划由门店 BP 按月提供，翻新审批状态是否入系统待问（Rita）；月度金价预测表未提供；集团年度目标邮件样例（财务）；折扣与活动日历未提供，需开 discount 专题会（Rita）；KPI 清单口径不齐（Anita 出维度与 KPI 定义文档）；driver 清单 POC 时识别、CTF 未逐项填（Anita／Rita 填，意臣已出初稿）
- [stated] 建模假设：珠宝周转慢、多数款式只有 1 件库存、缺货靠调拨，初期模型库存因子权重可低；货品不跨大类、不跨系列转移，限制 mix 模型解空间
- [stated] 待决：预测层级方法；财年与日历年对齐（尤其 3 月 31 日处理，Rita 核）；版本命名（V01／内审版／集团提交版）；风险：三系统维度时间不一致、手工台账年份与销售历史不匹配、历史事件标签缺失
- [stated] 下周行动：财务（Rita、Anita）下周二中午前把手工表清单、KPI 定义、关键假设上传共享文件夹；周五下午前完成月度滚测差异与 What-if 访谈；Rita 提供年度预算与季度滚测全套脱敏工作簿和预算时间表、核翻新台账年份、问门店 BP；ICC 提供样例数据；意臣与 Rita 核财年规则、整理翻新规则与分类、提出各场景版本命名
- [stated] 两周输出物：维度与 KPI 定义草案（已有初稿）、假设／driver 汇总清单（待业务填）、需求跟踪表（已启动）、As-Is 流程图（初稿）、To-Be 流程图（初稿，未决步骤用虚线）、数据清单与数据字典草案（未开始）、核心口径基线签认（未启动）、待决与风险登记（初稿）
- [stated] 与此前记录不一致、待核：总结写年度预算"约 3 月完成"，而 11/3 Anita 说 1 月经 CEO 和集团通过、3 月底是拆下一财年 Q1 门店目标；季度滚测一处写 8 月、另一处写 5 月中至 6 月底；闭店吸收率一处 40–50%、另一处约 60%；周滚测写 TBC，但 Ivy 11/3 已定每周日／一自动跑 13 周 Outlook；"待决 4 项"实际列了 3 项（编号从 6 开始）
- [stated] Ivy 同日回复：要列出全部 drivers 并分三类——①系统自动填（节假日、春节、中国情人节等）；②人工收集但须以数字化方式进 AI SF、不能由 FP&A 用 Excel 上传（开店、闭店、翻新）；③假设（金价）；这些输入与历史实际一起生成 trendline；她 11/11（周三）10:00 参加一小时，要求留时间讨论，若第 2 周没覆盖此题请告知

## 范围与口径（1008 SOW）
- [stated] 范围：中国大陆线下门店，含钟表，不含电商；首阶段只做内地，PT／o9 覆盖内地、港澳、国际，其他市场的门店目标来源未定
- [stated] 预测约 18 个月／78 周，周／月颗粒度（20 月／80 周只是示例）；输出 RSV、QTY、ASP、Discount；RSV = QTY × ASP，汇总 ASP = 汇总 RSV ÷ 汇总 QTY，数量取整、月转日、财历和 PT 对平规则待定义
- [stated] 1008 文本 ASP = RSP − Discount（折扣金额），取代旧"RSP × 折扣率"
- [stated] 预测 = Baseline + Drivers；Driver 示例算法属"当前建议，以蓝图调研为准"；Adjustment 承接 PT／DSC 调整；只改 RSV 时 QTY／ASP 怎么联动需甲方确认
- [stated] Drivers 概览含开关店、翻新、促销、新品、金价、调价、库存约束、节假日、竞品门店；会员因子 Nice-to-have
- [stated] 库存和组货不直接改 Baseline，只在第二阶段（拆门店）作约束，但意臣本期仍须接入这些输入
- [stated] 1008 SOW 规划流程：PT 调整回流 AI → AI 调整后的门店预测推送 DSC → DSC 按组货计划调整后回流 AI；这是目标流程，不证明接口已实现
- [stated] CR 只限两种情形：现有维度树以外的新维度体系／层级；蓝图未定义的新功能模块或前端页面；正常经营变化导致的调优属于质保
- [stated] 系统支持过去 10 年回测；ICC 能提供 10 年数据，数据取舍由意臣决定（Vivian 担心旧数据成噪声）
- [stated] System／Adjusted／Consensus 版本分开保存；正式预测须 FP&A／管理层确认后才推下游
- [stated] SOW 残留歧义：回测起点正文 2017/1、图内 2017/8；流程图"每月 12 round"未定义；"即 MAPE"表述；算力优化责任句缺主体——保留原文，不擅改

## 验收与准确率
- [stated] 准确率 = 1 − |预测 − 实际| ÷ 实际（实际为 0、预测不为 0 记 0；双方都为 0 未定）；底线全国全货类 ≥92%、门店全货类 ≥85%，取前三个月单月准确率的算术平均
- [stated] "12"指最近 12 个 forecast origins（每次滚动运行一个），不是 4 周 × 3 情景；这些预测值中至少 75% 达标；SOW 示例 12 × 6,000 = 72,000 个值、≥54,000 达标——是考核值数量，不是门店数，也不是每店 12 点里至少 9 点；75% 不等于准确率 75% 或 MAPE
- [stated] 重大例外须证明全国 >10% 可直接归因影响并经双方书面确认；10% 只是启动评估的门槛；金价不适用
- [stated] 单版本运行 ≤3.5 小时，前提是数据按时完整、算力达到蓝图配置；SOW §6.5 的 5 个工作日逾期确认只适用于变更发布

## Vivian 对 SOW 的 7 条意见（10/7 邮件，0929 → 1008）
- [stated] 已改 3 条：§2 数据湖与 Power BI 分列；§3.5.1 Drivers 概览补节假日、竞品门店；§3.5.1 增加"本系统调整后的门店预测推送至 DSC"
- [stated] 未改 4 条：Pt/K（两版都已有斜线，Vivian 说 AI SF 就用 Pt/K）；10 年历史（条款是回测能力）；两类 CR 条件；流程图 12 round（用户邮件已解释为 12 origins，但图未补定义）
- [stated] 比较表 Vivian_Comments_SOW_0929_vs_1008.xlsx 保存了用户的原邮件回复

## 用户需求收集清单
- [stated] AI_Sales_Forecast_User_Requirements_Tracker.xlsx：中英两个工作表；一项需求一个编号（SF001 起），来源写在说明里；"已确认"指业务确认，不代表已交付；2026-10-27 从 0 条开始，不从 SOW 或旧需求预填（如 9/21 的开店到"日"需求不自动回填）
- [stated] 用户要每天下午 5 点后根据投喂的资料、会议记录和文件更新该清单（格式仿 Elsie 跟进清单）
- [stated] SF001 按价格带分析销售额及销量（趋势与结构占比，支持库存规划）：来源 10/27 Planning Tool 会议纪要第 3 项，提出人 Ivy／Finance，优先级待定，状态待澄清；100k 只是示例分界；下一步由用户纳入需求调研，确认门槛、币种、价格口径与边界、历史分析还是预测、指标与分母、货类／地区／门店／时间粒度
- [stated] Elsie 跟进表第 4 项写的是"20 万以下"（10/21–22），与 SF001 的 10 万示例分开保留，不自动统一
- [stated] 根目录问题总表 S015"已解答"只是价带背景问题已解释，不能用来关闭 SF001

## 蓝图细化清单
- [stated] SOW1008_蓝图设计细化清单_中英对照.xlsx（10/12）：75 项蓝图事项（15 项明确蓝图＋3 项明确调研＋57 项总括条款下的方案细化）＋13 项其他确认（OT-01–OT-13）＋336 条原文索引；不要退回旧 154 项清单；原文基线 1008 clean(3)
- [stated] 三个工作表：蓝图确认清单、未限定蓝图的确认、SOW原文索引；主表七列（编号、领域、蓝图需细化事项、蓝图需确定的内容、既定要求及设计边界、主要依据类型、SOW章节及索引号）；用户删掉的 H 列"原文定位"和 A3–A5 说明不恢复；酒红、米白、浅金风格，管理层重点加粗＋浅金底
- [stated] 双语术语：甲方／乙方 Party A／Party B；蓝图 blueprint；调研 requirements discovery；试运行 trial operation；陪跑 post-trial support；质保 warranty；回测 backtesting；盲测 blind testing；归因 attribution；推演 simulation；组货计划 assortment plan；异常 anomaly（区别于重大例外 major exception）；严重／重要／一般缺陷 critical／major／general defects

## 现行滚测（10/14 访谈，FY27 6+6F 样本）
- [stated] 蓝图前的准备，不是蓝图启动；九份模型底稿已收，用户研究串流程后请业务反向确认
- [stated] 现行滚测 = 选定上一版 + 本轮变化（6+6 对 3+9，7+5 对 6+6），不是同比；上一版不等于 AI Baseline。大滚测（3+9／6+6／9+3）拆地区和门店目标入系统，小滚测主要给管理层参考；AOP 流程未完整了解
- [stated] 输入：四区举措／风险、开闭店和翻新、总部专题（活动、调价、会员、新品）；商业举措模板分 RSV／REV、直营／寄售／批发；没有统一"千万级"审批阈值
- [stated] Excel 模型：1.0 中间模型（RSV／QTY／ASP，未见单店 ID，店龄分新店／次新店／同店／闭店／其它）；2.0 级联三个入口 flow_fromRSV／flow_fromREV／flow_plugin（REV 入口把 RSV 清零防重复）；地区 review 接 1.0／2.0 供 3.0；4.0 可直接取 1.0——不是固定 1→2→3→4 串行
- [stated] 新店可能没有正式店号，临时 ID 与转营历史连续性要问 [[frank]]（咨询对象，不是 Owner）；闭店当月销售归闭店、之前月份保留
- [stated] 翻新增量逐店算（装修期影响、临时位、装修后增量），22% 不是统一增长率；新品"10 亿中 4 亿是增量"是个案，40% 不是蚕食率；节假日、季节性可能已在上一版结构里，不能无条件再叠加
- [stated] 金价对编制人员是判断 product mix 的参考，不是直接乘销售；常规货品不按现存库存设销售硬上限，紧俏系列可能受产能限制
- [stated] 地区模板按门店 × 货类 × 月填写，Check 按地区 × 经营性质 × StoreAge × 月 × 货类逐项对平；Calendar 要求最终门店 × 货类 × 日入系统
- [stated] 待核版本疑点：2.0 文件名 6+6F 但 config 是 FY27／5+7F／v01／P05；Calendar 写 9/24 入系统、西区模板写 9/28 前提交；东区 FY27 Q4 出现 2026-01／02；4.0 CN 是 RMB M、Total 是 HKD M 含港澳国际
- [stated] 条件性风险：一次性因素已在 AI 历史基线里时再加 Driver 会重复计算
- [stated] 调研优先项：增量／版本语义、系统范围与三类调整入口、门店主数据、月周日转换与分层对平、有效模型版本；建议用"活动重复申报""特殊门店"两个端到端样例验证
- [stated] 情景数量、假设和基线选择留待需求调研（10/21 Vivian 说"选中间情景"只是举例）
- [stated] 用户的 Driver 治理思路（非合同字段）：Must-have／Nice-to-have、用途、验证状态、适用范围、对应 SOW driver group

## 跨系统未决（10/21–10/22）
- [stated] o9 方认为只和 PT 集成、不和 AI SF 集成，这个认知有问题：AI SF 要把门店目标给 DSC
- [stated] PT 是 high level、不到店，总量以 PT 为准；门店目标从 AI 到 o9 在哪个层级、算 CR 还是 o9 Phase 2，之前没讨论过；AI SF 只有内地，港澳和国际的门店目标怎么来未定
- [stated] 10/21 Vivian 要求 DSC 沿用 AI 的分店拆分，避免从 PT 区域另拆
- [stated] 原料主数据的 OTB 管控层级：o9 说 ICS 数据不 ready、手工上传；另一方认为 ICS 有原始附件数据，可能是 mapping 问题——待查数据源和上传人
- [stated] 用户 10/22 定目标态：未来所有 DSC 顶层数据从 ICS 自动集成到 o9（删除旧 12.1 手工步骤）；这是目标，不是已上线
- [stated] 用户 10/09 删除了"受控 Excel＋自动集成"备选方案；1008 SOW 仍保留 PT Phase 1 adjustment 模板导入条款，两者分开，不用条款恢复已删方案

## 工作载体
- [stated] 项目材料、邮件、框架图放 Obsidian Vault（1 Projects/AI Sales Forecast，含项目档案八章和 Meetings、_Source 摘录）；行动和风险放 Linear 项目 AI Sales Forecast（P-SAM-1，team SAM）
- [stated] Linear 工作流 W1–W6：SAM-5 W1 合同与 SOW；SAM-14 W2 验收口径；SAM-9 W3 Finance 需求与蓝图准备；SAM-11 W4 数据与因子；SAM-18 W5 系统集成；SAM-22 W6 治理与角色（Done）；9/17 的细项多已标 Duplicate 归并

## 用户需求调研会 1（2026-11-03 周二 16:30–18:30，12 楼 1208＋线上；调研实际从这天开始）
- [stated] 参会（按邀请）：Ivy、Vivian（迟到）、Anita、Rita、Sampson；ICC 黎新洪、覃茜、孙永琨、王子欣；意臣赵秋红、戴婷（主持访谈）、王敬超、倪晟宇；抄送 Michelle Tam 譚銘恩
- [stated] 第一周（11/3–11/6，共 4 天）主题流程场景；意臣下周交流程图，Ivy 要以 To-Be 为主、As-Is 只简要了解；以年度预算（最长流程）为基础流程，其他场景按增减步骤描述；第一周按 Ivy 的 5 个场景拆，每个场景"现行做法 → 期望效果 → 与财务交流"；Ivy 只参加每周第一场做高层框架讨论，给她的邮件要用英文
- [stated] Ivy 的 5 个场景：年度预算（≥16 个月：财年 4/1 开始、11 月就跑；预算期 trendline 可能每天重跑，流程要留 lead time buffer）；季度预测（每年 3 次，流程同预算但跑得少）；月度滚测（每月跑 trendline）；每周日或周一自动跑 13 周 Outlook（与上一版比较，不做调整、不拆门店、不经 PT，但要城市／tier／货类／ASP／数量／SSSG 细节，Anita 团队是否要放假设待讨论）；What-if 敏感性（例：金价 4,100→4,000→3,900，看 F 类占比、ASP、数量；独立命名，不是 forecast 也不是 outlook，Ivy 可能直接让 Sampson 跑）
- [stated] Ivy 的预算／季度预测 To-Be 流程：历史＋假设 → AI SF 跑 trendline → Power BI 分析（门店 roll up 多维筛选）→ 选一版（如三个金价假设之一）→ PT 调整 → 回流 AI SF 拆门店 → 拆周（门店×周汇总必须等于 PT 月数，用星巴克式 Dummy Store 吸收尾差）→ Power BI 看细节并下载给区总 → 区总确认 → 一键把目标推到 Power BI 作 target（取代手工导入门店预算／滚测目标）→ DSC 按门店目标配货
- [stated] Ivy：两种上线先后都要设计，不能只有一套方案；绝不用 Excel 上传调整，必须数字化；AI SF 先于 PT Phase 2 上线（或系统宕机）时，PT 只回传最终总数，AI SF 与当前版本比差额再拆门店，并要有地方让财务录入分配假设（如活动或重点系列多放一线城市）；PT Phase 2 上线后 driver-based 调 ASP、Discount、Quantity、UPT 等，AI SF 学历史促销的门店响应来分配
- [stated] Ivy：PT、AI SF、DSC 三系统的维度、时间（周定义）、门店号必须一致；三家供应商清单比对、讨论往粗还是往细的利弊；会安排三供应商会议
- [stated] Ivy：要设计版本命名（预算 BUD、季度预测、滚测、预算多轮、每周、敏感性分开，FP&A 在 BI 里找得到）；先列完整假设清单（例 30 项）再按场景取舍，问每次导入的工作量值不值得；凡导入的假设历史都要打标（大翻新闭店约 8 周、之后约 15% uplift，小翻新约 2 周、1–2%；不让模型学闭店期的 0；台风等逐个 driver 定是导入还是只靠历史打标）；假设要同时影响 RSV、Discount、ASP、数量（DSC 要数量；ASP 关联 high jewelry，例单件 10 万以上，与 SF001 同类）；流程写清谁录入、谁看（支持多人同时录入；新店关店由 category 还是 regional finance 录待定）
- [stated] Anita 现行预算（As-Is，全在 Excel）：10–11 月集团下目标（守同比增长；Total China、钟表、电商、线下珠宝分开给，线下珠宝由营销＋中台拆四区）→ kick-off → 约 12 月各部门交关键假设（开关店和翻新以门店管理科为准，BD 已批新店含 12 个月 RSV；人货场举措按月填 RSV；中台全国营销日历和折扣；批发管理科取货；季度展销会；子品牌目标作手工附表；集团给季度末金价）→ 约两周按"积木"转成月×区×货类数字（只算比去年多出的增量、考虑蚕食，靠人判断）→ 两轮与区总／BU leader 讨论 → 集团 CFO → 1 月完成并经 CEO、集团（Sonia）通过 → 3 月底拆下一财年 Q1 门店目标（Q1 用预算、不滚测，之后 3+9）；自上而下方法约从去年开始，以前从 5,000–6,000 家店自下而上
- [stated] AI SF 与 PT 的假设边界未定：Anita 理解 AI SF 只跑基于历史的 trendline、举措都在 PT 里加；Ivy 的流程与 1008 SOW（Baseline + Drivers）要求部分假设进 AI SF
- [stated] 会上澄清：AI SF 预测 RSV（含 QTY、ASP），REV 衍生计算不预测（Sampson，Anita 认可）；调整在 PT 做、结果回流 AI SF 做目标分配；颗粒度到业务大类→小类→子品牌→重点系列、不到 SKU，所有系列都输出，方法（top down 或 hierarchical）按回测定（倪晟宇）；数量现按趋势平均 ASP 倒算，交集团合并，未给 DSC
- [stated] ICC：AI SF 与 DSC 在 o9 同一租户、同一套主数据；数据湖有销售、月／周库存、DSC 六七张表、客流、会员、交易笔数；意臣访问 CTF 环境的账号开通中，ICC 先抽部分现有数据；意臣调研后给出颗粒度和字段画像（如每日销售是否到牌仔级）再提交开发；倪晟宇接受先按周给数据
- [stated] 待核：翻新历史是否在系统里（问门店同事徐晴或 ICC）；意臣拿到的 8,000 家门店清单是否混入线上门店（Anita 说线上没有实体店）；店龄、同店、RSV／REV 没有书面定义，意臣出草稿、Anita 团队确认；子品牌是否单独展示（Anita 提问）；Dummy Store 有两种用法（新店占位 vs 周拆分尾差吸收）
- [stated] 会后行动：戴婷整理需财务提供的表样清单；Anita、Rita 有什么先给什么；意臣出数据字段清单、假设清单（Anita 团队确认）、维度和指标定义草稿；Sampson 要求意臣每场会后发中英文纪要（列 Ivy 的要求、下一步、待定项和依赖）并开始建带优先级的用户需求 checklist；Ivy 点名请 Sampson 介绍星巴克用 Dummy Store 做到周拆分无差异的做法
- [stated] 意臣（赵秋红）发出 11/3 会议纪要（英文摘要＋中文附件《CTF财务需求调研会议纪要_2026-11-03》，下次主题定为 Quarterly Forecast）；复核发现三处影响范围：把"AI 只出历史趋势线、新举措都在 PT"写成定位（只是 Anita 的理解，与 Ivy 流程及 SOW Baseline + Drivers 不一致）；漏记意臣"按协议所有系列都输出"的答复；写入了会上没有的"33 周预测"。另有人名笔误（倪晨宇、Vivan、孙继琨）

## 第一次项目周会（2026-11-06 周五 10:00–10:30，12 楼 1216＋Teams；黎新洪主持）
- [stated] 意臣（赵秋红）当天 13:00 发周报（W1 11/3–11/6）：只有进度表＋风险表两张图，无纪要和行动项；用户复核发现漏记 100K、版本管理、场景大表、数据需求日期、DSC 业务场景；任务 3（年度预算／季度滚测，计划 11/5）已逾期仍标 In Progress；下周 4 项无 Owner；风险 1 公式误写"Q3-1.5 IQR"（应为 Q3 + 1.5×IQR／Q1 − 1.5×IQR），且翻新无系统数据、有手工台账是已知缺口；正文日期写成 Nov 2–6。复核报告在 Claude Docs《AI SF 周会（2026-11-06）意臣周报交叉复核》并发了 Word 版
- [stated] Ivy 会上提 100K：Karen 群里告知 Sonia 要看 100K 以上货品（库存／销售，录音不清，币种未定）作为重要 KPI；AI SF trendline 按货类打 tag，分出售出 ASP >100K 的数量和金额，不必到 SKU；历史数据依赖 ICC（已请 Patrick 协调，可能难取）；Ivy 已告知 Vivian，PT、DSC/OTB 可能受影响；与 SF001 同类
- [stated] Ivy 会上提三系统版本管理：哪条 trendline 是最终推 PT、哪个 PT 版本回流 AI SF 再到 DSC，三系统统一版本命名（如 Final）；秋红称调研计划有版本控制专题
- [stated] 用户会上要求：每个场景拆输入、输出、颗粒度、数据流、依赖的 Excel 大表（秋红答应出"大宽表"）；会前清单至少提前 1–1.5 天发给财务
- [stated] 新洪要求意臣下周给出初步数据需求（至少到维度）及 DSC 字段能否满足的结论；秋红说约 11/20 明确——日期未对齐；新洪会后与秋红细化计划随纪要发出
- [stated] 孙方雨指出调研未安排 DSC 业务场景访谈（AI SF 哪些输出给 DSC、AP/DP 参数是否参考 AI SF），会上未闭环
- [stated] 秋红 WBS：需求 12 月结束、1 月确认、春节前蓝图确认；5 月前开发完、5 月 UAT；8 月上线陪跑；11 月陪跑完成；12 月"运维"（合同用语应为质保期）；调研 8 个主题，第 1 周讲完主题 1–2
- [stated] 周会仍定周五；Ivy 下周五（11/13）不参加
- [stated] 用户 2026-11-09 10:15 全部回复周报邮件，补记两项：100K（需求、ICC 数据依赖、行动：新洪向 ICC 确认数据、意臣出 tag 方案；用户把 KPI 关注人写成 Sonia/Karen）与三系统版本管理（行动：意臣纳入版本控制专题、列入三方会议题）；正式发出版删去了请 Ivy 确认库存／销售和币种的问题——这些仍待确认

## 门店类型 trendline 逻辑（Ivy 11/9 Teams，要用户 11/11 周三提醒她讨论）
- [stated] Ivy 列 5 类：①现有店／开业满 xx 个月 ②开业不足 xx 个月 ③未开业 ④翻新中将重开 ⑤关店；用户决定按 Ivy 5 类不再细拆，另补 3 类：⑥老店新开 ⑦Go dark（用户对"非翻新临时停业"如台风、商场整改的命名）⑧经营模式转换（直营／加盟寄售／加盟批发互转，转营）
- [stated] Ivy 11/9 晚定：老店新开、Go dark 不需要；经营模式转换需要——门店类型定为 Ivy 5 类＋经营模式转换共 6 类
````

### 01 AI Sales Forecast · areas/project-connections.md

- 原始路径：`/projects/01a1470f-ff85-76a8-9052-2edd4b94a69e/areas/project-connections.md`
- updated (UTC)：2026-11-09T02:16:41Z

````markdown
---
name: project-connections
description: How AI SF, Planning Tool and DSC/o9 connect — E1–E5/X1 flows, granularity, store-target source dispute, Ivy's 11/3 alignment rules, Power BI target publishing, Phase 2 timing gap (project copy)
sources: [cowork, chat]
aliases: [Project Connections, 三系统关系, 跨项目, E1-E5, 三方会议, 三系统数据流]
---

- [stated] E1：AI SF → PT，预测／趋势线，用于与 driver-based 目标比较
- [stated] E2：PT → AI SF，相对指定基线的调整差额（例：目标 120 对预测 100，差额 20），由 AI SF 按产品和门店重新分配（PT 没有门店层级）；同一差额只用一次，需冻结基线 ID、批准版、维度、期间和重传规则
- [stated] E3：AI SF → DSC，门店×产品目标（趋势＋调整＝目标，总额与 PT 一致）
- [stated] E4：DSC → PT，库存结果（库存余额／KPI）
- [stated] E5：PT → DSC，下一周期修订后的库存 KPI／目标（9/15 v3 图里的构想，10/21 数据流 15.2 同向）；X1：Finance → DSC 财务目标，只见于早期手册，PT 是否承接待确认
- [stated] 以上都是目标态的业务关系，目前没有任何已上线接口
- [stated] 门店目标来源仍有冲突：Vivian 10/21 要求 DSC 门店销售目标沿用 AI SF 的门店×周×货类分配结果，不要从 PT 大区数另拆，需与 Elsie 等核对原始 Excel 并在三方会议确认；o9 认为只接 PT、不接 AI SF；Elsie 记得 DSC 蓝图只到区域
- [stated] 颗粒度：PT 规划到区域×货类，不到门店（中国四大区与 Monologue 分列，正式层级名称待核）；AI SF 到门店×周×货类；目标按日入系统——需统一财历和跨月周，不能简单月 ÷ 4
- [stated] 10/21 审阅的数据流版本：10.3 暂保留（货类分配及 RGM 审阅后变化的回传校验），15.2 把管理层批准的期末库存用于下一轮预测；编号只适用于该版本
- [stated] 期初库存来源未查清：DSC 实际从哪取数、Lucanet 是否有门店粒度、是否已有集成、Excel 是否是中间加工步骤、谁维护
- [stated] 三系统数据流图约两个月前画的，早于 AI SF 供应商演示；三方会议前要请 Ivy、Elsie 重审，标出仍有效／已变化／未决
- [stated] 集团／市场财务目标原则上以 PT 为准；PT 和 o9 覆盖内地、港澳、国际，AI SF 首阶段只做内地，其他市场的门店目标来源待定（是否涉及 CR 未定）
- [stated] 模型链（CTF 页面，日期未知）：M1 预测（门店×周×货类／系列）→ 业务调整 → M2 门店目标分配（门店×周×货类，参考 M3 组货计划 AP）→ 门店级 MFP → M4 DP（门店×周×SKU，26 周）→ 驱动 OTB；M1／M2 属 AI SF，M3／M4 属 DSC／o9，SKU 级在 M3
- [stated] 上线时间差：AI SF 上线时 PT Phase 2 未必就绪；当前方向是在 PT 内做简易数字调整及回传、以后再扩展 driver（10/10 交 Vivian 审阅，未获批）；Excel 备用方案用户已于 10/9 删除，不要恢复；1008 SOW 里"PT Phase 1 调整通过模板导入"的合同条款仍在

## 11/3 调研会 1 的跨系统要点（Ivy、ICC）
- [stated] Ivy：PT、AI SF、DSC 的数据维度、时间（周定义）、门店号必须一致；三家供应商把清单拿出来比对、讨论粗细利弊，三供应商会议会安排
- [stated] Ivy：两种上线先后都要设计；绝不用 Excel 上传调整；PT Phase 2 未上线或系统宕机时，PT 只回传最终总数，AI SF 比差额后按财务录入的分配假设拆门店（即 E2 的总数版）；PT Phase 2 上线后 driver-based 调 ASP、Discount、Quantity、UPT 等
- [stated] Ivy：PT 是月数，AI SF 拆到门店×周后汇总必须等于 PT 月数（星巴克式 Dummy Store 吸收尾差）；每周 13 周 Outlook 不经 PT
- [stated] Ivy：区总确认后的门店目标要一键推到 Power BI 作 target，取代手工导入门店预算／滚测目标（E1–E5 里没有这条线）
- [stated] Ivy：DSC 按门店目标配货，最关心数量，所以 AI SF 的数量要准
- [stated] ICC：AI SF 与 DSC 在 o9 同一租户、同一套主数据；数据湖里有 DSC 相关六七张表

## 11/6 AI SF 周会的跨系统要点
- [stated] 100K 以上货品（Karen 转 Sonia 的 KPI，Ivy 提出）：AI SF trendline 要按货类打 tag 分出 ASP >100K 的数量和金额；Ivy 已告知 Vivian，PT 可能要改；DSC/OTB 也提过要分开——三系统都受影响，历史数据依赖 ICC
- [stated] 三系统版本管理（Ivy）：识别最终推 PT 的 trendline、回流 AI SF 再到 DSC 的 PT 最终版，统一版本命名；用户 11/9 邮件要求列入三方会议题
- [stated] 孙方雨（DSC PM）：AI SF 调研未安排 DSC 业务场景访谈（AI SF 哪些输出给 DSC、AP/DP 参数是否参考 AI SF 趋势），会上未闭环
- [stated] 三方会议仍按 12 月初；秋红称数据需求约 11/20 明确后再约三方会
````

### 01 AI Sales Forecast · areas/sbux-reference.md

- 原始路径：`/projects/01a1470f-ff85-76a8-9052-2edd4b94a69e/areas/sbux-reference.md`
- updated (UTC)：2026-11-10T01:30:55Z

````markdown
---
name: sbux-reference
description: Starbucks (SBUX) precedents relevant to AI SF — Dummy Store weekly reconciliation, event tagging, inventory as boundary, LTO new products; where SBUX material lives
sources: [chat]
aliases: [SBUX, 星巴克, Starbucks, SBUX for AI SF]
---

- [stated] 用户之前做过星巴克（SBUX）项目；claude.ai 里另有一个 "SBUX for AI SF" Project，资料和记忆在那边
- [stated] 用户要求 AI SF 需求调研阶段主动识别对当前需求有帮助的 SBUX 设计、逻辑、方案
- [stated] 11/3 Ivy：Sampson 可以介绍怎么帮星巴克做到周拆分"没有 variance"——用 Dummy Store 吸收某几周某些货类数量的多少，月合计仍与 PT 对平（对应 [[ai-sales-forecast]] 的月拆周需求）
- [stated] 11/3 Ivy 以"以前公司的经验"讲：翻新等事件要历史打标，模型不学闭店期的 0，否则预测偏低
- [stated] 9/21 纪要里的星巴克线索：库存是规则边界不是 AI 输入（饮品 RSP 不超过 42 元的例子）；组货做了多年也只到 subcategory；新系列可仿 LTO（业务给上市时间、货量、批次、参考历史系列曲线）；竞品门店因子效果不理想（Sampson）；天气数据由别的团队提供；尾款最后付给了供应商
- [stated] 另一份 11/3 复核稿（用户提供，引 PT 纪要，原件未在本项目核对）：9/16 Dennis 回顾星巴克用 4-4-5 财历、周能完整放进月，并认为 CTF 不宜为此改财历——CTF 自然月、周跨月，Dummy Store 不能照搬，需日级日历桥；9/16 还提到星巴克曾有南区覆盖北区、等待发布的权限问题；6/17 PT kick-off 曾要求 Novus 带回星巴克两系统维度与衔接经验
- [stated] 11/9–11/10 门店类型 trendline 逻辑表（给 Ivy 11/11 讨论用）：Ivy 定为她的 5 类（现有店／开业超 xx 月、开业不足 xx 月、未开业、翻新中待重开、关店）＋经营模式转换（直营／加盟寄售／加盟批发）；她说"老店新开"和"Go dark"不需要
- [stated] 该表三列 Store Type／Description／Previous Project Know-how；用户要求经验列借鉴 SBUX 里类似门店类型的逻辑、结合 CTF 应用而不是生搬硬套，且不出现 SBUX 字样；先出中文再出英文
````

### 01 AI Sales Forecast · topics/ctf-business-glossary.md

- 原始路径：`/projects/01a1470f-ff85-76a8-9052-2edd4b94a69e/topics/ctf-business-glossary.md`
- updated (UTC)：2026-11-03T11:48:37Z

````markdown
---
name: ctf-business-glossary
description: CTF business terms, metric definitions and product-category codes the user works with — read before interpreting RSV/REV/ASP/NGP/WOC/RO/PO or category codes (project copy, adds product-nature field semantics from the 2026-10-28 export)
sources: [cowork]
---

- [stated] RSV（零售销售额）不等于 REV（公司收入）：直营、加盟寄售、加盟批发下的转换逻辑不同，不能用单一比例换算
- [stated] NGP：10/22 命名标准化定为 Normalised Gross Profit；不是净利润
- [stated] ASP：同口径 ASP = 总 RSV ÷ 总 QTY，不能把各子项 ASP 相加或简单平均；AI SF 1008 SOW 写 ASP = RSP − Discount（折扣金额）
- [stated] SSSG：同店 RSV ÷ 同店基数 − 1，不等于全店同比；门店数是期末存量，不能逐月相加
- [stated] Forecast、Budget、Target、RMIP（门店指标分配）用途不同，不互相替换；Current 和 Previous 是具体的预测版本，PY 是上年比较
- [stated] WOC、DII、库存周转次数／天数／月数不能互换；比较前要统一期间、数量还是金额、币种、售价还是成本、平均还是期末库存、所有权范围
- [stated] RO = demand order（需求单），PO = purchase order（采购单），O3 = 在产订单；提前期分 RO→PO 和 PO→receipt；franchisee stock collection 指加盟商取货，不是收款
- [stated] Sign-off、合同审批、双方用印、文件命名是不同的事；SIT、UAT、缺陷关闭、业务签收也要分开
- [stated] 主类代码（product nature 字典，主组字段 material_nature_group）：F 饰品／工艺品黄金（足金类）、R 定价黄金、RU 黄金镶钻、A 钻石、K 玉类、J 宝石、C 珍珠、E 西金、PT 铂金、B 素金其他、MX 镶嵌其他、PA 包类、M 手表、M2 钟表配件、H 修理单、OX 展品、OZ 藏品、Z 赠品、ZZ 不适用、ZX 礼券、IF 工艺金条／金章、TF 投资黄金（依据 FY25 业务分类调整后的定义）
- [stated] 字典另有取值 NR 家品类、F99 金箱(足金)、P 铂金/K金类、0；product nature2.xlsx（#LN00071）12,369 条、55 列、568 个 stock_type、26 个 material_nature_group，updatedt 统一 2026-10-01，不代表正式生效日或 ICS 当前配置
- [stated] 字段语义：stock_type 详细货类编码，单独不是唯一映射键（190 个跨多组，排除 0/ZZ 后 40 个）；stock_group 附加分组；stock_nature 是款式／业务性质（戒指、耳环、投资金条），不是 A/F/R 主类；material_nature、material_nature_sum 材料性质及汇总；Group_Report_Type 是独立集团报表分类（定价首饰 ≠ 定价黄金 R）；Business_Type_1 是独立业务分类维度
- [stated] 不能凭首字母或单一历史编码归类，如 Q、G、AQ→MX，P→E/MX/P，FP→E/PT，CV→J/MX，VE→B/E，CD、GP→PT；具体货号以 ICS 当前设置为准
- [stated] 报表层级不等于字典代码：报表的"Gem-set (A)"是镶嵌类父层（含钻石、RU、和田玉、宝石、玉、珍珠、镶嵌其他）；"K gold"是西金标签，不是代码 K；部分滚测模型把 IF、TF 并入 F（4.0 IF 并 F，TF 在数量桥并 F）；1.0 模型里 F 称一般足金
- [stated] 重点系列（Signature Collection）：传承／HUA、故宫／Palace Museum、传福／Rouge、传喜／JOIE、万相／Dawn、传颂／Project S
- [stated] Store Concept（原称 Image）：Fashion（最高端）、Luxury、Main
- [stated] AI SF SOW 业务大类写法 R/F/Gem-set/Watches/Pt/K，Vivian 定 AI SF 统一用"Pt/K"

## 11/3 调研会补充（Anita、Ivy 口述）
- [stated] 财年 4 月 1 日开始；下一财年 Q1 直接用预算拆门店目标、不滚测，之后进入 3+9／6+6／9+3
- [stated] 店属性三种：直营、加盟寄售、加盟批发（寄售、批发都是加盟的运营模式；Anita 说直营也是寄售性质，含义待问）；直营 REV ≈ RSV 扣折扣率、积分使用率再去税；加盟批发 REV 只是批发价那部分收入；各货类批发率不同；全国活动的折扣主要影响直营（加盟商自担折扣、未必跟进）
- [stated] 店龄：同店 = 上一财年之前开、至少开满一整个财年（例：7 月时去年 5 月开的店仍不算同店）；次新店增长来自年化＋自然爬坡；关一家店约 60% 的生意被周边门店吸收（CTF 内部分析）
- [stated] 店形象是战略安排：主流门店 Main 月均约 200–300 万，下沉市场简化装修月均约五六十万，万象城、IFC 等高端商场开 Luxury；未来 3–5 年所有现有门店翻新并归入某种形象；11/3 转写还出现"会馆店""Select"，与 Fashion／Luxury／Main 的对应待核
- [stated] 中模 = 款式／模具层级，每个中模带系列标签；牌仔 = 单件货品编号，一件一个；约 80% 中模在库只有 1 件；有的货类周转达 20 个月；调行 = 门店间调货；缺货流失的需求无法量化
- [stated] 货类：大货类约 4 个，小货类 11 或 13 个（Anita 11/3 口述）
- [stated] 组织：门店管理科（开关店、翻新信息的口径和节奏）、BD 委员会（批新店及其 12 个月 RSV）、批发管理科（批发加盟商取货）、商品课（新品、重点系列计划）、中台（全国营销日历、折扣）、区域"营业"职能（区域目标 cascade 和编数）；子品牌 Monologue、ENZO、HOF（转写）、奥莱场
- [stated] 钟表全部直营，CTF 是经营方（代理劳力士、浪琴等），珠宝 CTF 是品牌方；电商约 95% 自营
- [stated] Dummy Store 两种用法要分开：没有正式店号的新店占位；Ivy 说的星巴克式周拆分尾差吸收店（保证门店×周汇总等于 PT 月数）
- [stated] 同店口径可能冲突：11/3 Anita 用"完整财年"口径；另一份复核稿称 9/15 战略规划、9/16 PT 纪要曾概括为"开满两年"——待用日期案例向 Anita 确认
````

### 01 AI Sales Forecast · topics/ctf-mainland-daily-finance-report.md

- 原始路径：`/projects/01a1470f-ff85-76a8-9052-2edd4b94a69e/topics/ctf-mainland-daily-finance-report.md`
- updated (UTC)：2026-10-28T12:26:41Z

````markdown
---
name: ctf-mainland-daily-finance-report
description: 國內財務日報（Power BI 自动推送的内地每日达标报表）— 来源、版面结构、字段口径、数据质量疑点和 10/11 快照；做 AI SF 实际数／达标口径对照时读
sources: [cowork]
---

用户 2026-10-28 要求吸收的邮件：[[rita]] 于 2026-10-12 转发给用户（FYI），附两份 PDF（数据日期 10/11）。关联 [[ai-sales-forecast]]、[[ctf-business-glossary]]。

## 来源与分发
- [stated] 发件：周大福系統通知 powerbiadminv1@chowtaifook.com（Power BI 自动推送），约每天早上 7:34
- [stated] 收件为分发组 BI_AUTO_TARGET_ACHEIVE_DAILY_REPORT_CN；用户本人不在列表上，是经 Rita 转发拿到
- [stated] 两个附件：《國內財務日報》（5 页）和《國內財務日報-分店性質》（3 页）；单位"百萬"，币种没有标注

## 《國內財務日報》结构
- [stated] 5 页对应 5 个期间：當日、當周累計、當月累計、當季累計、本年累計
- [stated] 列：整體、直營、加盟整體、加盟(寄售)、加盟(批發)；每组为 實際數、同比、年度預算達標率、季度滾測達標率、月度滾測達標率；月／季／年页另有 同店同比
- [stated] 行：整體按 RSV／REV／NGP 各拆货类（A、RU、CJ、J、K、C、PT、E、R、F、IF、TF、M）；再按 東區、南區、西區、北區、電子商務區、鐘錶中國區 给 RSV／REV／NGP；周及以上的页面多一行 NGPM(%)
- [stated] REV／NGP 行在加盟(批發)之后附 配貨、回倉、調行、寄售銷售、積分、淨開店店數、寄售轉批發分店數 等列（看起来是批发 REV 的组成项，含义待确认）
- [stated] 报表货类里出现 CJ，主类字典里没有；product nature2.xlsx 中详细 stock_type CJ 有 48 条（47 条归 J、1 条归 ZZ），不能据此定义日报 CJ，含义待确认
- [stated] 日报 13 个可见货类 ≠ 字典 20 个用户主类＋IF/TF（字典共 26 个 material_nature_group 取值）；未单列的类别不能自动解释金额勾稽差

## 《國內財務日報-分店性質》结构
- [stated] 3 页：自营门店、加盟寄售门店、加盟批发门店；每页横向是 当日／当周／月度／季度／年度
- [stated] 这份的达标列叫 年度／季度／月度"目標"達標率，主报表叫"預算"和"滾測"達標率；两份是否同一分母待确认
- [stated] 分店性質版的货类表多一个 NGPM 分货类块；自营含 TF、M，寄售和批发没有

## 数据质量与口径疑点（对 AI SF 有用）
- [stated] 所有页面、所有行的 季度滾測達標率 与 月度滾測達標率 数值完全相同；10/11 在季度首月可能合理，但本年累計页也相同，需要问清分母取的是哪一版滚测
- [stated] 小基数导致极端值：加盟 REV 同比 6380%、1183%；批发 A／K 的 NGP 达标率为负；電子商務區加盟 NGP 本年年度預算達標率显示 1,031,510,440.8%（预算接近 0）
- [stated] 加盟(批發) REV 远小于 RSV（10/11 当日 RSV 76.9 对 REV 8.0），印证 RSV→REV 在批发下不能按单一比例换算
- [stated] 报表包含電子商務區；AI SF 1008 SOW 范围不含电商、含钟表，对照准确率时要剔除电商

## 10/11 快照（百萬，仅作基准）
- [stated] 本年累計（FY27 至 10/11）：RSV 44,080（同比 −0.8%，同店 +4.0%，年度預算達標 91.9%，滾測達標 98.8%）；REV 32,018；NGP 7,025
- [stated] 當月／當季累計：RSV 3,640（同比 −23.9%，同店 −22.2%，滾測達標 87.5%）；NGPM 22.9%
- [stated] 當日：RSV 253.2（同比 −12.2%）；R 类 −78%、F 类 +40%；電子商務區本月 RSV +31.6%，线下四区都在 −25% 左右
````

### 01 AI Sales Forecast · people/anita.md

- 原始路径：`/projects/01a1470f-ff85-76a8-9052-2edd4b94a69e/people/anita.md`
- updated (UTC)：2026-11-03T11:36:20Z

````markdown
---
name: anita
description: Anita Lu (陆颖君) — leads mainland sales forecast & analysis (FP&A), key AI SF user; her view of AI SF vs Planning Tool (project copy)
sources: [chat]
aliases: [Anita, 陆颖君, Anita Lu, 妮塔]
---

- [stated] one of the key users of AI SF at Chow Tai Fook
- [stated] 全名 Anita Lu Ying Jun（陆颖君），常驻上海，带中国区 FP&A topline 团队；"Anitah"是旧拼写
- [stated] 10/8 由她向 Vivian 提供初版 Scorecard；Rolling Forecast 访谈要按她团队的时间安排；指定 [[rita]] 参与 DSC 参数工作
- [stated] 11/3 自述负责内地销售预测与分析团队，正在编 FY28 预算；在调研会上讲了年度预算现行流程（见 [[ai-sales-forecast]]）
- [stated] 11/3 的理解：AI SF 是跑基于历史的 trendline 的工具，举措都在 Planning Tool 里加；希望工具能预测某场活动应达到的 ASP；问过子品牌是否要单独展示
````

### 01 AI Sales Forecast · people/ivy.md

- 原始路径：`/projects/01a1470f-ff85-76a8-9052-2edd4b94a69e/people/ivy.md`
- updated (UTC)：2026-11-03T11:36:16Z

````markdown
---
name: ivy
description: Ivy Cheng (鄭凱因) — Finance VP, AI SF project lead, PT sponsor; her 11/3 discovery framework, English-email preference, Starbucks references (project copy)
sources: [chat]
aliases: [Ivy, VP, Ivy Cheng, 鄭凱因, 艾比, 艾薇]
---

- [stated] VP at Chow Tai Fook; ranks above [[vivian]], the user's boss
- [stated] 全名 Ivy Cheng（鄭凱因），Finance VP；Planning Tool Sponsor；AI SF 项目负责人（业务目标、范围、阶段成果确认、SOW sign-off）
- [stated] 与 Financial Systems 团队的 Ivy（黄凯仪，[[ivy-huang]]）是两个人，不能合并
- [stated] 11/3 自称以前是 [[ai-sales-forecast]] 的 finance PM；调研期每周只能参加第一场，做高层框架讨论，细节由意臣问 [[anita]] 团队
- [stated] 发给她的邮件要用英文，只有中文她可能不看
- [stated] 11/3 定了 AI SF 的 5 个场景框架（预算、季度预测、月度滚测、每周 13 周 Outlook、What-if），并说可能直接让 Sampson 跑金价 What-if（Karen 每天在问金价影响）
- [stated] 会上多次引用星巴克经验：11/3 Dummy Store 吸收周拆分尾差；9/21 库存作规则边界、组货只到 subcategory、新品仿 LTO；另以"以前公司的经验"讲翻新历史打标（见 [[sbux-reference]]）
````


---

## Part B · 项目：02 Planning Tool

- 记忆文件夹：`/projects/01a14710-8d0b-719f-888a-766abd27def7/`

### 02 Planning Tool · preferences.md

- 原始路径：`/projects/01a14710-8d0b-719f-888a-766abd27def7/preferences.md`
- updated (UTC)：2026-10-28T03:45:05Z

````markdown
---
name: preferences
description: How the user wants Claude to format work outputs in Planning Tool conversations — the Chow Tai Fook (周大福) Excel house style to apply to every Excel deliverable
sources: [cowork]
---

## Excel house style — 周大福风格 (asked to remember, 2026-10-28)
- [stated] asked to remember: the Excel style in "CTF_Elsie_Follow_Up_Tracker.xlsx" and "Sampson_Daily_Issue_Tracker.xlsx" is the Chow Tai Fook-style colour scheme and font to follow for Excel outputs
- [stated] reference A (Elsie Follow-up Tracker): font Arial; title row 2, 16pt bold, red #CA001B, no fill; summary/KPI strip row 4 fill #F4F2F1, labels 10pt #202327, KPI values 12pt bold #CA001B via COUNTIFS formulas; header row fill #CA001B, white bold 10pt, centred, bilingual header text ("Description\n事项说明"); body 10pt #202327, Topic column bold; banded rows #FFFFFF / #F7F6F5; thin borders #E2DEDD; secondary text #626978; gridlines off; freeze panes below header; no merged cells
- [stated] reference B (Daily Issue Tracker): font Noto Sans CJK SC; title 17pt bold burgundy #8F1830; KPI labels 11pt grey #68727A, KPI values 17pt bold #8F1830; header fill #8F1830, white bold 11pt; body 11pt #263238; banded rows #F8F6F4 / white; no cell borders; gridlines off; a separate 使用说明 sheet with bold #8F1830 labels in column A
````

### 02 Planning Tool · profile.md

- 原始路径：`/projects/01a14710-8d0b-719f-888a-766abd27def7/profile.md`
- updated (UTC)：2026-10-23T05:39:00Z

````markdown
---
name: profile
description: Project copy of who the user is — background facts stated in Planning Tool conversations
sources: [cowork]
---

- [stated] previously worked at Lenovo (联想), where they took part in UAT on large ERP programmes; draws on that UAT methodology for current work
````

### 02 Planning Tool · areas/ai-sales-forecast.md

- 原始路径：`/projects/01a14710-8d0b-719f-888a-766abd27def7/areas/ai-sales-forecast.md`
- updated (UTC)：2026-10-27T04:19:14Z

````markdown
---
name: ai-sales-forecast
description: Project copy — AI Sales Forecast items raised in Planning Tool conversations (read with the account-level ai-sales-forecast file)
sources: [cowork]
aliases: [AI SF, AISF, AI Sales Forecast, 销售预测项目]
---

## Requirements discovery timing (1:1 with Vivian, 2026-10-27)
- [stated] AI SF kick-off meeting on Thursday 29 Oct 2026; vendor (意臣) then starts user-requirement collection
- [stated] [[li-xinhong]] estimates requirements collection needs at least ~2 weeks
- [stated] [[anita]]'s team not available week of 2 Nov (actuals closing, topline / 7+1 forecast); week of 9 Nov first days still busy
- [stated] Vivian's suggestion: vendor sends the requirement list / points to align in advance (e.g. by Tuesday noon for a Wednesday meeting), key person reads and confirms by email or joins a ~1 h clarification; avoid starting from scratch; aim roughly 9-17 Nov so user can then move to Planning Tool UAT (18-19 Nov)
- [stated] user to ask Anita which format her team prefers (short sessions every other day vs a half day ~12-13 Nov, after 9 Nov)
- [stated] Vivian: users must attend — user cannot stand in for Anita's team; AI SF takes priority over user's presence at Planning Tool UAT

## New requirement from 2026-10-27 inventory report demo
- [stated] Ivy: AI SF should tag/project sales and quantity trend and mix by price band (e.g. above / below 100k ASP per category) to support inventory planning; not in the RFP — user to record it and include in AI SF requirements gathering
````

### 02 Planning Tool · areas/planning-tool-bs-cf-review.md

- 原始路径：`/projects/01a14710-8d0b-719f-888a-766abd27def7/areas/planning-tool-bs-cf-review.md`
- updated (UTC)：2026-11-02T07:14:51Z

````markdown
---
name: planning-tool-bs-cf-review
description: Planning Tool BS / Cash Flow / Inventories — CFO review layout (2026-10-16), 2026-10-21 inputs/dashboard sign-off meeting decisions, and the revised direct-method CF template structure sent to Novus 2026-10-23
sources: [cowork]
aliases: [B/S and Cashflow review, BS CF review, BS/CF dashboard, 资产负债表与现金流审阅, BS CF Inventories sign off, Revised CF model, 现金流模板]
---

## Source
- [stated] email "B/S and Cashflow review", 2026-10-16 (18:18 HKT), from [[vivian]] to [[dennis]] (Novus), cc user (Sun Yang / Samson); layouts given as 4 screenshots
- [stated] content = what the CFO ([[karen]]) looks at in her B/S review and CF review; relates to UAT topic "BS/cash flow/KPI scorecard" in [[planning-tool-uat-golive]]

## Balance Sheet review
- [stated] columns: Current Year (budget or forecast), Last Year, YOY $, YOY %
- [stated] based on "Balance Sheet Review – September" pack: Consolidated Statement of Financial Position (extract), HK$ million
- [stated] Non-current assets: Property, plant and equipment; Lease assets (non-current)
- [stated] Current assets: Inventory; Trade and other receivables; Bank deposits and cash equivalents → Total Assets
- [stated] Current liabilities: Trade and other payables; Lease liabilities (current); Bank borrowings (within one year); Gold loans
- [stated] Non-current liabilities: Lease liabilities (non-current); Bank borrowings (more than one year); Convertible bonds
- [stated] Total equity
- [stated] Supplemental: Total Borrowings & CB (bank borrowings + gold loans + convertible bonds); Bank deposits and cash equivalents; Net debt (= Total Borrowings + CB − Bank & cash equivalents); Working capital (net current assets)
- [stated] BS KPIs – Operating efficiency (working capital): DSO, DPO, DII (days of inventory turnover), CCC (cash conversion cycle)

## Cash Flow review ("Chow Tai Fook Jewellery Group – Cash Flow Analysis")
- [stated] columns: Current Year, Last Year, YOY $, YOY %
- [stated] Operating cash flows before movements in working capital (PBT + non-cash adj. items); Lease paid; Net cash from (used in) inventories; Net cash from (used in) other operating activities; Capital expenditure → Pro forma free cash flow
- [stated] then: Net change in bank borrowings; Net change in gold loans; Net proceeds from convertible bonds; Dividends paid; Dividends received; Other movements; Net cash outflow used in acquisition of subsidiaries; Capital contribution from a non-controlling shareholder of a subsidiary; Repayment of capital to non-controlling shareholder of subsidiaries → Net increase (decrease) in bank balances and cash
- [stated] Cash and cash equivalents (opening) and (closing)
- [stated] Vivian: some items may not exist in the system CF statement — map to the closest line available
- [stated] shown in red in the screenshots (reason not given): BS Convertible bonds; CF lines for inventories, bank borrowings, gold loans, convertible bonds

## 2026-10-21 meeting "Planning Tool - Inputs/Dashboard sign off: BS / CF / Inventories" (Teams 17:00-18:00 HKT)
- [stated] organiser Vivian; attendees Ivy (VP), Elsie, Arthur Leung, user, Dennis, [[andy-wu]]; purpose: sign off template format after Novus updated BS/CF/Inventories per demo feedback
- [stated] user sent key-takeaways email the same evening (5 items, table: requirement / follow-up / PIC)
- [stated] 1 CF classification: separate operating vs financing/investing cash flows (Karen's request); distinguish gold purchase for production vs for gold-loan repayment; update format first; currency realignment system-calculated, other lines are inputs. Flow: Dennis exports current template → Arthur/Jay draft (target 22 Oct) → Ivy reviews → Vivian final check → Dennis reimports and reconfigures currency realignment → further review
- [stated] 2 Inventory: quantity and value on same page, keep unit cost and inventory KPIs; turnover shown in days and months; split Offline Jewellery by store type, "Uncategorized" where N/A (e.g. e-commerce). Dennis to remove turnover display restrictions; input/aggregation method for 200,000 banding to confirm with Nana and Zoe — band boundaries and owner still open
- [stated] 3 OTB: finished goods keep product categories incl. Watch, remove N/A items (Service Income, Jewellery Trading); raw materials classified separately by material type incl. Gold, with Gold broken down by intended product use. Dennis adjusts RM hierarchy/order; Vivian + user check system display against names confirmed by Elsie
- [stated] 4 Labels: Phase 1 English labels only, fix spelling/capitalisation/naming; Chinese/bilingual for non-finance users in later phases. Vivian + user check page labels; A&P UAT cases must include Traditional/Simplified Chinese/English and mixed-language project names; testers confirmed in UAT assignments
- [stated] 5 Reports: Cash Flow confirmed after revised template is in; inventory report reviewed separately from input template; once inventory labels verified, repeat input-template review may not be needed
- [stated] 2026-10-22 Dennis sent the CF input template downloaded from the system, asking for the new template after Arthur and Jay review
- [stated] 2026-10-23 Vivian sent "Revised CF model_with VL edits2_toNovus.xlsx" (final = column K) asking Dennis to reimport; cc Jay (Hui Wang Nam)

## Revised CF template (2026-10-23, direct method)
- [stated] workbook: sheet "Comparison" (Old / Revised / changes col J / col K final / remarks) + sheet "CN Cashflow forecast" (CTF China, direct method, RMB'm, +ve inflow / -ve outflow, monthly columns + total)
- [stated] structure: Opening cash → (i) Operating Cash Inflows (A)+(B)+(C) → (ii) Operating Cash Outflows (D)+(E)+(F)+(G) → (iii) Investing Cash Inflows (H) → (iv) Investing Cash Outflows (I) → (v) Financing Cash Inflows/(Outflows) (J) → Net Cash Inflow/(Outflow) for the Period → Closing cash (+ Closing cash HKD)
- [stated] (A) Receipts from customers: A1 Jewellery Self-operated (self / 3rd-party collected), A2 Franchise (Consignment / Wholesale), A3 E-commerce, A4 Watches, A5 Service fee income from Franchisee, A6 International markets, A7 Jewellery trading
- [stated] (B) Business Model Change Receipts - Franchise: B1 store-opening deposit, B2 business-model-change receipts (B2.1-B2.7), B3 franchisee credit limit expired, B4 Others; (C) Other Receipts: franchise income, commission, trade/loan receivable interest, government subsidy, others
- [stated] (D) Purchase: D1 Gold (purchase from suppliers and repurchase from customers, each as kg × avg price per g), D2 Diamond and tax, D3 Other raw materials and processing fees, D4 Watches (purchase, rebate); (E) SG&A Expenses E1-E9 named in line with P&L; (F) Business Model Change Payments - Franchise (store-closure buyback, F2 model-change payments, F3 renovation deposit refund, F4 Others); (G) Taxation, Intercompany processing fee
- [stated] (H) H1 rental income, H2 others (currency realignment was briefly put at H2 on 27 Oct, then moved on 2 Nov — see below);
- [stated] 2026-11-02 decision (Ivy): currency realignment is not in H or J; "Opening cash & cash equivalents" splits into two expandable detail lines — "Closing balance from previous month" + "Currency realignment" (input, can be +/−); their sum is the month's opening balance; currency realignment is not forecast — only a bridging adjustment in the first forecast month when actual and forecast FX differ, rest zero; Jay had wanted it under J12 other adjustments; Dennis configures, Vivian reviews; rest of structure unchanged
- [stated] 2026-11-02: Dennis had loaded CF names from the "CN Cashflow forecast" sheet, not Vivian's revised column K — must follow the revised version, esp. sections B, E ("SG&A Expenses") and F; user reviews Dennis's corrections before CF template sign-off (I) CAPEX, others; (J) funding pool, dividend, trademark, convertible bonds, Panda Bonds, bank borrowings (each with principal/interest repayment), gold loan borrowings/repayment (kg × avg gold price), other adjustments
- [stated] Vivian's edit rules: section headings capitalise each word; other line items only first letter capitalised; "Self-operated" hyphenated as in P&L; "interest" without s; "Panda Bonds" kept as a name; decoration → renovation; colons removed; F2.8 Others removed per discussion with Ivy; Chinese labels changed to English
````

### 02 Planning Tool · areas/planning-tool-capex-template.md

- 原始路径：`/projects/01a14710-8d0b-719f-888a-766abd27def7/areas/planning-tool-capex-template.md`
- updated (UTC)：2026-10-29T03:17:06Z

````markdown
---
name: planning-tool-capex-template
description: Planning Tool CAPEX import templates (IT/Store/Office/PSC) — 2026-10-26 Capex inputs sign-off meeting, revised IT CAPEX template structure, field rules, CAPEX UAT scenarios and master-data gaps
sources: [cowork]
aliases: [Capex sign off, CAPEX 导入模板, IT CAPEX template, 020_IT CAPEX, Capex inputs/dashboard sign off]
---

## 2026-10-26 meeting "Planning Tool - Inputs/Dashboard sign off: Capex" (Teams 9:30, ran ~09:27-10:14)
- [stated] organised by user (Sampson); attendees Ivy (VP), Vivian, [[wu-qi]] (IT CAPEX owner), [[dennis]], [[andy-wu]]; Vivian joined late, Ivy left early for a call with Karen
- [stated] purpose: show how far the CAPEX templates improved after earlier back-and-forth and get format sign-off
- [stated] user sent key-takeaways email the same day (Vivian's 4-column table): 1 IT template — Wu Qi considers existing fields broadly sufficient for manual upload and record keeping; 2 field classification — Dennis to classify each template's fields into stable project attributes vs per-cycle amount/timing assumptions; 3 UAT scenarios before scripts

## Revised IT CAPEX template (020_IT CAPEX, sent by Novus ~Thu/Fri 22-23 Oct)
- [stated] Novus removed duplicate fields and reordered so fields shared across CAPEX templates (level, cost center, department, project) come first, module-specific (e.g. IT) after; added Instructions sheet with field explanations, examples and formats
- [stated] columns: Level Code (business market) | Tag Name (anchor of which cycle the project started, e.g. FY28 Budget — replaces the New/Carry-forward flag) | Project Status (Approved/Budgeted/Deleted) | Type of capex | Start Date | Completion Date | A-Dan (budget approval) | R-Dan (PO) | Cost Center Name or Code | Department Name | Project Name or Code | Proj Description/Remarks | Owner of Project | Category (IT only) | IT Project Type (IT only) | IT Project Expense Type (Cloud/Capex, IT only) | Total Project Amount | Payment Timing 1-4 | [Overwrite] Payment Amount 1-4 | depreciation months
- [stated] dates MM/DD/YYYY; name or code — fill either, code recommended (Chinese names risk full/half-width mismatches); one shared department list in the system; free-text extras go in Description/Remarks
- [stated] dimension name/code linked inside Workday (name can repeat across markets, code unique); blank dimension value → reported under "Uncategorized"; Project made a dimension (not text) so reports can slice by project
- [stated] payment timing hard-coded in Phase 1: default = Start Date + 2/3/4/5 months, amounts pre-split by ratio; fill overwrite amounts only if not using the default split; leaving timing to user input would need a per-year assumption each cycle (Dennis: not sensible)
- [stated] depreciation calculated from completion date, useful life and amount entered
- [stated] amounts converted by each level's currency (CN CNY, HK HKD), group consolidated to HKD at system rates
- [stated] missing lists flagged in template: IT Type of capex, full project list, IT project type, expense type
- [stated] Wu Qi will add an IT dimension for which function a system serves (Finance / Operations / HR …)
- [stated] adding columns or changing calc logic later is easy; removing columns may affect stored data — so Phase 2 integration changes remain possible

## Versions and import
- [stated] each version (Budget v1/v2, 3+9 v1-v4…) stores its own template data; copying a version (e.g. 3+9 → 3+9 v2) carries all imported rows over, no re-import needed
- [stated] import offers several modes (Dennis: 5) incl. append and full overwrite; Dennis will explain them in instructions; single-row fixes otherwise

## Ivy's direction (cycle vs project data)
- [stated] Planning Tool is not a project management system; each template must tag which data belong to the project (name, owner, market…) vs to the cycle (timing, amounts that change each 3+9 / 6+6 / 9+3)
- [stated] Phase 1: everything manual upload, no link — project codes (0001…) are maintained in offline Excel, so no system linkage; Phase 2 must design this properly
- [stated] Ivy plans to have Frank build a centralised Excel project-code database (likely next year) covering CAPEX, A&P, Prof Fee; Planning Tool imports from it and FP&A only updates timing/amounts; cancelled projects close their code, re-purposed money gets a new code
- [stated] Ivy expects Novus to sit in on Phase 2 workshops even before contract signing

## CAPEX UAT scenarios
- [stated] CAPEX UAT around 10 Nov (not 16-17 Nov)
- [stated] scenarios Ivy listed: Budget upload; edit (add row, delete row, change numbers of existing project); compare v1 vs v2; duplicate-project upload (does system flag/reject? expected outcome to verify); 3+9 upload of same project list with changes, v2 delete/add/change, compare v2 vs v1, v1 vs Budget, v2 vs Budget; download; finalise submission
- [stated] flow: Dennis drafts scenario list (expected 28-29 Oct) → user reviews with Wu Qi → user + Ivy / Vivian review → user returns to Dennis → Dennis writes scripts → Wu Qi (+1-2 people) executes on test day, marking pass/fail with reasons → Dennis fixes
- [stated] Ivy will also check scenario coverage (she has done CAPEX before)

## Master data gaps (Dennis's email to user and Vivian the week before)
- [stated] incomplete: department list, store concept list, COA for A&P and Prof Fee, IT type, project type, expense type (only 2), project list
- [stated] user to ask Wu Qi whether UAT uses real projects (then real lists needed) or dummy (001/002…; production lists loaded again before go-live)
- [stated] cost centers: user has the EAS list; HK & International cost centers are in SAP — get from [[cai-kun]] in the same format Dennis needs
- [stated] cost center source files the user holds (shared 2026-10-29): mainland "CN Cost Center" list — 316 rows (code + name), codes mostly numeric but some alphanumeric (e.g. 20003XT, JRBQ01), includes "-虚体" (virtual) and "（部门调整）" entries, 15 names repeat; SAP cost center export dated 10.23 — 1,101 rows, controlling area CTFJ, ~60 company codes (1003 largest, then 1016, 1023, 1025, 1054), category W/V, short text in Chinese, 5 expire 2026-08-09, names repeat across company codes (675 distinct) — so import by code, not name
- [stated] COA: Vivian has a version to send Dennis; Phase 1 only needs a short COA dropdown for A&P and Prof Fee (COA as a dimension elsewhere would mean maintaining it twice)

## Next reviews
- [stated] Vivian sending placeholder for Friday 30 Oct morning P&L and Balance Sheet walkthrough with FP&A (Dennis unavailable Friday afternoon); align that afternoon (26 Oct) with "阿斐" (as transcribed) on what FP&A will see
````

### 02 Planning Tool · areas/planning-tool-reporting.md

- 原始路径：`/projects/01a14710-8d0b-719f-888a-766abd27def7/areas/planning-tool-reporting.md`
- updated (UTC)：2026-11-02T07:14:58Z

````markdown
---
name: planning-tool-reporting
description: Planning Tool output reports — P&L webform, BS & cash flow webform, CFO scorecard (OfficeConnect), inventory report — decisions from the 2026-10-26 reporting review with Ivy/Elsie
sources: [cowork]
aliases: [P&L BS Cashflow CFO scorecard review, Financial Report Optimization Discussion, 财务报表及上线准备会议, CFO Scorecard, OfficeConnect scorecard]
---

## 2026-10-26 meeting "CTF Planning Tool - P&L, BS & Cashflow, CFO scorecard" (Teams 14:00-15:00)
- [stated] organiser Vivian; attendees Ivy, Elsie, [[dennis]], [[andy-wu]], [[issac-lau]], user; Frank joined mid-way for the scorecard
- [stated] purpose: Ivy/Elsie review completed P&L (summary + detail) webform, BS & CF webform, CFO scorecard in OfficeConnect before the FP&A demo on 30 Oct
- [stated] user sent key-takeaways email + CN minutes "Planning_Tool_Reporting_MoM_CN_20261026" (5 items) same day, cc Frank

## FP&A demo (30 Oct)
- [stated] Ivy: demo as a story — use a 9+3 / Budget scenario to walk through submission, roll-up and drill-down (effectively an end-to-end demo); Vivian provides the scenario, Dennis prepares, Ivy/Elsie review first

## P&L report
- [stated] two reports, thousands and millions, identical structure; QTY always in thousands (label it), ASP always in dollars with 2 decimals (label it regardless of report)
- [stated] store count: no decimals in reports, keep decimals in input/dashboard pages so users catch wrong entries
- [stated] header/label rows in bigger font, all figures same font size; keep blank separator rows
- [stated] removed redundant section-heading blocks (NGP, SG&A, Other Income, NOP to NP headings); kept the "Profit Margin" heading (Excel version used % of revenue) and SG&A at its original position (expandable)
- [stated] channel filter (retail / e-commerce / wholesale…) works with level, e.g. Group + e-commerce = all e-commerce; set to single-select
- [stated] drilling a dimension that isn't populated shows "Uncategorized"; heavier custom layouts → users copy to a personal report

## Balance sheet & cash flow
- [stated] BS: key metrics at top; current assets before non-current; Equity retained; metric renamed Gearing Ratio; otherwise no change since last review
- [stated] CF: Dennis reloading the new structure (many renames, per version reviewed with Vivian and Jay) on 26 Oct; Ivy wants to see the final product
- [stated] 27 Oct 10:00 session: first 45 min inventory report demo (large FP&A audience), last 45 min smaller-group CF review

## CFO scorecard (OfficeConnect)
- [stated] tabs per version (Budget, Actual…), version filter + refresh pulls live Workday data; blue linked cells are system-driven — don't edit
- [stated] Ivy: this sheet is raw data, not what goes to Karen; Frank to automate the presentable scorecard from it (refresh → PY / Budget / Forecast comparisons populate in seconds, like the weekly BI refresh she had at Starbucks), so her team stops spending 1-2 h checking — Karen keeps finding formula errors in the scorecard
- [stated] OfficeConnect magnitude is workbook-wide (would scale store count and gold price) → handle units per metric; don't put "HKDm"-type suffixes into Workday standard names, add them in the scorecard template
- [stated] market vs channel attributes can't sit in one list (e.g. Retail sits under China) → option: Dennis supplies raw data by level and Frank links via formulas/pivots; Dennis, Frank and Aaron to decide per section (Ivy: scorecard contact is Aaron, Yetta is more P&L)
- [stated] add Frank to subsequent scorecard meetings; Frank to start in November (December busy with 9+3 and budget)

- [stated] 27 Oct Dennis sent Vivian the OfficeConnect template "FY27_Raw_Data_Scorecard_Office Connect.xlsx" (users with OfficeConnect installed retrieve data through it); 29 Oct Vivian forwarded it to Frank (cc user) as the current Planning Tool version of the CFO scorecard
- [stated] OfficeConnect file: tabs per version (Budget, Actual FY24 monthly + quarters, Actual FY23 full year, a working sheet) with system time tokens like "Month (current-15)-Year (current)"; rows are Workday accounts with market prefixes (China-, Hong Kong & Macao-, International-, HQ-; CN/HKM/Intl E-commerce-) and suffixes like "-Store Type"; covers gold price (weighted average, normalised), store count roll-forward, RSV, HOF, SSSG RSV/Qty/ASP by store type, Qty, ASP, Revenue, category lines…
- [stated] 29 Oct meeting "CTF FP&A submission tool - CFO scorecard raw data format" (15:30-16:00; Vivian, Dennis, user, Frank, Aaron, Andy) on the OfficeConnect raw-data format; Vivian then sent Frank "FY27 Scorecard - blank.xlsx" as the look-and-feel reference
- [stated] Vivian's instruction to Frank: keep the existing scorecard look and feel but use the new line-item naming already in Planning Tool (e.g. CN → "China", HKM → "Hong Kong & Macao")
- [stated] existing scorecard ("FY27 Scorecard - blank", single P&L sheet, Group level): columns current forecast (e.g. FY27 4+8F) vs previous forecast final (3+9F Final), PY actual, Budget, with variances vs each, monthly Apr–Mar; rows: gold price assumption, store count opening/closure by CN/HKM/Intl, RSV (HKD M; CN in RMB M) by market + HOF + e-comm, SSSG (CN self-op / franchise, HKM, Intl), RSV category mix % and RSV / Qty / ASP by category (Gem-set sub-lines, Pt/K gold, Gold products R/F+IF, CTF Home, Watch, Service Income, Jewellery Trading), Revenue (incl. excl. SCM; wholesale/retail/e-com/CN Watch), NGP and NGPM by market and by category, SG&A and SG&A % by market/channel and by expense type, NOP (incl. excl. provision)

## Inventory report (pre-run with Elsie, 26 Oct)
- [stated] Elsie: Phase 1 inventory report is for checking totals and trends of what was uploaded, not for reporting; keep layout simple — market view shows Finished Goods and total
- [stated] remove Service Income; keep Jewellery Trading; zero rows disappear once "suppress zeros" is on with real numbers
- [stated] store type moved from rows to a top selector (row version looked too cluttered); other adjustments only at group level, market sees total only
- [stated] turnover selectable by day or month; quarter/year view for high-level users, drill to month; users can copy to own report for other views

## 2026-10-27 meeting "CTF Planning Tool - demo - Inventory Report" (Teams 10:00-10:45, FP&A audience)
- [stated] attendees incl. Ivy, Vivian, Elsie, Zoe, Liu Yanzun (刘艳遵), Nana, Priscilla (黄荟, new), Anita's team, Frank, Novus; user sent key-takeaways email (3 items) same day
- [stated] Ivy restated Phase 1 objective: manual uploads to keep and compare budget/forecast versions (group submission before Karen review, revised after, final) for version variance and April budget true-up; management review and detailed analysis stay in Excel; Phase 1 doesn't replace Excel
- [stated] report layout (Workday): Value and Quantity reports; rows = Total Inventories (with adjustments, collapsible), Turnover (month or days, selectable), Inventory per store, expanded by Product Category; columns = current version vs comparison version, variance and %; filters: Current Forecast, Comparison Forecast, Level, Time from/to, Store Type, Inventory - ASP Range, Turnover, FG/RM; drill into FG vs RM per row; "Inventory and OTB" dashboard tabs: Inventory, OTB, Report (Quantity), Report (Value), with "find report" link to the source report
- [stated] users can copy reports to personal folders and pivot dimensions (e.g. store type instead of category); suppress-zero rows; every page exports to Excel/PDF
- [stated] turnover days vs months use the same formula (month-end inventory ÷ cumulative COGS), only multiplied by days or months
- [stated] store concept (Fashion/Luxury…) per-store averages and brand are not in Phase 1 inventory; brand flagged for inventory Phase 2
- [stated] actuals uploaded manually in Phase 1 into the Actual version; actual overlay takes actuals before the cycle cut-off month and opens later months for input, at whatever granularity was uploaded; handling a not-yet-updated month to be validated in E2E UAT; Phase 2 integration waits until data is ready in Lucanet/BI
- [stated] price band threshold changed from 200k to 100k (Elsie, morning of 27 Oct); Nana must re-pull historical actuals (she extracts below-band then derives above-band = total − below); budget must use new band, rolling forecast applicability TBC
- [stated] decided: Phase 1 keep it simple — markets submit Total plus a below-100k figure as reference (top-down / allocation), not a bottom-up sum; Workday can't input into a roll-up total, so Dennis will split into two sheets (total and 100k split) with linkage, needing 1-2 days; show final product Friday 30 Oct for sign-off; finer logic via Phase 2 change request
- [stated] Phase 2 requirements: business users send to user and Vivian by email or group chat, consolidated for requirements and the Phase 2 budget discussion with Lydia, Karen, Patrick

## 2026-10-27 follow-up "Business Data Discussion" (10:43-11:16; Vivian, Ivy, Elsie, user, Dennis, Arthur, Frank, Aaron)
- [stated] official invite "CTF Planning Tool - demo - CFO Scorecard" (Vivian, 27 Oct 10:45-11:30; invitees incl. Aaron Fung 馮家朗, Andy, Issac, Frank); scorecard itself was already reviewed 26 Oct, so the session covered CF update, version naming and Phase 2 multi-currency
- [stated] user wrote CN minutes "Planning_Tool_CFO_Scorecard_MoM_CN_20261027" and sent the English key-takeaways email the same day (3 items: version naming, version management & FX UAT as S1/S2, Phase 2 international multi-currency)
- [stated] CF: currency realignment is system-calculated (from opening/closing FX) and can't take input; placed under (H) Receipts from investing activities as new H2 "Currency realignment" between H1 Rental income and Others (Others becomes H3); can be explained to Karen via remark
- [stated] version naming: two budgets per year — January budget (go-live) and April true-up budget; past budget cycle reached ~65 versions (Jan + April); Ivy proposes Starbucks EP style: number = review round (V1 = first round with Karen, V2 = with leaders, V3 Final = aligned with Sonia/Kent = January budget; April true-up continues V4-V6), letters A-Z for iterations within a round, suffix "Review" for versions reviewed with someone and "Final" for the final; maintain an online glossary/description per version (e.g. gold price 4,000 in 1A) instead of names like "Karen version"
- [stated] Aaron + Vivian to set the naming rule (Ivy won't decide at her level), Dennis configures; user is the test — if user can't tell what a version is, the naming isn't good enough; Aaron used to save each reviewed version into a "for final" folder and compare final vs final, not every version
- [stated] Phase 2 international: Karen likely to want constant-currency analysis; International to split into markets (Taiwan, Singapore, Malaysia, US, Dubai…) submitting local-currency P&L; Dennis: add currency + FX rate and assign to new levels under a new branch, keep the Phase 1 International structure/history untouched; channel views roll up across markets in HKD via attributes

## 2026-11-02 "CTF Planning Tool - demo of reporting - BS Cashflow and CFO Scorecard" (11:00-11:35; Vivian, Ivy, Dennis, Arthur, Jay, Elsie, user; rescheduled from 26 Oct because of interim report)
- [stated] user sent key-takeaways email + CN minutes "Planning_Tool_Reporting_MoM_CN" (3 items: Excel solution for CFO scorecard and P&L; monthly BS/CF export and CF name check; CF opening balance and currency realignment — CF details in [[planning-tool-bs-cf-review]])
- [stated] BS report: key metrics on top, collapsible; default view is full year; BS figures are month-end balances, full-year column must not sum months; monthly view via copy-to-personal report and changing time span
- [stated] shared reports sit in a shared folder (development now, production later); users can't edit the template, copy it to personal reports where they can change layout, time span, column width; data stays linked
- [stated] Ivy: nobody will review numbers with Karen in Workday — every team needs an Excel solution from system output; the system is the source of truth / record keeping until Phase 2
- [stated] CFO scorecard approach changed: instead of the OfficeConnect layout, Dennis provides a transaction-style raw data dump and Frank builds SUMIFS mapping into the scorecard; Yetta will operate it; Frank got a Workday account on 2 Nov; structure needs manual expansion due to time-dimension limits
- [stated] P&L for Karen: Dennis + Yetta to assess linking an OfficeConnect report vs export-and-map; final approach TBC
- [stated] ACTION user: regroup with Dennis, Frank, Yetta and give Ivy a step-by-step timeline (download, mapping, populate, refresh) — must be proven before UAT sign-off
- [stated] ACTION Dennis: send monthly BS/CF export samples to Jay (not Arthur, busy) so Jay can rework his reporting files in December
````

### 02 Planning Tool · areas/planning-tool-uat-golive.md

- 原始路径：`/projects/01a14710-8d0b-719f-888a-766abd27def7/areas/planning-tool-uat-golive.md`
- updated (UTC)：2026-11-06T04:24:59Z

````markdown
---
name: planning-tool-uat-golive
description: CTF Planning Tool (Workday Adaptive, vendor Novus) Phase 1 UAT plan, go-live plan, training approach and Phase 2 scope — from the 2026-10-20 UAT & Go-Live discussion
sources: [cowork]
aliases: [Planning Tool UAT, Go Live, UAT 与上线, WAP Phase 1 UAT]
---

## Context
- [stated] Planning Tool is built on Workday Adaptive Planning; implementation partner Novus ([[dennis]] lead consultant, Andy on vendor side, Isaac also on Novus team); Lydia from CTF IT
- [stated] user (Samson) prepared the first UAT topics list; Dennis reformatted it into "WAP_Phase1_UAT_Topics" (19 topics)
- [stated] Phase 1 go-live results go to Patrick and Karen; Vivian must align UAT plan, go-live checklist and scope with Novus before presenting to them

## 2026-10-20 meeting "CTF Planning Tool - discussion on UAT topics" (Teams, 9:00-10:00)
- [stated] organiser: Vivian Lau Man Ming (CTFHK-劉敏明); attendees: Ivy Cheng (CTFHK-鄭凱因), Andy Wu (Novus), Dennis Chen (Novus), Elsie Wong Ching Yin (CTFHK-黃靖燕), Sun Yang (CTFCN-孙洋, "Samson"); cc: Li Miao Dan (CTFCN-李妙丹, ICC 资讯及通讯应用中心), Lydia Wu Ho Yan (CTFSG-胡可欣, IT)
- [stated] agenda: UAT topics & timeline; go-live checklist (tentative); scope list review (tentative)

## UAT topics (19, 3 categories)
- [stated] Foundations & Controls (01-08, pre-UAT setup by project team): org structure/levels (re-review before UAT, many changes to market structure), user access by user groups (not roles; e.g. China P&L, HQ), data entry & template uploads, version management (actuals overlay, virtual version for FX impact, dev/test/prod version folders), submission & staged locking (lock users within a market by user group), FX & gold price assumptions (pre-load before UAT), dimensions (e.g. CAPEX project list), dummy data
- [stated] Business Modules (09-17): store count/concept, topline (RSV/qty/ASP), SSSG, Signature Collection, COGS/GP/NOP-to-NP, SG&A incl. HC, A&P, Prof Fee, IT spend, CAPEX/depreciation/payment plans, inventory & OTB (may relate to DSC project), BS/cash flow/KPI scorecard
- [stated] Consolidation & E2E (18-19): group consolidation/eliminations/reconciliation; management reporting & version comparison
- [stated] International not tested separately — same set-up as Hong Kong (different entity); if HK, China, HQ pass, International assumed fine; Samson may act as International user. International will later split into regions (USA, Taiwan…), Flora's team, Phase 2

## UAT approach & timeline
- [stated] Novus internal testing weeks of 2 Nov and 9 Nov; UAT targeted from mid-Nov (week of 16 Nov); all fixes and sign-off by 30 Nov
- [stated] HQ FP&A busy 16-18 Nov (rolling forecast presentation to Karen on 18 Nov) → flip order: mini sessions + BS/cash flow + inventory before ~15 Nov; P&L end-to-end ~20 Nov after P&L finalised
- [stated] prefer several mini sessions (e.g. access control, A&P/CAPEX templates) + one physical end-to-end session, rather than 2 intensive days; Dennis willing to be on site in HK ~1 week; Novus to bring a second person
- [stated] Lydia suggested agile/staggered delivery: release modules that pass internal QC early for user testing
- [stated] Novus writes scenario list → FP&A validates → Novus writes scripts (reuse previous script format); FP&A will not review scripts within a day
- [stated] consider using FY26 actuals + FY26 budget as UAT data so it can be copied to production (avoid reloading); otherwise dummy data and load production dimension lists before go-live
- [stated] SSO not needed for UAT (temporary passwords); separate short session with IT/Novus to test SSO before go-live
- [stated] UAT venue is KC — Vivian must book rooms once dates fixed; IT to name on-site helpdesk backup
- [stated] Samson may need to travel to HK to support UAT and should sit with China team to learn their forecast process
- [stated] China key testers ~3 people (P&L submitter, Shenzhen inventory person); Shenzhen can join remotely
- [stated] user (Sampson) is drafting the UAT acceptance criteria Excel; shared with Dennis 2026-10-23; after 2026-10-27 discussion with Vivian, points-deduction dropped — severity is Critical / High / Low only (Medium merged into High), go-live needs 0 open Critical and High and fewer than 3 open Low per module (per Ivy); testers just describe issues, FS team + Dennis classify
- [stated] 2026-10-27 1:1 with Vivian on the criteria: Critical = system logic wrong / control fails (e.g. locked data can still be changed); High = wrong numbers or function fails (upload not shown/saved, totals or % wrong); Low = cosmetic only (labels, font/column size, colours differ from agreed, typos e.g. NGP vs agreed name, error message not naming the failing row); Vivian asked to spell out examples concretely (e.g. "user uploads 10 then 0, system still keeps 10") so Dennis understands
- [stated] check in UAT: user-changed column widths should persist (system default otherwise)
- [stated] issue categories: logic/configuration, upload/template, calculation, submission, performance/platform stability, report & presentation; non-system: out of Phase 1 scope (→ Phase 2), data issue (test/master data wrong — CTF's responsibility, Finance corrects and retests), training/user error, test script error (retest), duplicate / same root cause
- [stated] extra scenarios raised by users on the spot during UAT may be added and are classified with the same criteria
- [stated] UAT training for participants planned 17 Nov; Vivian has a clashing meeting (~10:50) and asked user to attend for her; main UAT days 18-19 Nov, 20 Nov half-day spare; Vivian wants user on site but AI SF requirements work takes priority
- [stated] signed-off templates can still get non-fundamental (cosmetic) changes from user feedback; the "signed-off templates will not be reworked" wording is to be dropped from the mapping document; user guidance on template fields belongs in Dennis's training material, not a separate sheet
- [stated] version-management UAT cases (Ivy, 2026-10-27; Vivian to add, Dennis to support): create 1B as copy of 1A and change only one market / one item by partial upload or entry — other markets and untouched templates (P&L, A&P, Inventory…) must equal 1A; FX-only change: market local-currency figures unchanged, only group translation, CF translation and currency realignment change; create a new version from an older one (e.g. 1A content into 1H) and restore older content into an existing version
- [stated] report-permission UAT cases (Vivian via Teams chat, 2026-10-30; user agreed to capture): users can only COPY a report from the Shared folder to their Personal folder, not MOVE it out — shared reports must not suddenly disappear; also test whether users can change the format in a shared report
## 2026-11-02 UAT discussion (11:36-12:32; Ivy, Dennis, user, Vivian and Elsie joined late) — CN minutes "Planning_Tool_UAT_MoM_CN_20261102"
- [stated] Ivy's sign-off precondition (not a UAT script, but required before UAT sign-off): every team (market P&L, inventory, OTB, cash flow, collections…) must confirm it can download final system output and turn it into its Karen review file / scorecard in minutes, not hours — otherwise markets will keep working offline and only upload at the end; must happen in November (December busy, Dennis not on site at Christmas)
- [stated] Dennis: Workday reports are user-configurable (unlike Anaplan's fixed templates); users copy shared report to personal, change time span (e.g. to month), export; there is also a pure data-export page (pick account, dimension, level); he will give sample exports before UAT and build usage into the UAT sessions
- [stated] Dennis's functional topic list: common — submit, submit with 0 (a 0 overwrites existing value; blank does not), drill-down, review/copy report, export; store count by concept variance vs store type; SSSG quarter/half/full-year submitted separately; Signature Collection balancing (formula); revenue/COGS mix; SG&A and other expenses; NOP-to-NP flow at group level only (copy finance team's NOP as baseline); market eliminations needed or China total is inflated by retail/wholesale; OTB/BS/CF mainly submit + key metrics
- [stated] CAPEX cases: add new dimension values on import (two test accounts, one for Wu Qi with create rights); override vs incremental import; copy version as carry-forward; capex actuals/depreciation actuals not in Phase 1; payment override is per payment batch (move month, %, amount — e.g. move March payment to Feb) not month-by-month re-spread; project total must balance; zero allowed (e.g. project dropped), negative rejected on entry and on upload; audit trail; market lock
- [stated] inventory 100K: test total vs 100K vs balancing figure; negative balancing figure highlighted (yellow background preferred) in report — warning only, no input block; same for Signature Collection
- [stated] FX change must be tested across P&L, cash flow and inventory templates
- [stated] sandbox: Ivy wants forecast base + adjustment = outlook (e.g. 100 + 3 = 103) for main lines (RSV, REV, NGP), not by category; Workday scenarios don't work that way (needs adjustment accounts); low priority — not a Phase 1 go-live deliverable, assess after go-live / Phase 2; Ivy keeps Excel meanwhile
- [stated] scenario process: Dennis sends functional list 3-4 Nov; user reviews first, then one meeting with Ivy, Vivian, Elsie, time-slotted by module — P&L/Topline Aaron + Yetta, cash flow Arthur, inventory Zoe, Vicky, Nana; return to Dennis by end of Fri 6 Nov so he can write scripts with expected outcomes; Vivian to update a week-by-week task/owner timeline incl. download validation at next regroup
- [stated] CAPEX UAT ~10 Nov; Dennis's CAPEX scenario list due 28-29 Oct, reviewed by user with Wu Qi then Ivy/Vivian before scripts — details in [[planning-tool-capex-template]]
## Email thread "Preliminary Discussion on Planning Tool phase 1 UAT" (19-28 Oct, user / Vivian / Dennis)
- [stated] 19 Oct pre-meeting (user + Dennis) takeaways: prioritise core Phase 1 functions; prerequisites = user access, time dimension, separate test version, Level hierarchy review; market locking via user-group write permission; test data = business-approved real or sanitised data, users upload forecast themselves, Novus may preload budget, handling of sensitive actuals TBC; keep system-required sheet/field names, guidance on Instructions sheet; Excel for scripts/issues/screenshots (reuse SBUX script template); acceptance criteria then not yet agreed
- [stated] 21 Oct Ivy's revised timeline (agreed by Dennis 22 Oct): Novus internal testing 2-6 Nov; UAT prep 9-13 Nov (P&L scripts 11-13 Nov; markets' P&L submission 13 Nov); 10 Nov online UAT session = CAPEX; Ivy pulls RF P&L review with Karen forward to 16 Nov; 17 Nov inventory market submission; 18 Nov RF review with Karen; UAT on site 18 Nov (9-12 Topline & P&L, 14-15 P&L cont., 15-16:30 NOP to NP, 16:30-18 P&L KPI) and 19 Nov (9-12 Inventory/OTB, 14-15 cont., 15-16:30 SG&A / Other Expenses, 16:30-18 CF/BS & Key Metrics); 20 Nov morning buffer, inventory review with Karen; 23-26 Nov users very busy, Novus fixes issue log; 27 Nov review after fixes; 3 Dec target UAT sign-off; 4 Dec SSO setup (Novus + ICC) and go-live prep; deployment from 7 Dec (instance unavailable 4-7 business days)
- [stated] each UAT session includes a 30-min "how to" brief training; Dennis flies to HK around the on-site sessions
- [stated] post go-live calendar in that thread (before the 26 Oct change to 8 Jan): end-user training 29 Dec; topline submission 6-8 Jan with on-site support; FY28 topline review with Karen 11 Jan; full P&L market submission 20 Jan, inventory market submission 22 Jan, on-site support 19-22 Jan; budget review with Karen (full P&L, BS, CF) 27-29 Jan
- [stated] Dennis's UAT vs go-live checklist: UAT general settings (user access, time, create budget/forecast version, level structure), scenario FX impact, functions (import template, input erase, actual overlay, lock by level), data (dummy actual, FX rate, previous budget if needed), dimensions, functional areas (P&L, BS/CF…); go-live = production version setting, ask WAP support to clone as production instance (4-7 business days)
- [stated] 22 Oct Dennis: cost centers already loaded with user's help; remaining master data to finalise: Department (CAPEX), Store Concept (store count), COA accounts (A&P and Prof Fee entries; users can't create on import), IT Type of CAPEX, IT Project Type, IT Expense Type, CAPEX Project List; dimensions that change often or have a single owner can be opened so users create values on import
- [stated] time labels: Dennis proposed months 04-2025, quarters 1Q-2026, halves 1H-2026, FY26; 28 Oct Vivian asked to standardise "FY26" for fiscal year and plain year for calendar — rename to 1H-FY26, 1Q-FY26; months stay calendar (04-2025 = Apr 2025); FY26 = Apr 2025-Mar 2026
## Official UAT announcement — Vivian's email 23 Oct 2026 "Planning Tool UAT timeline and participants list (Nov 17 Training / Nov 18-19 UAT)" (supersedes the 22 Oct session split)
- [stated] to testers + Dennis, cc Ivy, Anita, Liu Yanzun, Anthony Lai, Elsie, Flora, Andy; framed Phase 1 as a centralised web-based platform for Topline, P&L, Expenses, Inventories, B/S and Cashflow submission for FY28 Budget and Forecast cycles
- [stated] Novus provides scenarios and steps; testers run assigned scenarios, report issues, confirm functions are fit for business use; meeting invites to follow
- [stated] online: Capex UAT Nov 10 (Tue) 10:00-12:00 — Wu Qi (gets a quick 30-min training first); training for all testers Nov 17 (Tue) 10:00-11:00
- [stated] in person, HK KC office 24/F — Nov 18 (Wed): 9:30-11:30 Topline — Rita 张晶 (CN), Zoe (HKM), user (International), Yetta (Group/consolidation); 9:30-11:30 in parallel Expense Templates — Cheng Dan 程丹 + Jin Xin 金欣 (CN), Ben Hui 許畝誠 (HKM), user (HQ); 13:30-18:00 P&L, COGS, SG&A, Other Income, P&L KPI — Cheng Dan + Jin Xin (CN), Ben (HKM), user (International), Yetta (HQ & Group consolidation)
- [stated] Nov 19 (Thu): 9:30-13:00 Inventory and OTB — Shen Na (CN inventory), Zoe (HKM inventory), Vicky Cui 崔霞 (Group inventory), Lu Zhuojun 陆卓君 (OTB); 14:30-16:00 P&L group consolidation, NOP to NP — Yetta (Group), Arthur (HQ); 16:00-18:00 B/S, Cashflow & Key metrics — Arthur
- [stated] user is a tester in three Nov 18 slots (Topline for International, Expense Templates for HQ, P&L for International)
- [stated] (update 2026-11-05) Cheng Dan 程丹 is not taking part in UAT — leave her name out of tester lists; CN expense / P&L testing is Jin Xin
- [stated] ACTION: Vivian + Dennis to send an email with concrete dates in calendar form (mini-session days, E2E days, script return date, FP&A confirmation dates, tester list deadline) — not a vague "3-week" format

## Status update deck "Planning Tool Status Update & Go-Live Criteria" (v3, file dated 261028, presentation dated 3 Nov 2026)
- [stated] agenda: Phase 1 deliverable; Jun-Oct status; Nov-Dec timeline; align go-live criteria; Phase 1 & 2 scope change vs RFP; Phase 2 next steps
- [stated] Phase 1 benefits for FY28 Budget: single platform with version control; standardised input templates (FP&A uploads collected BU data); FY26 actuals and FY27 9+3 forecast pre-uploaded; automated consolidation, cross-template checks, automated CFO scorecard; P&L drill-down and sandbox for sensitivity
- [stated] milestones: 14 Jun SI (Novus) contract signed; 16-17 Jun kick-off; 29 Jul Workday Adaptive subscription signed; 6 Aug requirements signed off; 17 Aug design signed off; Sep build/demos; Oct reporting review; tentative sign-off of all demos by 3 Nov
- [stated] deck timeline: Nov 2-6 Novus internal testing; Nov 10 CAPEX UAT; Nov 17 online tester training; Nov 18-19 on-site UAT HK; Nov 23-27 fixes and review; Dec 3 target UAT sign-off; Dec 4 SSO setup (ICC) + go-live prep; Dec 7-18 deployment window; Dec 18 end-user training; Dec 21 confirm project go-live (email sign-off); Dec 30 end-user refresher training; Jan 5-8 topline submission and Jan 19-22 P&L, Inventories, BS and CF submission, both with Novus on-site support
- [stated] 5 proposed go-live readiness checks (to complete before go-live Dec 21): 01 UAT completion per subject (Foundations, Store Count, Topline, Expenses, Capex, Inventory & OTB, Balance Sheet, Cashflow, Consolidation and Reporting) with open issues having agreed treatment; 02 master data completeness (COA for A&P & PF, departments, cost centers, expense filters); 03 historical data (FY26 actual, FY27 9+3 prelim forecast); 04 training preparation; 05 user accounts and SSO tested before go-live; appendix: no Critical or High unresolved, max 3 Low per subject
- [stated] Phase 1 out-of-scope additions: A&P detail, IT Spend detail, Prof Fee detail included free of charge; IFRS 18 P&L for FY28 Budget in Phase 1 — preliminary max 10 man-days / HKD 40K off-site, pending pro-forma early Dec; SG&A templates in Phase 1 for submission & version control, to be enhanced in Phase 2 without CR
- [stated] Phase 2 items outside RFP: #1 three-vendor (AI SF / DSC o9 / PBI) integration design meeting late Nov-early Dec, Novus T&M HKD 40K funded from AI SF budget; store-level P&L; actual data integration (Lucanet, SAP); DSC o9 integration (AI SF integration was in scope, o9 was not); approved-budget push to SAP/EAS; scorecard for markets; inventories by brand / store concept and "above HKD 100K" input logic; 3-5-year strategic plan
- [stated] Phase 2 next steps: COA clean-up for ID SAP roll-out and IFRS 18; FY29 budget workshop in Feb (cross-functional, process re-engineering, one set of assumptions, possibly non-finance users); Phase 1 hypercare Jan-Mar 2027; Phase 2 capex approval end Feb-early Mar (Novus original Phase 2 quote HKD 1.7M per RFP, excl. additions); Phase 2 kick-off 1 Apr 2027; AI SF expected live ~Aug 2027
- [stated] Phase 1 spend: implementation budget HKD 1.35M vs actual 1.18M + 0.04M IFRS 18 CR = 1.22M; licence budget 0.40M vs ~0.30M (Aug 2026-Jul 2027); maintenance 0.135M (Apr 2027-Mar 2028, FY28 budget); total ~HKD 0.23M below budget

## Go-live
- [stated] FY27 9+3 done offline, loaded into system during quiet Christmas weeks as the FY28 base
- [stated] first go-live milestone: first week of Jan 2027 — actualise Dec topline and load FY28 topline for the topline review with Karen; if the system can't consolidate topline for that review it's a fail
- [stated] (update 2026-10-26) Karen unavailable 11-12 Jan → topline review moved to 8 Jan 2027; topline submission starts 5 Jan; 4 Jan is buffer
- [stated] end-user training locked 29 Dec (mainly HK users); Ivy suggests a second session before Christmas (18 Dec afternoon only, or 21/22 Dec, not 24 Dec) so people on leave can pick one; Dennis to propose; deployment needs ~4-7 days
- [stated] before go-live: reports and CFO scorecard complete, UAT passed, training done, master data loaded → sponsor sign-off (Karen, Patrick) by email since they'll be on leave; Vivian to tell them this week; Vivian to ask Lydia what go-live documentation / user announcement CTF requires (Ivy: Starbucks used the official go-live email as milestone evidence); formal go-live date still TBC
- [stated] Ivy flagged: Vivian to check with Lydia whether Novus time-and-material work in November (no contract yet) needs a supplement contract or PO
- [stated] Novus to provide someone physically on site in HQ that week (not necessarily Dennis); Andy on standby
- [stated] go-live checklist items: UAT acceptance tolerance, master data completeness (dimensions, COA, entities), training, user accounts, SSO
- [stated] go-live with a small user group (one uploader per market/team, incl. someone from SCM via Elsie), then expand for the next rolling forecast

## Training
- [stated] Dennis (not Isaac) must deliver UAT training and official training
- [stated] Phase 1 users mainly use 2 pages: dashboard and integration (template import) + login
- [stated] split training by audience (P&L/templates vs inventory/cash flow — e.g. Arthur, Jake for cash flow; inventory group), like the earlier Anaplan training; record sessions and provide screenshot manual
- [stated] two rounds: go-live training for core uploaders, then full end-user training later

## Phase 2 / out of scope
- [stated] change-request supplement contract not yet signed; Dennis and Vivian each keep an out-of-scope list
- [stated] Phase 2 candidates: 3-year strat plan (Novus did some for free — mention to Patrick & Karen), RSA team, store-level P&L, AI sales forecast, automation/elimination, actual data & data integration (DSC, SAP…), approved budget
- [stated] ACTION: Andy to give high-level ballpark cost for the additional items (beyond original RFQ) for expectation management with Patrick & Karen
- [stated] user (Samson) is building the Planning Tool data-source mapping & automation roadmap for Phase 2 integration estimates — Workday accounts split into Actual source vs Forecast logic by system; going with P&L + Inventory first, BS/CF later
- [stated] 2026-10-27: user refined the mapping template (with AI help) into separate Phase 1 / Phase 2 overview and Actual vs Forecast sections; Vivian: gold price assumption input is by month; Phase 1 = all templates loaded manually, go-live target end of December

## 2026-11-05 UAT scenario discussion (Ivy, Vivian, user; 15:57-17:02) and scenario workbook v1.8
- [stated] Ivy: v1.5 list was functionality, not scenarios — she wants real-life "what happens if" cases (numbers keep changing, past Excel errors); Dennis's scripts must state the expected system result; split functional checks across markets (one tester per check), only E2E needs every market (markets submit, Yetta consolidates); scripts separate functional vs E2E
- [stated] Ivy: response time matters to Karen — time NGP calculation and group consolidation; group consolidation over 1 minute = fail
- [stated] Ivy: where Workday can't block/warn (store concept not tying to store count, negative Signature Collection balancing, A&P detail vs P&L), Dennis states actual behaviour → known limitation + user training, not a design defect
- [stated] Ivy: no UAT sign-off until downloads are usable — A&P / Prof Fee upload = download, CFO Scorecard downloadable in Frank's format (after Frank gives it to Issac), download time recorded; how teams link downloads into their own Excel is ongoing, not a UAT script
- [stated] Ivy's E2E/business scenarios: store opening/closure without updating concept (concept is a month-end breakdown, doesn't roll); business model change must not change concept; RSV change with quantity fixed → ASP; negative forecast quantity; RSV without quantity / quantity without RSV (diamond vs jade); SSSG RSV/qty ≤ topline (no quarter = sum-of-months check — CTF SSSG is point-in-time); Signature Collection 100m vs RSV 120m→90m; revenue without COGS (service fee may be 0); FX-only change incl. currency realignment; reopen one market only; consolidate with unfixed errors and drill down to the market; China retail/wholesale elimination (120/100 → 150/100); SG&A % moves when revenue changes; clear-out before new cycle; actualisation 2+10 → 3+9 then Final (test with SG&A); correction after Final (210 vs 201); NOP→NP finance-cost update after cash flow (version naming 1A/1B); SG&A change flows through to NP; inventory FX / gold price / COGS change → turnover; cash flow gold price & FX resubmit; OTB cases to be collected from Elsie / Lu Zhuojun
- [stated] user's instruction for these files: E2E/business scenarios must only contain what Ivy raised — no made-up additions; testers assigned to match their own module per the 23 Oct session table
- [stated] final workbook "Planning_Tool_UAT_Scenarios_v1.8" (EN + CN, same content): 1 Framework; 2 Scenario List (75 functional checks FD/CS/SC/TL/PL/NP/GC/BC/IN/OT/AP/CX/CR, one proposed tester each, remark column empty); 3 Ivy Comments & E2E (A requirements, B E2E-01–13, C BIZ-01–16); 4 Tester & Access (Cheng Dan removed)
- [stated] v1.8 added BIZ-16: group views for HJ (High Jewellery), eCom and HOF — same version/period, roll up separately and reconcile to market data, change one input and re-consolidate; Yetta + relevant market users (TBC), Dennis supports mapping
- [stated] open points at v1.8: E2E-11 COGS change assigned to Jin Xin but she is only scheduled 18 Nov (inventory session is 19 Nov); Tang Jin Ke kept for CAPEX normal-user test though not in the session table
## 2026-11-06 scenario walkthroughs with testers
- [stated] user walked testers through the UAT scenarios on 6 Nov and asked them to send any additional scenarios to him by email / Teams by end of day Wed 11 Nov; Novus then writes detailed test scripts from the agreed scenarios, and the detailed test list with steps goes to testers before UAT
````

### 02 Planning Tool · areas/planning-tool.md

- 原始路径：`/projects/01a14710-8d0b-719f-888a-766abd27def7/areas/planning-tool.md`
- updated (UTC)：2026-11-09T01:51:41Z

````markdown
---
name: planning-tool
description: Project copy — Planning Tool phase framing, Workday account structure export and the modeled-sheet (template) dimension list (read with the account-level planning-tool file)
sources: [cowork]
aliases: [PT, Planning Tool, Workday Adaptive, WAP, Workday Account Structure, Modeled sheet dimensions]
---

- [stated] Planning Tool has only Phase 1 and Phase 2 — do not frame work in End State v4's Phase 2.5 / 3 / 3.5; items not yet decided are "whether to include in Phase 2 (TBD)"

## Workday Account Structure (export by Dennis, 22 Oct 2026; user shared 9 Nov)
- [stated] ~370 rows: Name | Rolls Up To | Display As | Default Formula; blank Display As = "Group" (only groups accounts, system does NOT sum children); an account can be the child of another account, then it does roll up
- [stated] top groups under Custom: Rolling_Forecast_P&L (Store Concept, Store Count by store type, Topline RSV/Qty/ASP = RSV÷Qty, SSSG CY/Base, Net Gross Profit — Revenue, COGS, NGP excl. gold price impact = Revenue − COGS, SG&A, Other income, Reported GP & OP with gold price fluctuation — RGP, Reported OP, PBT, Taxation, Profit for the period, ROP margin; NOP, NGP, NOP minus interest expense); Gold Price Assumption (weighted average, normalised); Custom Cash Flow; Custom Balance Sheet; BS Key Metrics; Margin % (SG&A as % of revenue by expense type); Inventories (value, qty, OTB FG / RM gold kg × normalised gold price / RM non-gold, inventory supplement — gold balance kg, gold loan balance kg, self-op + consignment store count); Signature Collection accounts (storage RSV, RSV mix %)
- [stated] Custom Cash Flow in this export is still the older layout: opening (= prior-month closing), (i) inflows A Revenue / B Other receipts, (ii) outflows C Purchase / D SG&A / E Other payments, (iii) other F Store count impact - Franchise / G Others, closing — predates the revised direct-method A-J template and the 2 Nov opening-balance split
- [stated] Custom Balance Sheet accounts: non-current assets (PPE prepayment & rental deposit, others); current assets (cash, AR CN, AR HKM&O, other receivables, inventory, others); liabilities (AP CN, AP HKM&O, other payables, bank loan CN/HK, gold loan CN/HK, convertible bond, bond 1-3, lease liabilities, taxation payable, others); equities
- [stated] BS key metrics: cash balance (PRC/HKM), bank borrowing, bank loan facility & utilisation, gold loan, gold loan facility & utilisation, total loan utilisation, CB, bonds 1-3, net debt (bank borrowing + gold loan + CB + bonds), inventory balance, F-gold weight (kg), hedging ratio (metrics use iff(hedging ratio ≠ 0)), gearing = net debt ÷ equities, CCC = DSO + DII − DPO
- [stated] file footer: "Confidential Information. Do not distribute without permission."

## Modeled sheet dimensions (template field list)
- [stated] field types: Level (market/entity + cost center, see Level Hierarchy), Dimension (maintained list in system, restricts input, usable for pivot analysis), Text, Number, Value Lookup (e.g. level currency, system populated)
- [stated] CAPEX (Store): Level Code, Tag Name, Depreciation Type (SG&A or Manufacturing/COGS), Type of capex, Project Status (Approved/Budgeted/Delete), Store Name & Store Code (text), Store CAPEX Nature (Self-op/MSA/Consignment/Wholesale), Store Concept, Level Currency
- [stated] CAPEX (IT): Level Code, New/Carried over, Department (HR/ICC/Finance/E-commerce), Project Type, Category (new project / carried-forward / new routine / existing routine…)
- [stated] CAPEX (Office/PSC): Level Code, District (HQ HK/PRC, CN 4 regions, ID SG/TW/MY/AU), Project Type
- [stated] A&P: Level Code, A&P Department (品牌/HJ/地區/電商/總務…), Nature (Digital/PR/Tmall…), Budget Tiers (T0/T1/T2…), Budget Projects (names from Aaron), plus source text fields Dept (Source)部门, 科室, Type, Project, 主項目, 子項目 — their mapping to dimensions still marked with "?" in the sheet; Level Currency; Target (number)
- [stated] Professional Fee: Level Code, Department (歷史及文化管理部…), 項目名稱 (dimension), Project Description, 項目負責人 (text), 會計科目 (dimension, e.g. 其他諮詢費), Level Currency
- [stated] tabs Level Hierarchy, A&P Dimension, Type of CAPEX hold images only
````

### 02 Planning Tool · topics/ctf-business-glossary.md

- 原始路径：`/projects/01a14710-8d0b-719f-888a-766abd27def7/topics/ctf-business-glossary.md`
- updated (UTC)：2026-10-27T02:49:56Z

````markdown
---
name: ctf-business-glossary
description: Project copy — CTF business terms clarified in Planning Tool conversations (read with the account-level glossary)
sources: [cowork]
---

- [stated] A单 (A-Dan) = PR / budget approval stage (when budget is locked); R单 (R-Dan) = PO — per Vivian 2026-10-27
````

### 02 Planning Tool · people/dennis.md

- 原始路径：`/projects/01a14710-8d0b-719f-888a-766abd27def7/people/dennis.md`
- updated (UTC)：2026-10-20T02:17:50Z

````markdown
---
name: dennis
description: Dennis — Novus lead consultant on the CTF Planning Tool (Workday Adaptive) implementation
sources: [cowork]
aliases: [Dennis, Novus consultant]
---

- [stated] Novus consultant leading Planning Tool build, UAT scripts and training; works with [[vivian]] on UAT schedule — see [[planning-tool-uat-golive]]
- [stated] FP&A insists Dennis (not Isaac) delivers UAT and official training; previously delivered a well-received split-session Anaplan training
````

### 02 Planning Tool · people/wu-qi.md

- 原始路径：`/projects/01a14710-8d0b-719f-888a-766abd27def7/people/wu-qi.md`
- updated (UTC)：2026-10-26T05:08:47Z

````markdown
---
name: wu-qi
description: Wu Qi (伍琦) — CTF China colleague who owns IT CAPEX input for the Planning Tool and its CAPEX UAT
sources: [cowork]
aliases: [Wu Qi, 伍琦, 武琪, 武奇, 穆奇]
---

- [stated] Wu Qi (CTFCN-伍琦), IT CAPEX user/owner for the Planning Tool; often transcribed as 武琪/武奇/穆奇
- [stated] 2026-10-26 judged the IT CAPEX template fields sufficient for Phase 1 manual upload; wants a system-function dimension (Finance/Operations/HR) and room to change fields in Phase 2 — see [[planning-tool-capex-template]]
- [stated] reviews CAPEX UAT scenarios with the user first, then executes UAT (~10 Nov)
````


---

## Part B · 项目：03 DSC Project

- 记忆文件夹：`/projects/01a14711-18cb-7340-b9c6-ba609c01c468/`

### 03 DSC Project · areas/dsc-project.md

- 原始路径：`/projects/01a14711-18cb-7340-b9c6-ba609c01c468/areas/dsc-project.md`
- updated (UTC)：2026-11-09T08:45:28Z

````markdown
---
name: dsc-project
description: User's involvement in the DSC project (MFP/OTB) — read for any DSC UAT or project work
sources: [cowork]
aliases: [DSC, DSC项目, MFP/OTB]
---

- [stated] preparing the finance-side UAT for the DSC project (MFP/OTB module): test scenarios, UAT success criteria and a tracker for issues finance users hit in testing

## PMO 进展更新（截至 10/23，任波 Ren Bo 发，10/25 邮件；用户在抄送）
- [stated] 总体 🟢、整体可控；MFP/OTB UAT 65% 🟢；AP 组货计划 详细设计 90% 🟡（落后，拟本月追上计划）；DP 需求计划 开发配置 29% 🟢；数据集成 配置/开发 90% 🟢
- [stated] MFP/OTB：项目组已完成过渡期手工上传模板及操作方式设计，开始与业务沟通，后续按测试反馈完善流程和指引
- [stated] 计划：MFP/OTB 11 月中下旬完成 UAT，随后做上线前历史数据初始化和用户权限设置，OTB Dashboard 同步上线（较 10/15 o9 说的"10 月底前完成 UAT"已后移）；AP、DP 11 月完成开发配置
- [stated] AP：门店分群采用"商圈等级 × 销售等级 × 门店 ASP 等级 × 门店形象"四维标签；运营模型与新品规划在最终确认；ROS 计算方向已明确，待结合不同历史期间及中模状态分析验证
- [stated] DP：o9 外籍数据科学家团队参与，已出首版基准预测，进入验证与迭代，下一步引入促销等驱动因素
- [stated] 11/04 第六次 DSC 项目指导委员会会议将进一步汇报；收件人含 Karen Yih、Patrick Cheung、Ivy Cheng、Elsie、孙方雨、o9 Kai Xu 等，Vivian、用户在抄送

## 10/29 MFP/OTB 业务周例会（o9 Ying Zhang 纪要 + 例会 PPT + UAT 问题清单 v20261029）
### 计划与签收
- [stated] 时间线：11/06 前完成 UAT 及问题处理（11/06 UAT 总结）→ 11/13 前业务确认及 UAT Sign-off → 11/18 Go/No-Go → 11/27–11/30 切换上线，目标 11 月底技术上线；11/04 SteerCo 前持续更新进展
- [stated] Release 1 UAT 范围：MFP 年度及滚动、成品 OTB 年度及滚动（含 1.6 财务视角成品 OTB 滚动——之前工作簿与 10/15 邮件的冲突至此按"在范围内"处理）；原料 OTB 不在 Release 1
- [stated] UAT 签收人（PPT）：Elsie（集团财务总监，财务规划关键用户）、Brenda（集团商品零售规划总监）、军爷（资讯及通讯应用 AVP，PPT 标为 DSC 项目经理）
- [stated] 签收依据：测试范围、测试脚本完整度、测试结果通过度、缺陷优先级和解决度（P1/P2 上线前须关闭）、无法上线前实现的新需求要给优先级和方案计划
- [stated] 优先级定义：P1 严重/P2 重要 = 阻断性缺陷，上线前必须关闭；P3 一般、P4 轻微 = 上线前尽量解决、澄清，或与 CTF 对齐预计解决时间
### UAT 问题状态（截至 10/29）
- [stated] 共 71 条，Closed 44（62%），未关闭 27：WIP 12、Pending Discussion 7、Open 5、ADO 3；PPT 口径总体解决 63.2%（P2 45.45%、P3 64.1%、P4 61.9%）；无 P1
- [stated] 未关闭类型：用户友好 13、问题澄清 6、CR 4、数据 3、产品 bug 1（PPT 的占比列有误：bug 写成 34%）
- [stated] 未关闭的 P2：Rita 财务目标上传部分成功、展板未同步（数据问题，ADO，due 11/13）；上传失败明细下载为空（产品 bug，ADO，未指派）；OTB 牌面价法 vs 成本价法（Pending）；加盟批发库存口径（Pending，需求待明确）；选市场后区域下拉框未过滤（Open，due 11/30）；On Order 取 RO 还是 PO（WIP，辉哥，due 11/30）
- [stated] 多条 WIP/CR 需与 DP 对齐需求（回仓计划、Bottom-up OTB 复制到 Top-down 模拟、DP 买货件数周转、中模回仓建议、HJ 标签），due 11/30，即晚于 11/13 签收
### 业务逻辑结论（10/29）
- [stated] 加盟批发库存：财务周转目标不含加盟批发商库存，但 OTB 仍要考虑其买货需求；口径和周转对比方式在 UAT 中继续验证
- [stated] ASP/Unit：老系列计划 ASP，按 RSV 反算 Unit（Elsie 10/29 确认）；市场有不同假设可用 Scenario 调 RSV 或 ASP
- [stated] 预测金价：集团统一提供，暂由 Rita 上传，按月维护，同月各周用同一金价（Rita 原建议由 HK 上传，未采纳）
- [stated] RO/PO 差异：辉哥 10/19 主张 RO 一周内发出、未来不考虑 RO；军爷 10/22 建议取 PO 并推动流程变革；Elsie 10/29 认为流程变革短期难实现，要求 Plan B 和风险管控——o9 负责把 Elsie 的担忧反馈给 CTF 项目组并讨论备选方案
- [stated] OTB 计算：继续对比牌面价法与成本价法在各系列和重点业务分类的差异，重点评估对 F 类 OTB 预算的影响（o9 & 元凤）后定方案
- [stated] 多币种：CN 用 CNY、港澳及海外用 HKD 计划，集团统一转 HKD 汇总；PPT 列方案 A（统一 HKD 上传）和方案 B（本地币计划、提交后转换），未定；待答：哪些数据要转换、CN 历史按历史汇率还是计划汇率、谁触发转换；Rita/沈娜 10/23：集团审核 CN 目标用 CNY
- [stated] 用户权限：o9 给出初版方案（Finance/Merch/OTB/Group Planner 等角色），待业务反馈；未定问题：Production Lead Time 是否由 Production Planner 维护，WOC、成本率等关键参数是否限定特定人修改
- [stated] 其他已关闭澄清：管理层建议打和以商品目标为准；10/1 起无 MONOLOG 区域，目标并入东南西北区；FLEX 作目标调整池允许负数；金价波动只影响 F、IF、TF、R、RU 五类的 OTB 成本，不影响库存成本/在产订单成本；过期在产订单放到当周下一周并标注；财务回仓计划（业务分类层级）仅作参考，参与计算的是商品部中模层级回仓计划；港澳海外不取含金粒的管理大类
### 行动项
- [stated] 11/06 前解决遗留问题、沟通并对齐方案（o9 & MFP/OTB 用户）；11/13 前 Release 1 业务确认及 Sign-off（o9 & Elsie）；o9 跟进上传模板、市场筛选、多语言展示和字段命名统一；o9 & 元凤 扩大牌面价/成本价差异分析；o9 反馈 RO/PO 担忧并讨论备选方案

## 10/30 o9 邮件：加盟批发商库存扣减及财务周转口径（Ying Zhang → Elsie；抄送 Caroline、胡志军、孙方雨、用户、o9 团队）
- [stated] o9 说明现状：系统里 RSV Target 含加盟批发商销售目标、OTB 含其买货需求、Ending Inventory 也含其期末库存，所以系统算出的 Stock Turnover 是含加盟批发商的口径
- [stated] o9 建议：保留现有 Stock Turnover，新增财务口径的 Reporting Stock Turnover——Reporting Inventory = 总库存 − 加盟批发商库存；Reporting RSV Target = 总 RSV Target − 加盟批发商 RSV Target；Reporting Stock Turnover = Reporting Inventory / Reporting RSV Target
- [stated] 已有明确的加盟批发商 RSV Target 数据，可直接扣减；但期末库存里怎么识别、扣除加盟批发商库存还不清楚，o9 要求财务给出扣减规则、数据来源和计算方式，之后才落实计算逻辑——球在财务（Elsie）这边
- [stated] 此邮件对应 10/29 UAT 清单里 Pending 的 P2 问题"加盟批发库存口径"

## 11/05 MFP/OTB 业务周例会（o9 Ying Zhang 纪要 + PPT v20261105；用户在主送，Ivy、胡志军、任波、孙方雨抄送）
### 节点
- [stated] 11/06 UAT 问题及测试结果阶段性确认 → 11/13 UAT Sign-off → Go/No-Go 11/19（10/29 PPT 写 11/18）→ 11/27–11/30 切换，Release 1 计划 11/30 上线
- [stated] 签字人（PPT）：Elsie 代表集团财务、Brenda 代表集团商品、军爷代表资讯及通讯应用；流程 UAT 结果确认（11/6）→ Sign-off（11/13）→ 上线准备 → Go/No-Go（11/19），结论以 Email 给 CTF
- [stated] HKM/ID UAT：数据模板预计下周中才提供，可能影响 11/13 整体签收；是否允许 CN 先单独签收、签收范围及量化标准，待 Elsie 和管理层决定（o9 & Elsie 行动项）
- [stated] 下周计划组织 Finance → MFP → OTB 端到端联合演示，验证上下游数据和流程衔接（o9 & CTF 项目组）
### 测试脚本结果（PPT）
- [stated] 共 79 行脚本，78 通过、1 未通过：导入财务目标 9 行中 1 行未过，原因是数据上传不一致（UAT Owner 卢傲环，10/19 确认）；制定商品目标 10/10（Caroline）、输出 MFP 年度目标 6/6（Caroline/卢傲环）、成品 OTB 年度预算 23/23（黄元凤）、财务视角成品 OTB 滚动 31/31（Caroline/卢傲环/黄元凤），确认日期都在 10/14–10/21，均为 Phase 1
- [stated] o9 纪要称整体通过情况良好，主要遗留在财务目标上传后的数据一致性和部分功能优化
### 问题状态（截至 11/05）
- [stated] 71 条，Closed 47（66.2%）；WIP 11（多涉及 DP 依赖、主数据调整、开发）；Pending Confirmation 7（o9 已给方案或 workaround，待用户验证）；ADO 4；Pending Discussion 2
- [stated] P2 进展：
  - Rita 财务目标上传部分成功/展板不同步（BUG 1011974）和失败明细下载为空——两条都在 ADO，o9 预计 12 月底平台升级后解决，due 12/30，晚于 11/30 上线
  - RO/PO（On Order 取数）：军爷 10/22 定为取 PO 作在产订单、ICS 内部做数据治理使 RO 与 PO 一致；CTF 项目组称在解决中、上线前解决（WIP，due 11/30）
  - 区域下拉框按市场过滤：已配置（ADO 1016619），但与 Subtotal 功能不兼容，Pending Confirmation 待元凤反馈
  - 加盟批发库存口径、OTB 牌面价 vs 成本价：仍 Pending Discussion，"待业务团队确认方案"
- [stated] 多条命名/显示类 WIP（PY27→FY27、Display Name 简繁英、Sales Channel 命名、维度名精简）o9 建议 11 月底改，否则影响现有数据；汇率切换方案已定待配置；4 条依赖 DP；HJ 标签依赖 ICS 数据
- [stated] 两条 P4 UI 问题（冻结列、Attributes 版面）当前功能不支持，已建 VOC ADO
### 业务讨论
- [stated] 加盟批发库存：财务周转需剔除批发商库存，但 Ending Inventory 的识别和扣减规则仍待业务/财务确认（承接 10/30 o9 邮件）
- [stated] OTB 牌面价 vs 成本价：继续分析差异，尤其所有黄金类和无系列数据，另约 Elsie 讨论
- [stated] 金额显示：系统按数值自动缩放为 K/M/B，下载保留完整数值；沈娜建议增加可选固定单位（K/M/B）

## 11/09 库存扣减逻辑与 UAT 讨论（12:59–13:34，智能纪要 + 录音；Elsie、o9 Ying Zhang、军爷、用户等；Elsie 只有半小时）
### 加盟批发库存：Elsie 的口径与顾虑
- [stated] 财务算存货和周转只用 CTF 归属的存货；批发端在确认 REV（加盟商取货）时存货已转出 CTF、销售成本同月体现，所以集团周转目标是 REV 视角；RSV 与 REV 之间主要是时间差
- [stated] Elsie 认为 o9 10/30 提的"从 RSV/库存直接扣减加盟批发"没有体现时间差；还担心取货率/铺货率——加盟商不一定 100% 取货（可能只取八成多），没取走的货压在 CTF 手里，单用 RSV 推不出来
- [stated] o9 回应：牌面价换算本来就分两套——自营和加盟寄售用 RSV 推，加盟批发用 REV 推，所以认为时间差已考虑；待向 Angie（安琪）确认；三种模式的 RSV、REV、当前库存是分开的，但 OTB 计算不分自营/加盟
### Back test（Elsie 要求，签收前完成）
- [stated] 用上半年（4–9 月）的 RSV、件数、批发率作输入，按系统现有逻辑跑出期末库存和 OTB，与实际存货和实际 OTB 对比；差异小就往下走，差异大就修正逻辑；可接受阈值未定（Elsie 举例 3% 或 5%，按百分比还是金额也未定）
- [stated] o9 说 back test 不在 UAT 内（UAT 用静态数据），但可以做；o9 需财务指定人提供数据和业务判断
- [stated] Elsie 指定内地的 [[shen-na]] 和 Priscilla 参与；批发主要是内地问题，港澳和国际基本没有批发
- [stated] Elsie 请用户帮忙安排 back test 并拉内地团队，争取一两天内跑出结果，赶在 11/13 签收前；Elsie 认为 back test 做完才算真正完成 UAT
- [stated] 用户在会上的意见：按范围拆开看——CN 测试已按 o9 场景做完，但 bug 和 UI 问题需关键用户复测确认；港澳（卢傲环）数据还在准备上传；back test 可与端到端演示同步进行，但都要有明确可量化的结果
### UAT 状态与 11/10 端到端演示
- [stated] o9：UAT 已无单独需要再测的；能处理的问题都处理完，部分因依赖要到 11 月底；剩两条重要的待业务确认——加盟批发库存、牌面价 vs 成本价
- [stated] 11/10 端到端演示保留，重点是带用户走通财务 → 商品 → 成品 OTB 流程、明确各自职责，不讨论数据本身；back test 分析出结果后另约会议
- [stated] Elsie 要求讲清楚：Release 1 的结果是真实数据，要判断业务合理性，测试同事的责任不只是功能通过，发现异常要及时反馈；o9 同意让业务重点校验 OTB 结果和周转是否合理，也请 Elsie 向负责同事强调
### 港澳海外与签收范围
- [stated] o9 项目侧提议：会后由他、用户、孙方雨一起对港澳海外 UAT 的准备情况，出计划，看能否赶在 11/19 Go/No-Go 前测完，据此决定上线范围；11/13 关闭/确认 UAT 问题，11/19 Go/No-Go 由领导层、军爷、Elsie、孙方雨等共同决定
- [stated] Elsie 同意，条件是讲清楚：各时间节点做到什么、哪些范围已通过、哪些没通过、没通过的怎么处理（含 workaround），不要让人以为部分通过就是全部通过
### 外部顾问风险
- [stated] 有外部顾问（含 Theresa Wang）在调研 MFP/OTB 流程；Elsie 只向顾问讲过 RSV 和滚动预测的财务流程，没讲 o9 里怎么做；上周 product workshop 上 Brenda、Annie 说他们做的是 bottom-up MFP；军爷说 MFP 有两个方向——财务自上而下和商品视角
- [stated] Elsie 担心顾问建议大改、导致 UAT 重做；军爷 11/10 会见顾问，之后会专题沟通 o9 现状，并尽量控制改动
- [stated] Elsie 偏好约 15–30 分钟快速 catch-up，而不是来回邮件
### 用户的行动（11/09 起，未见完成证据）
- [stated] 安排内地 back test：拉沈娜、Priscilla，与 o9 确定数据和口径，一两天内出结果，赶在 11/13 前
- [stated] 与 o9 项目侧、孙方雨对港澳海外 UAT 计划，目标在 11/19 前判断上线范围
````

### 03 DSC Project · areas/elsie-follow-up.md

- 原始路径：`/projects/01a14711-18cb-7340-b9c6-ba609c01c468/areas/elsie-follow-up.md`
- updated (UTC)：2026-11-09T08:43:55Z

````markdown
---
name: elsie-follow-up
description: Project copy of the user's Elsie follow-up list — latest stated changes to how it is maintained; see account-level /areas/elsie-follow-up.md for fields and rules
sources: [cowork]
aliases: [Elsie tracker, Elsie 跟进清单, Elsie follow-up list, tracking list for Elsie]
---

- [stated] 2026-10-28 用户要求为 Elsie 跟进清单建立每天更新的追踪机制；会议讨论事项要梳理后更新进该清单（Excel 版文件名形如 CTF_Elsie_Follow_Up_Tracker_Updated_N.xlsx）
- [stated] 2026-11-09 用户要求牢记：Elsie 跟进清单每次都要输出可下载的 Excel 文档（每日任务无变化时也要发）
````

### 03 DSC Project · people/elsie.md

- 原始路径：`/projects/01a14711-18cb-7340-b9c6-ba609c01c468/people/elsie.md`
- updated (UTC)：2026-10-22T05:44:18Z

````markdown
---
name: elsie
description: Elsie Wong — Chow Tai Fook colleague; full name and work email
sources: [cowork]
aliases: [Elsie, Elsie Wong, Wong Ching Yin, 黃靖燕]
---

- [stated] full name Wong Ching Yin, Elsie (CTFHK-黃靖燕); work email elsiewong@chowtaifook.com
````

### 03 DSC Project · people/ivy.md

- 原始路径：`/projects/01a14711-18cb-7340-b9c6-ba609c01c468/people/ivy.md`
- updated (UTC)：2026-10-22T05:44:23Z

````markdown
---
name: ivy
description: Ivy Cheng — VP at Chow Tai Fook; full name and work email
sources: [cowork]
aliases: [Ivy, Ivy Cheng, 鄭凱因, VP]
---

- [stated] full name Cheng Ivy (CTFHK-鄭凱因); work email ivycheng@chowtaifook.com
````

### 03 DSC Project · people/vivian.md

- 原始路径：`/projects/01a14711-18cb-7340-b9c6-ba609c01c468/people/vivian.md`
- updated (UTC)：2026-10-22T05:44:20Z

````markdown
---
name: vivian
description: Vivian Lau — user's direct boss at Chow Tai Fook; full name and work email
sources: [cowork]
aliases: [Vivian, Vivian Lau, Lau Man Ming, 劉敏明, boss, 老板]
---

- [stated] full name Lau Man Ming, Vivian (CTFHK-劉敏明); work email vivianlau@chowtaifook.com
````


---

## Part B · 项目：05 Catch up with VV

- 记忆文件夹：`/projects/01a14711-e4ef-76c4-870b-f9c3a0b6c8cc/`

### 05 Catch up with VV · preferences.md

- 原始路径：`/projects/01a14711-e4ef-76c4-870b-f9c3a0b6c8cc/preferences.md`
- updated (UTC)：2026-10-29T12:54:15Z

````markdown
---
name: preferences
description: How the user wants Claude to work in the 05 Catch up with VV project — standing cross-check rule when updating reports and project material
sources: [cowork]
---

- [stated] 每次更新（周报等）时，都要交叉复核所有项目的记忆：01 AI Sales Forecast、02 Planning Tool、03 DSC Project、04 Project Connections、05 Catch up with VV（用户 2026-10-29 明确要求牢牢记住）
````

### 05 Catch up with VV · areas/finance-systems-projects.md

- 原始路径：`/projects/01a14711-e4ef-76c4-870b-f9c3a0b6c8cc/areas/finance-systems-projects.md`
- updated (UTC)：2026-10-29T12:54:44Z

````markdown
---
name: finance-systems-projects
description: Milestones, timeline and open items for AI Sales Forecast, Planning Tool and DSC/o9, from emails, the timeline and the Go-Live Criteria deck the user shared (updated 29 Oct 2026); read when drafting weekly reports or planning
sources: [cowork]
aliases: [AI SF, Planning Tool, PT, DSC, o9, 三系统, timeline]
---

User asked to absorb these shared emails and attachments (week of 19–23 Oct 2026); updated 29 Oct with the user's 29 Oct email to Elsie and the Go-Live Criteria deck v3.

## Weekly report sent
- [stated] The 23 Oct weekly update sent to Vivian was the user's own revised version (no special-focus band), with the reviewed three-project timeline (00_Timeline_AI_SF_DSC_Planning_Tool_EN_Reviewed_20261023) attached
- [stated] Weekly Finance Systems team meeting is normally Monday 11:00–12:00; the week of 26 Oct it moved to Tuesday 27 Oct, 11:30–12:30

## AI Sales Forecast
- [stated] Kick-off (Finance, ICC, Yichen) on 29 Oct 2026; user requirements discovery Tue–Fri 3–6 Nov 2026 (user, 29 Oct)
- [stated] Go-live schedule to be revalidated; original window Jun–Aug 2027 (Go-Live deck v3: AI SF expected go-live around Aug 2027)
- [stated] Open item: number of scenarios, assumptions and baseline selection rules, to be clarified in requirements gathering

## Planning Tool
- [stated] Phase 1 = submit & consolidate, basic calculations & reporting, version control, no external integration
- [stated] Phase 1 plan per the user's Go-Live Criteria deck v3 (28 Oct, for the 3 Nov status / go-live criteria meeting; all planned, not done): demos tentatively all signed off by 3 Nov; 2–6 Nov Novus internal testing; 10 Nov CAPEX UAT; 17 Nov online training for UAT testers; 18–19 Nov on-site UAT in HK (sessions confirmed by Dennis on 22 Oct); 23–27 Nov Novus fixes and CTF review; 3 Dec target UAT sign-off; 4 Dec SSO setup and go-live prep; 7–18 Dec deployment; 18 Dec end-user training; 21 Dec go-live confirmation (email sign-off); 30 Dec refresher; 5–8 Jan 2027 Topline and 19–22 Jan P&L / Inventory / BS / CF submission, both with Novus on site
- [stated] Phase 1 UAT acceptance criteria: user sent the revised v8.1 to Vivian on 27 Oct after her guidance (per-module rules: all tested, 0 Critical/High, ≤3 Low open — corrected by user 29 Oct); details in [[planning-tool]] project copy
- [stated] Go-Live deck v3 proposes five readiness checks: UAT completion (no Critical/High open, ≤3 Low per subject across 9 subjects: Foundations, Store Count, Topline, Expenses, Capex, Inventory & OTB, Balance Sheet, Cashflow, Consolidation and Reporting), master data completeness, historical data (FY26 actual, FY27 9+3 prelim), training preparation, user accounts / SSO — proposed, not yet aligned
- [stated] Next: draft the Planning Tool Roadmap from the template, P&L first; align with Dennis, then Frank and other system stakeholders
- [stated] Phase 2 (driver-based planning / integration, scope TBC): earliest start 1 Apr 2027, subject to budget approval and contract signing; an earlier start or phased delivery (adjustment entry and return to AI SF first) is under assessment
- [stated] Monologue: the user reported that Anita says it has been merged into the four regions (North/South/East/West) since 10.1

## DSC / o9
- [stated] Release 1 UAT ongoing, overall sign-off pending; upload consistency, OTB valuation (tag price vs cost) and the RO/PO process need validation
- [stated] 29 Oct email to Elsie: group targets use finance-scope turnover (ex franchise wholesale) as the single source — Karen prefers not to keep dual scopes; franchise-wholesale turnover only as reference / scenario with no target; user to align with Sun Fangyu and submit the requirement to o9
- [stated] 29 Oct email to Elsie: RO/PO budget commitment gap pending senior management decision, user follows the project team's discussion with Jun Ye; ending actual cost algorithm — Elsie asked o9 to recalculate the full F-category gap (amount and %) before the final decision, user tracks it
- [stated] Original baselines: MFP/OTB technical go-live 30 Nov 2026; AP/DP 31 Jan 2027; to be revalidated
- [stated] Finance targets are uploaded manually to o9 for now and will transfer automatically once the PT integration is ready; integration timing TBC

## Cross-system
- [stated] Three-vendor (AI SF, o9, Novus) integration design meeting: Go-Live deck v3 says late Nov to early Dec (earlier talk: weeks of 7 or 14 Dec), exact date TBC; Novus quote HKD 40K (T&M), to be funded from the AI SF budget
- [stated] Vivian 29 Oct: AI SF user requirements are not to be signed off before the three-vendor meeting has aligned
- [stated] Already live: Power BI (refreshed daily from ICS); Lucanet (consolidates Mainland EAS, HK S4 and international sources for external reporting); SAP (HK moved to S4 in Apr 2026, Mainland on EAS, international S4 rollout to follow)

## 1:1 with Vivian
- [stated] Weekly 1:1 with Vivian, Tuesday 9:30–10:00 (Teams); user sends the agenda the day before
- [stated] 27 Oct agenda: roadmap template (automated vs manual fields and data sources), PT UAT acceptance criteria, personal Q&A, timeline for AI SF user requirement discovery
````

### 05 Catch up with VV · areas/planning-tool.md

- 原始路径：`/projects/01a14711-e4ef-76c4-870b-f9c3a0b6c8cc/areas/planning-tool.md`
- updated (UTC)：2026-10-29T12:46:27Z

````markdown
---
name: planning-tool
description: Project-scoped updates to the Planning Tool (Workday Adaptive, Novus) — UAT acceptance criteria v8.1, data-source mapping status, roadmap task (from 27 Oct 2026); read with the account-level planning-tool file
sources: [cowork]
aliases: [PT, Planning Tool, Workday Adaptive, WAP, Submission Tool, 财务规划工具]
---

User asked to absorb the 27 Oct 2026 1:1 email to Vivian and its two attachments. Account-level background stays in the main planning-tool file.

## UAT 验收标准 v8.1（10/27 发给 Vivian 的修订版）
- [stated] 按模块判定通过，三条同时满足：① 全部场景已测（含异常步骤和 UAT 现场新增场景），模块 owner 确认 Testing done = Yes；② Critical / High 为 0（Novus 修复、业务用户复测后关闭；临时关闭需 Ivy / Vivian 批准）；③ 每模块 Low 最多 3 个未关闭（用户 10/29 更正，原记为 2 个），上线后再修
- [stated] 六个模块：Foundations & Controls（组织层级、权限、模板上传、版本与实际化、提交与锁定、汇率／金价参数、清数）；P&L Inputs（门店数、Topline RSV/Qty/ASP、SSSG、Signature Collection、COGS / NOP to NP）；Expenses & CAPEX（SG&A、A&P、Professional Fee、IT Spend、CAPEX 模板、折旧与付款）；Inventory & OTB；BS & Cash Flow（含 BS KPIs）；Consolidation & Reporting（合并、版本比较、CFO Scorecard、下载对数、Topline 演练）
- [stated] 严重度由 Fin Tech 团队在每日 triage 设定，测试人只描述问题；未 triage 的问题按 High 计；Critical = 系统逻辑错或控制失效（越权查看／修改、锁定版本仍可改、版本或实际数无故变化）；High = 数字错或功能失败（上传未显示／未保存、合计或比率算错、上传或提交失败、上传 0／空白不能覆盖旧值）；Low = 仅外观或轻微易用性（标签措辞、格式、报错信息不清、列宽不保留）
- [stated] 问题分类：Access / lock / version、Logic / configuration、Upload / template、Calculation / aggregation、Submission / workflow、Performance / stability、Report / presentation 计入上线判断；Change request（进 Novus 范围外登记）、Out of Phase 1 scope（进 Phase 2 需求清单）、Test script error 不计入；标签可能误导读数时 Report 类升为 High
- [stated] 状态流：Open → In progress → Ready for retest → Closed，复测失败设 Reopened；Issue Log 测试人填黄色列，triage 填蓝色列，其余自动计算

## 数据来源 Overview + Mapping（10/27 版）
- [stated] Phase 1：23 个模板全部人工上传且均已 Finalized——P&L／库存／明细 20 个模板 111 个输入项，BS／CF／Key Metrics 3 个模板 116 个输入项，共 227 项
- [stated] Phase 2 目标：Actual 全部来自系统（Lucanet / SAP / EAS / Power BI），FP&A 不再人工上传；Forecast 可为人工上传、系统集成或两者结合
- [stated] Phase 2 Actual 来源：已识别 102 项、待确认 121 项（多数在 Cash Flow 86 项）、无实际数 4 项（OTB、CAPEX 通用假设）；Forecast 方法：系统集成（含 PT 内计算）85、人工＋系统 14、人工 54、TBD 74
- [stated] 按系统：Lucanet 提供 84 项 Actual；SAP 4 项（汇率、Store / Office / PSC CAPEX）；Power BI 11 项（门店、库存）；EAS 提供 4 项 CAPEX 预测（已批预算）；DSC (o9) 3 项 OTB 预测；AI SF 14 项预测（门店数开关店、RSV/Qty、SSSG）；54 项预测无系统来源、由业务上传
- [stated] 10/27 Vivian 提出的待确认：Cash Flow 模板各行如何对应 Lucanet 科目；Power BI 门店数只有时点余额，开店／关店／业态转换能否取得或推算
- [stated] 其他待确认：哪些 P&L 科目取 Lucanet、哪些取 SAP（Ivy 10/19：全科目表都要集成）；SAP 费用能否按项目／活动取数；EAS 与 PT 数据方向，A&P 和 Professional Fee 是否也走 EAS；o9 集成时间与过渡期 OTB 由谁提供；AI SF trendline 的维度和颗粒度、是否覆盖门店数和 SSSG
- [stated] 系统联系人：Lucanet—ICC、Arthur、Jay；SAP—ICC；EAS—ICC、Xiao Lin；Power BI—ICC、[[frank]]；DSC—[[elsie]] 与 DSC 团队；AI SF—[[li-xinhong]]

## Roadmap（10/27 1:1 后）
- [stated] 用户先按模板起草 Planning Tool Roadmap，先聚焦 P&L（Vivian 暂不需要看细节）；与 [[dennis]] 对齐后再跟 [[frank]] 和其他系统相关方跟进
````

### 05 Catch up with VV · areas/weekly-report.md

- 原始路径：`/projects/01a14711-e4ef-76c4-870b-f9c3a0b6c8cc/areas/weekly-report.md`
- updated (UTC)：2026-10-22T11:03:44Z

````markdown
---
name: weekly-report
description: User's recurring weekly PPT status report (周报) to Vivian, wanted ready by Friday noon, in the format of earlier reports
sources: [chat]
aliases: [周报, weekly update, Finance Systems weekly, PPT周报]
---

- [stated] prepares a weekly PPT report (周报) for [[vivian]]; wants it drafted every Friday by 12:00, following the format of earlier weekly reports
````


---

## Part B · 项目：SBUX for AI SF

- 记忆文件夹：`/projects/01a18bf6-69ce-7194-a079-be3f5d7af704/`

### SBUX for AI SF · areas/starbucks-reference.md

- 原始路径：`/projects/01a18bf6-69ce-7194-a079-be3f5d7af704/areas/starbucks-reference.md`
- updated (UTC)：2026-11-10T01:49:46Z

````markdown
---
name: starbucks-reference
description: Starbucks EP project knowledge (SBX-001–105) kept as an isolated reference for AI SF learning — boundary rules and where the docs live
sources: [chat]
aliases: [星巴克项目, SBUX, Starbucks EP, SBX]
---

- [stated] asked to absorb the user's past Starbucks project design ideas independently, as a possible reference for [[ai-sales-forecast]]
- [stated] exclude anything related to 杉数科技 (Shanshu)
- [stated] must not interfere with or change the current Chow Tai Fook projects — Starbucks items are reference only, never CTF requirements, decisions or to-dos
- [stated] source: 01_Starbucks_Independent_Knowledge_Full.docx (dated 2026-10-29) plus three further batches of Starbucks EP files uploaded 2026-10-30
- [stated] project docs: starbucks/SBX_knowledge_part1_ch1-6.md, starbucks/SBX_knowledge_part2_ch7-12.md (SBX-001–060), starbucks/SBX_batch2_business_logic.md (061–085), starbucks/SBX_batch3_storedays_versions_checks.md (086–097), starbucks/SBX_batch4_drivers_planning_inputs.md (098–105), starbucks/SBX_to_AISF_reference_map.md
- [stated] several Starbucks decks were authored by the user (Sampson Sun), e.g. FP Logic Enhancement, EP Logic Enhancement 0910, Store List Recon Solution, Dummy Store Weekend Closure, New Storelist & FF Logic Enhancement
- [stated] term mapping the user uses: 同店 = SSSG; 可比店 = Comp store; 当年开业 = CY store
````

