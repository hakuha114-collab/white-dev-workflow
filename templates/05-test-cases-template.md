# 测试用例

## 项目信息

| 项目 | 值 |
|------|-----|
| 项目名称 | {{PROJECT_NAME}} |
| 测试时间 | {{TEST_TIME}} |

---

## 单元测试

### 测试类列表

{{UNIT_TEST_CLASSES}}

### 测试用例详情

| 测试类 | 测试方法 | 测试场景 | 预期结果 | 状态 |
|--------|----------|----------|----------|------|
| {{TEST_CLASS}} | {{TEST_METHOD}} | {{SCENARIO}} | {{EXPECTED}} | {{STATUS}} |

---

## 集成测试

### 测试场景

{{INTEGRATION_TESTS}}

### 测试用例详情

| 场景 | 输入 | 预期输出 | 实际输出 | 状态 |
|------|------|----------|----------|------|
| {{SCENARIO}} | {{INPUT}} | {{EXPECTED}} | {{ACTUAL}} | {{STATUS}} |

---

## 边界测试

| 边界条件 | 测试数据 | 预期行为 | 状态 |
|----------|----------|----------|------|
| {{BOUNDARY}} | {{TEST_DATA}} | {{EXPECTED_BEHAVIOR}} | {{STATUS}} |

---

## 测试覆盖率

| 模块 | 行覆盖率 | 分支覆盖率 | 方法覆盖率 |
|------|----------|------------|------------|
| {{MODULE}} | {{LINE_COVERAGE}}% | {{BRANCH_COVERAGE}}% | {{METHOD_COVERAGE}}% |

---

## 测试报告

{{TEST_REPORT}}

---

*生成时间: {{GENERATE_TIME}}*
*生成方式: QClaw Dev Workflow - Phase 5*
