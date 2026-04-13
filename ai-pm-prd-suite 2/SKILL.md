---
name: ai-pm-prd-suite
description: "AI 产品经理 PRD 工具套件。用于：(1) 生成生产级 PRD 文档；(2) 验证 PRD 开发友好性；(3) 生成前端原型代码；(4) 设计 Benchmark 评测框架；(5) 生成 Eval 飞轮配置；(6) 转化痛点为 PRD。触发词：PRD、产品需求文档、原型、Benchmark、Eval、痛点、需求验证、验收标准。"
metadata:
  hermes:
    display_name: "AI PM PRD 套件"
    tags: [PRD, 产品经理, AI, Benchmark, Eval, 原型, 需求文档]
    category: productivity
    author: "OpenClaw"
    version: "1.0.0"
---

# AI PM PRD Suite

一站式 AI 产品经理 PRD 工具套件，覆盖从「产品构想」到「开发就绪」的完整链路。

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

## 能力一：PRD 生成 (`/prd`)

### 功能描述
根据产品构想生成生产级 PRD 文档，包含完整的 7 个模块。

### 使用方式

```
/prd <产品构想>
```

### 输入示例

**简单模式：**
```
/prd AI 知识库可视化产品
```

**详细模式：**
```
/prd
产品名称：智能周报生成器
目标用户：产品经理、工程师、运营
核心功能：
- 自动汇总本周工作
- 生成周报草稿
- 支持多模板切换
约束条件：前端可直接开发，无逻辑漏洞
```

### 输出结构

```markdown
# 需求文档

## 1. 应用概述
- 应用名称
- 应用描述

## 2. 用户与使用场景
- 目标用户
- 核心使用场景

## 3. 页面结构与功能说明
- 3.1 整体页面结构（树状图）
- 3.2 全局视觉与交互规范
- 3.x 各区块详细说明

## 4. 业务规则与逻辑

## 5. 异常与边界情况（表格）

## 6. 验收标准（列表）

## 7. 本期不实现功能
```

---

## 能力二：PRD 验证 (`/prd-validate`)

### 功能描述
检查 PRD 是否符合开发友好标准，输出评分和改进建议。

### 使用方式

```
/prd-validate
/prd-validate --file <文件路径>
```

### 检查维度

| 维度 | 权重 | 检查项 |
|------|------|--------|
| 完整性 | 20% | 7 个模块是否齐全 |
| 开发友好 | 30% | CSS 类名、动画参数、响应式断点 |
| 逻辑闭环 | 25% | 跨模块联动、事件冒泡处理 |
| 异常覆盖 | 25% | 边界情况表格完整性 |

### 输出示例

```
PRD 验证结果
============================================================
评分：85/100
等级：B
状态：✅ 通过

发现问题 (2 个)：
------------------------------------------------------------
[MEDIUM] 3.2: 缺少 prefers-reduced-motion 降级方案
    建议：添加 @media (prefers-reduced-motion: reduce) 样式

[LOW] 5: 异常表格未覆盖响应式断点场景
    建议：添加屏幕宽度相关异常处理
```

---

## 能力三：原型生成 (`/prototype`)

### 功能描述
将 PRD 转换为可运行的前端代码（HTML/CSS/JS）。

### 使用方式

```
/prototype
/prototype --output <输出目录>
```

### 输出文件

```
prototype/
├── index.html      # 主页面
├── styles.css      # 样式（含响应式）
├── main.js         # 交互逻辑
└── data.js         # 数据结构
```

### 特性

- 数据驱动渲染，不硬编码数量
- 响应式布局支持（桌面/平板/手机）
- `prefers-reduced-motion` 动画降级
- CSS 类名预设与 PRD 一致

### 运行方式

```bash
cd prototype
python3 -m http.server 8080
# 访问 http://localhost:8080
```

---

## 能力四：Benchmark 设计 (`/benchmark`)

### 功能描述
为 AI 产品定义可量化的评测维度和指标体系。

### 使用方式

```
/benchmark <产品类型> --scenarios <场景列表>
```

### 输入示例

```
/benchmark AI 问答助手 --scenarios 知识问答,多轮对话,创意生成
```

### 输出示例

```json
{
  "product_name": "AI 问答助手",
  "benchmark_set": [
    {
      "dimension": "准确性",
      "weight": 0.4,
      "metrics": [
        {
          "name": "事实正确率",
          "definition": "答案中事实陈述的正确比例",
          "threshold": "≥ 90%"
        }
      ]
    },
    {
      "dimension": "有用性",
      "weight": 0.3,
      "metrics": [
        {
          "name": "问题解决率",
          "threshold": "≥ 80%"
        }
      ]
    }
  ]
}
```

### 预设维度

| 维度 | 适用场景 | 常用指标 |
|------|----------|----------|
| 准确性 | 知识问答、代码生成 | 事实正确率、引用准确率 |
| 有用性 | 所有 AI 产品 | 问题解决率、用户满意度 |
| 安全性 | 内容生成、对话 | 有害内容率、偏见输出率 |
| 效率 | 实时交互 | 首字延迟、生成速度 |

---

## 能力五：Eval 框架 (`/eval`)

### 功能描述
生成完整的 Eval 飞轮配置，包含观察、分析、评估、改进四个阶段。

### 使用方式

```
/eval <产品名称>
```

### Eval 飞轮模型

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ Observe │ -> │ Analyze │ -> │ Evaluate│ -> │ Improve │
│  观察   │    │  分析   │    │  评估   │    │  改进   │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
     │              │              │              │
     ▼              ▼              ▼              ▼
  日志采集       信号提取       标准执行       迭代优化
```

### 输出格式

```yaml
eval_framework:
  product: "AI 问答助手"
  
  observe:
    events:
      - user_query
      - model_response
      - user_feedback
      
  analyze:
    signals:
      - response_quality
      - latency_p95
      
  evaluate:
    rules:
      - quality_gate
      - latency_gate
      
  improve:
    triggers:
      - trigger_retraining
      - scale_infrastructure
```

---

## 能力六：痛点转化 (`/pain-to-prd`)

### 功能描述
将痛点数据转换为完整的 PRD 文档，可与 auto-prd-hunter 联动。

### 使用方式

**方式一：联动 auto-prd-hunter**
```
/auto-prd-hunter 远程办公痛点
/pain-to-prd
```

**方式二：直接输入痛点**
```
/pain-to-prd
{
  "pain_points": [
    {
      "id": "PP-001",
      "title": "AI 回答不够准确",
      "severity": "high"
    }
  ]
}
```

### 转化流程

```
痛点数据 → 用户故事 → MVP 功能 → PRD 文档
    PP-001      US-001      F-001     7 模块
```

---

## 工作流示例

### 场景一：从 0 到 1 做新产品

```
用户想法 → /prd → /prd-validate → /prototype → 可交互原型
```

### 场景二：竞品分析驱动

```
/auto-prd-hunter → /pain-to-prd → /prototype → 前端开发
```

### 场景三：AI 产品评测

```
/benchmark → /eval → 部署评测流水线
```

---

## 参考文档

| 文档 | 位置 | 用途 |
|------|------|------|
| PRD 模板 | `references/prd_template.md` | 撰写 PRD 参考 |
| Benchmark 模式库 | `references/benchmark_patterns.md` | 设计评测维度 |
| Eval 框架设计 | `references/eval_framework.md` | 理解 Eval 飞轮 |

---

## 约束

1. PRD 必须包含全部 7 个模块
2. 所有交互必须定义状态机
3. 所有动画必须包含 `prefers-reduced-motion` 降级
4. 数据必须动态计算，禁止硬编码
5. 异常情况必须使用表格格式
