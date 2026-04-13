# AI PM PRD Suite

> 一站式 AI 产品经理 PRD 工具套件，覆盖从「产品构想」到「开发就绪」的完整链路。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skill Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/openclaw/ai-pm-prd-suite)
[![OpenClaw Compatible](https://img.shields.io/badge/OpenClaw-Compatible-green.svg)](https://openclaw.ai)

---

## 核心能力矩阵

```
┌─────────────────────────────────────────────────────────────┐
│                   AI PM PRD Suite                            │
│                  核心能力 × 核心命令                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📝 PRD 生成        /prd                    构想 → PRD      │
│  ✅ PRD 验证        /prd-validate           检查 → 评分      │
│  🎨 原型生成        /prototype              PRD → 代码       │
│  📊 Benchmark 设计  /benchmark              场景 → 评测      │
│  🔄 Eval 框架       /eval                   飞轮配置         │
│  🎯 痛点转化        /pain-to-prd            痛点 → PRD       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 快速开始

### 安装

```bash
# OpenClaw
cp -r ai-pm-prd-suite ~/.openclaw/skills/

# Hermes Agent
cp -r ai-pm-prd-suite ~/.hermes/skills/
```

### 使用

```
/prd AI 知识库可视化产品
```

---

## 📖 六大核心能力

### 1️⃣ PRD 生成 (`/prd`)

**功能**：根据产品构想生成生产级 PRD 文档

**输入**：
```
/prd AI 问答助手，面向产品经理
```

**输出**：完整的 7 模块 PRD 文档

---

### 2️⃣ PRD 验证 (`/prd-validate`)

**功能**：检查 PRD 开发友好性

**输入**：
```
/prd-validate
```

**输出**：评分 + 改进建议

---

### 3️⃣ 原型生成 (`/prototype`)

**功能**：PRD → 可运行前端代码

**输出**：
```
prototype/
├── index.html
├── styles.css
├── main.js
└── data.js
```

---

### 4️⃣ Benchmark 设计 (`/benchmark`)

**功能**：定义 AI 产品评测维度

**输入**：
```
/benchmark AI 问答助手 --scenarios 知识问答,多轮对话
```

**输出**：评测维度 + 指标体系

---

### 5️⃣ Eval 框架 (`/eval`)

**功能**：生成 Eval 飞轮配置

**飞轮模型**：
```
Observe → Analyze → Evaluate → Improve
   ↓         ↓          ↓          ↓
日志采集   信号提取   标准执行   迭代优化
```

---

### 6️⃣ 痛点转化 (`/pain-to-prd`)

**功能**：痛点数据 → 完整 PRD

**流程**：
```
痛点 → 用户故事 → MVP 功能 → PRD
```

---

## 📁 项目结构

```
ai-pm-prd-suite/
├── SKILL.md                    # Skill 主文档
├── README.md                   # 项目说明
├── LICENSE                     # MIT 许可证
├── scripts/                    # Python 脚本
│   ├── generate_prd.py
│   ├── validate_prd.py
│   └── pain_to_prd.py
├── references/                 # 参考文档
│   ├── prd_template.md
│   ├── benchmark_patterns.md
│   └── eval_framework.md
├── assets/                     # 前端原型模板
│   ├── index.html
│   ├── styles.css
│   ├── main.js
│   └── data.js
└── examples/                   # 示例文件
    ├── example-prd.md
    ├── example-benchmark.json
    └── example-eval.yaml
```

---

## 🎯 使用场景

### 场景一：从 0 到 1 做新产品

```
/prd → /prd-validate → /prototype
```

### 场景二：竞品分析驱动

```
/auto-prd-hunter → /pain-to-prd → /prototype
```

### 场景三：AI 产品评测

```
/benchmark → /eval
```

---

## 📄 许可证

MIT License

---

<p align="center">
  Made with ❤️ by OpenClaw Team
</p>
