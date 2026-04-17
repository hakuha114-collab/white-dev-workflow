---
name: qclaw-dev-workflow
description: >
  完整的软件开发工作流 Skill，结合 Superpowers TDD 流程、Karpathy 代码规范、三元代码审核，
  自动生成完整的项目文档。使用场景：(1) 创建新项目 (2) 开发新功能 (3) 代码重构。
  自动生成：需求文档、设计文档、开发记录、测试用例、代码评审报告、Skill/Agent 使用统计。
license: MIT
---

# QClaw Dev Workflow — 完整开发工作流

基于 [obra/superpowers](https://github.com/obra/superpowers)、[Karpathy Coding Guidelines](https://x.com/karpathy/status/2015883857489522876) 和 [sanyuan-skills](https://github.com/xxnuo/sanyuan-skills) 的综合开发工作流。

## 核心特性

1. **TDD 开发流程** - 测试驱动，规格先行
2. **Karpathy 代码规范** - 简洁、精准、目标导向
3. **三元代码审核** - 结构化、多维度代码评审
4. **自动文档生成** - 需求/设计/开发/测试/评审全覆盖
5. **使用统计追踪** - Skill 和 Agent 调用次数自动记录

## 工作流 Pipeline

```
Idea → Brainstorm → Plan → Subagent-Driven Build (TDD) → Code Review (三元) → Doc Generation → Finish
```

---

## Phase 1: Brainstorming（需求澄清）

**触发条件**: 用户想要构建新功能或项目

**执行步骤**:
1. 探索项目上下文（文件、文档、最近提交）
2. 一次问一个澄清问题（优先选择题）
3. 提出 2-3 种方案 + 权衡 + 推荐
4. 分段展示设计，每段获得用户批准
5. 生成需求文档 → `doc/01-requirements.md`

**Karpathy 规范应用**:
- Think Before Coding: 明确假设，不隐藏困惑
- 如果不确定，问清楚再开始

---

## Phase 2: Writing Plans（编写计划）

**触发条件**: 需求已批准

**执行步骤**:
1. 编写详细的分任务实现计划
2. 每个任务 = 2-5 分钟: 写测试 → 看失败 → 实现 → 看通过 → 提交
3. 生成设计文档 → `doc/02-design.md`
4. 保存实现计划 → `doc/03-tasks.md`

**Karpathy 规范应用**:
- Goal-Driven Execution: 定义可验证的成功标准
- 每个任务必须有明确的 verify 条件

---

## Phase 3: Subagent-Driven Development（子代理开发）

**触发条件**: 计划存在，用户选择子代理驱动执行

### 每个任务的循环

1. **Implementer** (`sessions_spawn`)
   - 使用 subagent 执行具体开发任务
   - **必须遵循 Karpathy 规范**:
     - Simplicity First: 最小代码解决问题
     - Surgical Changes: 只改必须改的
   - 生成开发记录 → `doc/04-dev-log.md`

2. **Spec Reviewer** (`sessions_spawn`)
   - 确认代码符合规格
   - 生成评审记录 → `doc/06-code-review.md`

3. **Quality Reviewer** (`sessions_spawn`)
   - 代码质量审核（应用 Karpathy 规范）
   - 检查：简洁性、精准性、目标导向

4. **修复问题**（如需要）
   - 重新派发 Implementer 修复
   - 重新审核直到通过

### TDD 强制要求

- 先写失败的测试
- 再写通过测试的代码
- 删除测试前写的代码

---

## Phase 4: Code Review（代码评审）- 三元审核

**触发条件**: 所有任务完成

**执行步骤**:
1. **使用 sanyuan-skills 进行代码审核**（主要工具）
2. 辅助使用 agency-agents 进行补充审核
3. 应用 Karpathy 规范进行全面检查
4. 生成代码评审报告 → `doc/06-code-review.md`
5. 修复发现的问题（循环 Phase 3）

### 三元代码审核流程

```python
# 调用 sanyuan-skills 进行代码审核
sessions_spawn:
  agentId: "sanyuan-reviewer"  # 三元代码审核 Agent
  task: |
    对以下代码进行结构化评审：
    
    文件: [文件路径]
    代码: [代码内容]
    
    请从以下维度进行评审：
    1. 可读性 - 命名、注释、结构
    2. 可维护性 - 耦合度、内聚性、扩展性
    3. 性能 - 算法复杂度、资源使用
    4. 安全性 - 输入验证、异常处理
    5. 测试覆盖 - 单元测试、边界测试
    
    输出格式：
    - 问题等级: P0(严重)/P1(重要)/P2(中等)/P3(轻微)
    - 问题描述
    - 具体位置
    - 修复建议
```

### 三元审核检查清单

| 维度 | 检查项 | 权重 |
|------|--------|------|
| **可读性** | 命名规范、代码注释、函数长度、结构清晰 | 25% |
| **可维护性** | 单一职责、依赖管理、模块化、配置化 | 25% |
| **性能** | 算法复杂度、资源使用、缓存策略 | 20% |
| **安全性** | 输入验证、异常处理、敏感信息 | 15% |
| **测试覆盖** | 单元测试、集成测试、边界测试 | 15% |

---

## Phase 5: Test Case Generation（测试用例）

**触发条件**: 代码评审通过

**执行步骤**:
1. 生成完整的测试用例文档 → `doc/05-test-cases.md`
2. 包括：单元测试、集成测试、边界测试
3. 确保测试覆盖率

---

## Phase 6: Doc Generation（文档生成）

**触发条件**: 所有开发和测试完成

**生成文档清单**:

| 文档 | 文件名 | 内容 |
|------|--------|------|
| 需求文档 | `doc/01-requirements.md` | 功能需求、非功能需求 |
| 设计文档 | `doc/02-design.md` | 架构设计、技术选型 |
| 任务计划 | `doc/03-tasks.md` | 分任务实现计划 |
| 开发记录 | `doc/04-dev-log.md` | 开发过程记录、修改历史 |
| 测试用例 | `doc/05-test-cases.md` | 测试用例、测试报告 |
| 代码评审 | `doc/06-code-review.md` | 评审记录、问题修复 |
| 使用统计 | `doc/07-usage-stats.md` | Skill/Agent 调用统计 |

---

## Phase 7: Finishing（项目收尾）

**触发条件**: 所有文档生成完成

**执行步骤**:
1. 验证所有测试通过
2. 生成使用统计报告 → `doc/07-usage-stats.md`
3. 提供选项：合并 / PR / 保持 / 丢弃
4. 执行用户选择

---

## Karpathy 规范检查清单

每个代码提交前必须检查：

- [ ] **Think Before Coding**: 假设明确，困惑已提出
- [ ] **Simplicity First**: 最小代码，无过度设计
- [ ] **Surgical Changes**: 只改必要的，风格一致
- [ ] **Goal-Driven**: 成功标准可验证

---

## 三元代码审核规范

### 问题等级定义

| 等级 | 定义 | 处理要求 |
|------|------|----------|
| **P0** | 严重问题：会导致系统崩溃、数据丢失、安全漏洞 | 必须立即修复，阻塞发布 |
| **P1** | 重要问题：影响功能正确性、性能严重下降 | 必须修复，可延期但需记录 |
| **P2** | 中等问题：代码可读性差、可维护性低 | 建议修复，技术债追踪 |
| **P3** | 轻微问题：风格不一致、注释缺失 | 可选修复，批量处理 |

### 审核维度详解

**可读性 (25%)**
- 命名是否清晰表达意图
- 函数是否短小精悍（<20行）
- 注释是否解释"为什么"而非"是什么"
- 代码结构是否符合认知负荷原则

**可维护性 (25%)**
- 是否遵循单一职责原则
- 依赖是否合理、可注入
- 是否易于扩展和修改
- 配置与代码是否分离

**性能 (20%)**
- 时间复杂度是否合理
- 空间使用是否高效
- 是否有不必要的计算
- 缓存策略是否得当

**安全性 (15%)**
- 输入是否验证
- 异常是否妥善处理
- 敏感信息是否泄露
- 是否有注入风险

**测试覆盖 (15%)**
- 单元测试是否覆盖主要路径
- 边界条件是否测试
- 集成测试是否完整
- 测试是否独立可重复

---

## OpenClaw Subagent 派发模式

### 开发 Agent

```yaml
sessions_spawn:
  agentId: "implementer"
  task: |
    Goal: [一句话目标]
    Context: [为什么重要，哪个计划文件]
    Files: [确切路径]
    Constraints: 
      - 遵循 Karpathy 规范
      - 只改必要的代码
      - TDD 强制
    Verify: [如何确认成功]
```

### 三元审核 Agent

```yaml
sessions_spawn:
  agentId: "sanyuan-reviewer"
  task: |
    对以下代码进行三元代码审核：
    
    文件: [文件路径]
    代码类型: [Java/Python/JS等]
    业务场景: [简要描述]
    
    请从可读性、可维护性、性能、安全性、测试覆盖五个维度进行评审。
    输出结构化报告，包含问题等级、位置、描述、修复建议。
```

---

## 使用统计追踪

自动记录以下信息：

| 类型 | 记录内容 |
|------|----------|
| Skill 使用 | skill 名称、使用次数、用途 |
| Agent 调用 | agent ID、调用次数、执行任务 |
| 三元审核 | 审核文件数、发现问题数、修复数 |
| 文档生成 | 文档类型、生成时间、文件大小 |
| 代码变更 | 文件数、行数、修改类型 |

统计信息写入 `doc/07-usage-stats.md`

---

## 文档模板

使用 `templates/` 目录下的模板生成文档：

- `01-requirements-template.md`
- `02-design-template.md`
- `03-tasks-template.md`
- `04-dev-log-template.md`
- `05-test-cases-template.md`
- `06-code-review-template.md`（含三元审核维度）
- `07-usage-stats-template.md`

---

## 关键原则

1. **规格先行** - 不写代码直到设计批准
2. **TDD 始终** - 先写失败测试，再写代码
3. **YAGNI** - 移除所有不必要功能
4. **DRY** - 不重复
5. **系统化** - 压力越大越要遵循流程
6. **证据胜于声明** - 验证后再宣布成功
7. **频繁提交** - 每个绿测试后提交
8. **Karpathy 规范** - 简洁、精准、目标导向
9. **三元审核** - 结构化、多维度代码评审

---

## 依赖

- exec 工具
- sessions_spawn 工具
- karpathy-guidelines skill（代码规范）
- **sanyuan-skills（代码审核 - 主要工具）**
- agency-agents skill（代码审核 - 辅助工具）
