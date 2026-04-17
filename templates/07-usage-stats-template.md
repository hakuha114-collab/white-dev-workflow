# 使用统计报告

## 项目信息

| 项目 | 值 |
|------|-----|
| 项目名称 | {{PROJECT_NAME}} |
| 统计时间 | {{STATS_TIME}} |
| 项目周期 | {{PROJECT_DURATION}} |

---

## Skill 使用统计

### Skill 使用总览

| Skill 名称 | 使用次数 | 主要用途 | 占比 |
|------------|----------|----------|------|
| {{SKILL_NAME}} | {{USAGE_COUNT}} | {{USAGE_PURPOSE}} | {{PERCENTAGE}}% |

### Skill 使用详情

{{SKILL_USAGE_DETAILS}}

---

## Agent 调用统计

### Agent 调用总览

| Agent ID | 调用次数 | 执行任务 | 占比 |
|----------|----------|----------|------|
| {{AGENT_ID}} | {{CALL_COUNT}} | {{TASKS}} | {{PERCENTAGE}}% |

### Agent 调用详情

{{AGENT_CALL_DETAILS}}

---

## 文档生成统计

| 文档类型 | 生成次数 | 总大小 | 平均大小 |
|----------|----------|--------|----------|
| 需求文档 | {{REQ_COUNT}} | {{REQ_SIZE}} | {{REQ_AVG}} |
| 设计文档 | {{DESIGN_COUNT}} | {{DESIGN_SIZE}} | {{DESIGN_AVG}} |
| 任务计划 | {{TASK_COUNT}} | {{TASK_SIZE}} | {{TASK_AVG}} |
| 开发记录 | {{DEV_COUNT}} | {{DEV_SIZE}} | {{DEV_AVG}} |
| 测试用例 | {{TEST_COUNT}} | {{TEST_SIZE}} | {{TEST_AVG}} |
| 代码评审 | {{REVIEW_COUNT}} | {{REVIEW_SIZE}} | {{REVIEW_AVG}} |

---

## 代码变更统计

| 指标 | 数值 |
|------|------|
| 总提交次数 | {{TOTAL_COMMITS}} |
| 新增文件数 | {{NEW_FILES}} |
| 修改文件数 | {{MODIFIED_FILES}} |
| 删除文件数 | {{DELETED_FILES}} |
| 新增代码行 | {{LINES_ADDED}} |
| 删除代码行 | {{LINES_DELETED}} |
| 净增代码行 | {{LINES_NET}} |

---

## 时间统计

| 阶段 | 开始时间 | 结束时间 | 耗时 |
|------|----------|----------|------|
| Phase 1: Brainstorming | {{P1_START}} | {{P1_END}} | {{P1_DURATION}} |
| Phase 2: Writing Plans | {{P2_START}} | {{P2_END}} | {{P2_DURATION}} |
| Phase 3: Development | {{P3_START}} | {{P3_END}} | {{P3_DURATION}} |
| Phase 4: Code Review | {{P4_START}} | {{P4_END}} | {{P4_DURATION}} |
| Phase 5: Test Cases | {{P5_START}} | {{P5_END}} | {{P5_DURATION}} |
| Phase 6: Doc Generation | {{P6_START}} | {{P6_END}} | {{P6_DURATION}} |
| Phase 7: Finishing | {{P7_START}} | {{P7_END}} | {{P7_DURATION}} |

---

## 效率指标

| 指标 | 数值 | 说明 |
|------|------|------|
| 代码产出率 | {{PRODUCTIVITY}} 行/小时 | 净增代码行 / 开发时间 |
| 问题发现率 | {{ISSUE_RATE}} 个/千行 | 发现问题数 / 千行代码 |
| 修复效率 | {{FIX_RATE}}% | 已修复问题 / 总问题数 |
| 文档覆盖率 | {{DOC_COVERAGE}}% | 有文档的任务 / 总任务数 |

---

## 总结

{{SUMMARY}}

---

*生成时间: {{GENERATE_TIME}}*
*生成方式: QClaw Dev Workflow - Phase 6*
