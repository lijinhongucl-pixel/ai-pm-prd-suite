# AI PM PRD Suite

> 一站式 AI 产品经理 PRD 工具套件，覆盖从「产品构想」到「开发就绪」的完整链路。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skill Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/openclaw/ai-pm-prd-suite)
[![OpenClaw Compatible](https://img.shields.io/badge/OpenClaw-Compatible-green.svg)](https://openclaw.ai)

## ✨ 核心能力

| 能力 | 命令 | 用途 |
|------|------|------|
| 📝 PRD 生成 | `/prd-generate` | 产品构想 → 生产级 PRD |
| ✅ PRD 验证 | `/prd-validate` | 检查 PRD 开发友好性 |
| 🎨 原型生成 | `/prototype` | PRD → 可运行前端代码 |
| 📊 Benchmark 设计 | `/benchmark` | 定义可量化评测维度 |
| 🔄 Eval 框架 | `/eval-framework` | 生成 Eval 飞轮配置 |
| 🎯 痛点转化 | `/pain-to-prd` | 痛点分析 → 完整 PRD |

---

## 🚀 快速开始

### 安装

#### 方式一：OpenClaw / Hermes Agent

```bash
# 将 skill 目录复制到 skills 目录
cp -r ai-pm-prd-suite ~/.hermes/skills/
# 或
cp -r ai-pm-prd-suite ~/.openclaw/skills/
```

#### 方式二：使用 .skill 文件

```bash
# 下载 .skill 文件后导入
hermes skills install ai-pm-prd-suite.skill
```

### 使用

启动 Agent 后，发送以下命令：

```
/prd-generate 我想要一个 AI 知识库可视化产品
```

---

## 📖 功能详解

### 1. PRD 生成 (`/prd-generate`**

```json
{
  "product_idea": "AI 知识库可视化产品",
  "target_users": ["AI PM", "产品经理"],
  "constraints": ["前端可直接开发", "无逻辑漏洞"]
}
```

**输出结构（7 个模块）：**

1. **应用概述** - 名称、描述
2. **用户与使用场景** - 目标用户、核心场景
3. **页面结构与功能说明** - 树状结构图、交互规范
4. **业务规则与逻辑** - 可复用逻辑
5. **异常与边界情况** - 表格形式
6. **验收标准** - 可转化为测试用例
7. **本期不实现功能** - 需求边界管理

---

### 2. PRD 验证 (`/prd-validate`)

**检查维度：**

| 维度 | 权重 | 检查项 |
|------|------|--------|
| 完整性 | 20% | 7 个模块是否齐全 |
| 开发友好 | 30% | CSS 类名、动画参数、响应式断点 |
| 逻辑闭环 | 25% | 跨模块联动、事件冒泡处理 |
| 异常覆盖 | 25% | 边界情况表格完整性 |

**输出示例：**

```json
{
  "score": 85,
  "grade": "B",
  "issues": [
    {
      "module": "3.2",
      "severity": "medium",
      "issue": "缺少 prefers-reduced-motion 降级方案"
    }
  ]
}
```

---

### 3. 原型生成 (`/prototype`)

**输入：** PRD Markdown 文档

**输出：**

```
prototype/
├── index.html      # 主页面
├── styles.css      # 样式（含响应式）
├── main.js         # 交互逻辑
└── data.js         # 数据结构（动态计算）
```

---

### 4. Benchmark 设计 (`/benchmark`)

**输入：**

```json
{
  "product_type": "AI 问答助手",
  "scenarios": ["知识问答", "多轮对话"]
}
```

**输出：**

```json
{
  "benchmarks": [
    {
      "dimension": "准确性",
      "metrics": ["事实正确率", "引用准确率"],
      "threshold": "≥ 90%"
    }
  ]
}
```

---

### 5. Eval 框架 (`/eval-framework`)

**Eval 飞轮模型：**

```
Observe → Analyze → Evaluate → Improve
   ↓         ↓          ↓          ↓
日志采集   信号提取   标准执行   迭代优化
```

---

### 6. 痛点转化 (`/pain-to-prd`)

与 `auto-prd-hunter` 联动：

```
auto-prd-hunter          pain-to-prd
      ↓                       ↓
  抓取痛点              痛点 → PRD 转换
      ↓                       ↓
pain_points[]          完整 7 模块 PRD
```

---

## 📁 项目结构

```
ai-pm-prd-suite/
├── SKILL.md                    # Skill 主文档
├── README.md                   # 项目说明
├── LICENSE                     # MIT 许可证
├── CHANGELOG.md                # 变更日志
├── CONTRIBUTING.md             # 贡献指南
├── .gitignore                  # Git 忽略文件
├── scripts/                    # 脚本目录
│   ├── generate_prd.py         # PRD 生成器
│   ├── validate_prd.py         # PRD 验证器
│   └── pain_to_prd.py          # 痛点转 PRD
├── references/                 # 参考文档
│   ├── prd_template.md         # PRD 模板
│   ├── benchmark_patterns.md   # Benchmark 模式库
│   └── eval_framework.md       # Eval 框架设计
├── assets/                     # 资产文件
│   ├── index.html              # 原型模板
│   ├── styles.css              # 样式文件
│   ├── main.js                 # 交互逻辑
│   └── data.js                 # 数据配置
└── examples/                   # 示例目录
    ├── example-prd.md          # 示例 PRD
    ├── example-benchmark.json  # 示例 Benchmark
    └── example-eval.yaml       # 示例 Eval 配置
```

---

## 🎯 使用场景

### 场景 1：从 0 到 1 做新产品

```
用户输入想法 → /prd-generate → /prd-validate → /prototype → 可交互原型
```

### 场景 2：竞品分析驱动

```
auto-prd-hunter 抓竞品痛点 → /pain-to-prd → /prototype → 前端直接开发
```

### 场景 3：AI 产品评测

```
/benchmark → /eval-framework → 自动化评测流水线
```

---

## 🤝 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

### 贡献方式

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

---

## 📝 变更日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解版本历史。

---

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

---

## 🙏 致谢

- 灵感来源：AI PM 核心能力方法论（Prototype、Benchmark、Eval）
- 支持平台：OpenClaw、Hermes Agent

---

## 📮 联系方式

- 问题反馈：[GitHub Issues](https://github.com/openclaw/ai-pm-prd-suite/issues)
- 讨论：[GitHub Discussions](https://github.com/openclaw/ai-pm-prd-suite/discussions)

---

<p align="center">
  Made with ❤️ by OpenClaw Team
</p>
