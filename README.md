# white-dev-workflow

完整的软件开发工作流 Skill，结合 TDD 流程、Karpathy 代码规范、三元代码审核，自动生成完整的项目文档。

[English](./README-en.md) | 中文

## 特性

- 🚀 **TDD 开发流程** - 测试驱动，规格先行
- 📐 **Karpathy 代码规范** - 简洁、精准、目标导向
- 👥 **三元代码审核** - 结构化、多维度代码评审
- 📄 **自动文档生成** - 需求/设计/开发/测试/评审全覆盖
- 📊 **使用统计追踪** - Skill 和 Agent 调用次数自动记录

## 工作流 Pipeline

```
Idea → Brainstorm → Plan → Subagent-Driven Build (TDD) → Code Review (三元) → Doc Generation → Finish
```

## 快速开始

```
用 white-dev-workflow 帮我创建一个 xxx 项目
```

## 文档模板

| 文档 | 文件名 | 说明 |
|------|--------|------|
| 需求文档 | `doc/01-requirements.md` | 功能需求、非功能需求、验收标准 |
| 设计文档 | `doc/02-design.md` | 架构设计、API 设计、数据模型 |
| 任务计划 | `doc/03-tasks.md` | 分任务实现计划 |
| 开发记录 | `doc/04-dev-log.md` | 开发过程日志 |
| 测试用例 | `doc/05-test-cases.md` | 单元测试、集成测试用例 |
| 代码评审 | `doc/06-code-review.md` | 三元审核报告 |
| 使用统计 | `doc/skill_agent_usage.md` | Skill/Agent 调用统计 |

## 依赖

- OpenClaw
- Subagent (Codex / Claude Code)
- Text File Skill

## License

MIT
