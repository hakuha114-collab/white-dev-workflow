# 代码评审报告

## 项目信息

| 项目 | 值 |
|------|-----|
| 项目名称 | {{PROJECT_NAME}} |
| 评审时间 | {{REVIEW_TIME}} |
| 评审方式 | 三元代码审核 (sanyuan-skills) |
| 审核工具 | sanyuan-skills + agency-agents |

---

## 评审摘要

| 指标 | 数值 |
|------|------|
| 评审文件数 | {{FILES_REVIEWED}} |
| 发现问题数 | {{ISSUES_FOUND}} |
| 已修复问题 | {{ISSUES_FIXED}} |
| 待修复问题 | {{ISSUES_PENDING}} |
| 综合评分 | {{OVERALL_SCORE}}/100 |

---

## 三元审核维度评分

| 维度 | 权重 | 得分 | 状态 |
|------|------|------|------|
| 可读性 | 25% | {{READABILITY_SCORE}} | {{READABILITY_STATUS}} |
| 可维护性 | 25% | {{MAINTAINABILITY_SCORE}} | {{MAINTAINABILITY_STATUS}} |
| 性能 | 20% | {{PERFORMANCE_SCORE}} | {{PERFORMANCE_STATUS}} |
| 安全性 | 15% | {{SECURITY_SCORE}} | {{SECURITY_STATUS}} |
| 测试覆盖 | 15% | {{TEST_COVERAGE_SCORE}} | {{TEST_COVERAGE_STATUS}} |
| **综合** | **100%** | **{{OVERALL_SCORE}}** | **{{OVERALL_STATUS}}** |

---

## 维度详细分析

### 1. 可读性 (25%)

**检查项**:
- [ ] 命名清晰表达意图
- [ ] 函数短小精悍（<20行）
- [ ] 注释解释"为什么"而非"是什么"
- [ ] 代码结构符合认知负荷原则

**评分**: {{READABILITY_SCORE}}/100

**问题**: {{READABILITY_ISSUES}}

---

### 2. 可维护性 (25%)

**检查项**:
- [ ] 遵循单一职责原则
- [ ] 依赖合理、可注入
- [ ] 易于扩展和修改
- [ ] 配置与代码分离

**评分**: {{MAINTAINABILITY_SCORE}}/100

**问题**: {{MAINTAINABILITY_ISSUES}}

---

### 3. 性能 (20%)

**检查项**:
- [ ] 时间复杂度合理
- [ ] 空间使用高效
- [ ] 无不必要的计算
- [ ] 缓存策略得当

**评分**: {{PERFORMANCE_SCORE}}/100

**问题**: {{PERFORMANCE_ISSUES}}

---

### 4. 安全性 (15%)

**检查项**:
- [ ] 输入验证完整
- [ ] 异常妥善处理
- [ ] 无敏感信息泄露
- [ ] 无注入风险

**评分**: {{SECURITY_SCORE}}/100

**问题**: {{SECURITY_ISSUES}}

---

### 5. 测试覆盖 (15%)

**检查项**:
- [ ] 单元测试覆盖主要路径
- [ ] 边界条件已测试
- [ ] 集成测试完整
- [ ] 测试独立可重复

**评分**: {{TEST_COVERAGE_SCORE}}/100

**问题**: {{TEST_COVERAGE_ISSUES}}

---

## 问题详情

{{REVIEW_DETAILS}}

### 问题记录格式

```markdown
### Issue {{ISSUE_NUMBER}}: {{ISSUE_TITLE}}

**严重程度**: {{SEVERITY}} (P0/P1/P2/P3)

**维度**: {{DIMENSION}} (可读性/可维护性/性能/安全性/测试覆盖)

**位置**: {{FILE_LOCATION}}

**问题描述**: {{DESCRIPTION}}

**Karpathy 规范相关**: {{KARPATHY_GUIDELINE}}

**修复建议**: {{SUGGESTION}}

**修复状态**: {{STATUS}}

**修复提交**: {{COMMIT_HASH}}
```

---

## 按严重程度分类

### P0 - 严重问题（阻塞性）

{{P0_ISSUES}}

### P1 - 重要问题（必须修复）

{{P1_ISSUES}}

### P2 - 中等问题（建议修复）

{{P2_ISSUES}}

### P3 - 轻微问题（可选修复）

{{P3_ISSUES}}

---

## Karpathy 规范检查

| 规范项 | 检查结果 | 问题数 |
|--------|----------|--------|
| Think Before Coding | {{THINK_RESULT}} | {{THINK_ISSUES}} |
| Simplicity First | {{SIMPLICITY_RESULT}} | {{SIMPLICITY_ISSUES}} |
| Surgical Changes | {{SURGICAL_RESULT}} | {{SURGICAL_ISSUES}} |
| Goal-Driven | {{GOAL_RESULT}} | {{GOAL_ISSUES}} |

---

## 审核工具记录

| 工具 | 审核文件数 | 发现问题数 | 占比 |
|------|------------|------------|------|
| sanyuan-skills | {{SANYUAN_FILES}} | {{SANYUAN_ISSUES}} | {{SANYUAN_PERCENT}}% |
| agency-agents | {{AGENCY_FILES}} | {{AGENCY_ISSUES}} | {{AGENCY_PERCENT}}% |

---

## 评审结论

{{REVIEW_CONCLUSION}}

### 是否通过审核

- [ ] 通过 - 代码质量达标，可以合并
- [ ] 有条件通过 - 需修复 P0/P1 问题
- [ ] 不通过 - 需重大修改

### 后续行动

{{FOLLOW_UP_ACTIONS}}

---

*生成时间: {{GENERATE_TIME}}*
*生成方式: QClaw Dev Workflow - Phase 4 (三元代码审核)*
