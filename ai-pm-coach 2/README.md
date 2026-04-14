# AI PM Coach

> 我是教练，不是工具。我引导你思考，不替你做决策。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/openclaw/ai-pm-coach)
[![OpenClaw Compatible](https://img.shields.io/badge/OpenClaw-Compatible-green.svg)](https://openclaw.ai)

---

## 这是什么？

AI PM Coach 是一个 **Sub Agent**，通过引导式对话帮助 PM 完成 AI 产品设计。

与传统的"一键生成"工具不同，它：

- ❌ 不替你做决策
- ✅ 引导你思考
- ✅ 在关键节点让你选择
- ✅ 让你成为真正的"导演"

---

## 核心理念

```
传统工具：用户 → 命令 → AI输出 → 用户被动接收

AI PM Coach：用户 ↔ 教练式对话 ↔ 用户做决策
```

---

## 快速开始

### 安装

```bash
cp -r ai-pm-coach ~/.openclaw/skills/
# 重启 Agent
```

### 开始对话

```
用户：我想设计一个 AI 客服助手

教练：很好！让我们一步步分析。首先，这个产品要解决什么核心问题？

用户：客服响应太慢，用户等很久

教练：明白了。这个问题影响有多大？

...
```

---

## 工作流程

```
痛点诊断 → AI 适用性评估 → 能力边界定义 → 置信度设计 → 幻觉应对 → PRD 整合
   ↓            ↓              ↓             ↓            ↓          ↓
 澄清问题     评分判断       边界确认       阈值设置     容忍度定义   决策汇总
```

---

## 与传统工具的区别

| 传统工具 | AI PM Coach |
|----------|-------------|
| 命令-输出模式 | 对话-引导模式 |
| AI 替你做决策 | 你做决策，AI 引导 |
| 输出即最终结果 | 输出是你的决策汇总 |
| 用户是使用者 | 用户是学习者 |
| 单次交互 | 持续对话 |

---

## 决策节点

在以下节点，你需要做出选择：

| 节点 | 你需要决策 |
|------|-----------|
| 痛点确认 | 是否值得用 AI 解决？ |
| 边界确认 | AI 能做什么、不能做什么？ |
| 阈值设置 | 置信度设多少？转人工比例上限？ |
| 容忍度定义 | 什么错误可以接受？ |
| 责任划分 | AI 出错谁负责？ |

---

## 内部架构

本 Sub Agent 内部包装 5 个 Skill：

| Skill | 功能 |
|-------|------|
| pain-check-skill | 痛点评估 |
| boundary-skill | 边界定义 |
| confidence-skill | 置信度设计 |
| hallucination-skill | 幻觉应对 |
| prd-skill | PRD 生成 |

**重要**：这些 Skill 不直接暴露给用户，由 Sub Agent 内部调用。

---

## 适用场景

### 适合 AI PM Coach
- 用户不确定如何设计 AI 产品
- 需要学习和引导
- 完整的产品设计流程

### 适合传统工具
- 用户清楚知道自己要什么
- 需要快速输出文档
- 单点问题咨询

---

## 项目结构

```
ai-pm-coach/
├── SKILL.md              # Sub Agent 主文档
├── README.md             # 项目说明
├── CHANGELOG.md          # 变更日志
├── CONTRIBUTING.md       # 贡献指南
├── ARCHITECTURE.md       # 架构说明
├── GUIDE.md              # 使用指南
├── LICENSE               # MIT 许可证
├── examples/             # 示例对话
└── skills/               # 内部 Skills
    ├── pain-check-skill/
    ├── boundary-skill/
    ├── confidence-skill/
    ├── hallucination-skill/
    └── prd-skill/
```

---

## 许可证

MIT License

---

## 贡献

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)

---

> 我是教练，不是替你做作业的人。所有的决策，都需要你来确认。因为这是你的产品，你才是导演。

---

<p align="center">
  Made with ❤️ by OpenClaw Team
</p>
