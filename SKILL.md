---
name: ai-pm-prd-suite
description: "AI 产品经理 PRD 工具套件。用于：(1) 从产品构想生成生产级 PRD 文档；(2) 验证 PRD 是否符合开发友好标准；(3) 生成可运行的前端原型代码；(4) 设计 AI 产品 Benchmark 与 Eval 框架；(5) 将痛点转化为完整 PRD。触发词：PRD、产品需求文档、原型、Benchmark、Eval、痛点分析、需求验证。"
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

## 核心能力矩阵

| 能力 | 命令 | 用途 |
|------|------|------|
| PRD 生成 | `/prd-generate` | 产品构想 → 生产级 PRD |
| PRD 验证 | `/prd-validate` | 检查 PRD 开发友好性 |
| 原型生成 | `/prototype` | PRD → 可运行前端代码 |
| Benchmark 设计 | `/benchmark` | 定义可量化评测维度 |
| Eval 框架 | `/eval-framework` | 生成 Eval 飞轮配置 |
| 痛点转化 | `/pain-to-prd` | 痛点分析 → 完整 PRD |

---

## 1. PRD 生成 (`/prd-generate`)

### 输入格式

```json
{
  "product_idea": "产品构想描述",
  "target_users": ["目标用户1", "目标用户2"],
  "constraints": ["约束条件1", "约束条件2"]
}
```

### 输出结构

必须严格输出以下 7 个模块：

```markdown
# 需求文档

## 1. 应用概述
- 应用名称
- 应用描述

## 2. 用户与使用场景
- 目标用户
- 核心使用场景

## 3. 页面结构与功能说明
### 3.1 整体页面结构（树状文本结构图）
### 3.2 全局视觉与交互规范
### 3.x 各区块详细说明

## 4. 业务规则与逻辑

## 5. 异常与边界情况（表格）

## 6. 验收标准（列表）

## 7. 本期不实现功能
```

### 撰写原则

**前端友好性：**
- 使用前端语言：`overflow-x: hidden`, `backdrop-filter`, `z-index: 9999`
- 数据驱动：定义 `TERMS` 等 JS 对象，数量动态计算
- 预设 CSS 类名：`.term`, `.term-popup`, `.card-hover`

**交互定义：**
- 定位算法：水平居中、边界溢出修正、垂直翻转
- 状态机：默认态 → Hover 态 → 激活态 → 点击态
- 动画参数：类型、缓动、时长、延迟 + `prefers-reduced-motion` 降级

**响应式断点：**
```css
@media (max-width: 900px) { /* 平板 */ }
@media (max-width: 700px) { /* 手机 */ }
```

---

## 2. PRD 验证 (`/prd-validate`)

### 检查维度

| 维度 | 检查项 | 权重 |
|------|--------|------|
| 完整性 | 7 个模块是否齐全 | 20% |
| 开发友好 | CSS 类名、动画参数、响应式断点 | 30% |
| 逻辑闭环 | 跨模块联动、事件冒泡处理 | 25% |
| 异常覆盖 | 边界情况表格完整性 | 25% |

### 输出格式

```json
{
  "score": 85,
  "grade": "B",
  "issues": [
    {
      "module": "3.2",
      "severity": "medium",
      "issue": "缺少 prefers-reduced-motion 降级方案",
      "suggestion": "添加 `@media (prefers-reduced-motion: reduce)` 样式"
    }
  ],
  "passed": false
}
```

---

## 3. 原型生成 (`/prototype`)

### 输入

PRD Markdown 文档

### 输出目录结构

```
prototype/
├── index.html      # 主页面
├── styles.css      # 样式（含响应式）
├── main.js         # 交互逻辑
└── data.js         # 数据结构（动态计算）
```

### 核心实现

**自动提取规则：**
1. 从 PRD 提取 CSS 类名 → 生成 `styles.css`
2. 从 PRD 提取数据结构 → 生成 `data.js`
3. 从 PRD 提取交互逻辑 → 生成 `main.js`
4. 从 PRD 提取动画参数 → 添加 CSS 动画 + `prefers-reduced-motion`

**示例输出：**

```javascript
// data.js
const TERMS = {
  prototype: {
    zh: "原型",
    en: "Prototype",
    definition: "通过 Vibe Coding 缩短验证周期",
    examples: ["用 Claude 生成 Landing Page", "用 v0 生成组件"]
  },
  // ...
};

// 动态计算数量
const termCount = Object.keys(TERMS).length;
```

---

## 4. Benchmark 设计 (`/benchmark`)

### 输入

```json
{
  "product_type": "AI 问答助手",
  "scenarios": ["知识问答", "多轮对话", "创意生成"]
}
```

### 输出框架

```json
{
  "product_name": "AI 问答助手",
  "benchmarks": [
    {
      "dimension": "准确性",
      "description": "回答的事实正确程度",
      "metrics": [
        {
          "name": "事实正确率",
          "definition": "答案中事实陈述的正确比例",
          "measurement": "人工标注 / 自动化验证",
          "threshold": "≥ 90%"
        },
        {
          "name": "引用准确率",
          "definition": "引用来源与内容匹配的比例",
          "measurement": "URL 有效性检查",
          "threshold": "≥ 95%"
        }
      ]
    },
    {
      "dimension": "有用性",
      "metrics": ["问题解决率", "用户满意度"],
      "threshold": "≥ 85%"
    },
    {
      "dimension": "安全性",
      "metrics": ["有害内容率", "偏见输出率"],
      "threshold": "≤ 0.1%"
    }
  ]
}
```

---

## 5. Eval 框架 (`/eval-framework`)

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

### 输出配置

```yaml
eval_framework:
  product: "AI 问答助手"
  
  observe:
    - event: "user_query"
      fields: ["query", "timestamp", "user_id"]
    - event: "model_response"
      fields: ["response", "latency", "tokens"]
    - event: "user_feedback"
      fields: ["rating", "comment", "action"]
  
  analyze:
    signals:
      - name: "response_quality"
        source: "user_feedback.rating"
        aggregation: "avg"
      - name: "latency_p95"
        source: "model_response.latency"
        aggregation: "p95"
  
  evaluate:
    rules:
      - name: "quality_gate"
        condition: "response_quality >= 4.0"
        action: "pass"
      - name: "latency_gate"
        condition: "latency_p95 <= 2000"
        action: "alert"
  
  improve:
    triggers:
      - condition: "quality_gate_failed"
        action: "trigger_retraining"
      - condition: "latency_gate_failed"
        action: "scale_infrastructure"
```

---

## 6. 痛点转化 (`/pain-to-prd`)

### 与 auto-prd-hunter 联动

```
auto-prd-hunter          pain-to-prd
      ↓                       ↓
  抓取痛点              痛点 → PRD 转换
      ↓                       ↓
pain_points[]          完整 7 模块 PRD
user_stories[]
mvp_features[]
```

### 输入格式

```json
{
  "pain_points": [
    {
      "id": "PP-001",
      "title": "AI 回答不够准确",
      "severity": "high",
      "context": "用户反馈 AI 经常给出错误答案",
      "sources": [{"platform": "Reddit", "url": "...", "quote": "..."}]
    }
  ],
  "user_stories": [...],
  "mvp_features": [...]
}
```

### 输出

完整的 7 模块 PRD 文档，包含：
- 痛点映射到用户故事
- 用户故事映射到 MVP 功能
- MVP 功能映射到开发任务

---

## 工作流示例

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

## 参考文档

- **PRD 模板**: 见 `references/prd_template.md`
- **Benchmark 模式库**: 见 `references/benchmark_patterns.md`
- **Eval 框架设计**: 见 `references/eval_framework.md`

---

## 脚本说明

| 脚本 | 功能 |
|------|------|
| `scripts/generate_prd.py` | PRD 生成核心逻辑 |
| `scripts/validate_prd.py` | PRD 验证检查器 |
| `scripts/pain_to_prd.py` | 痛点到 PRD 转换 |

---

## 约束

1. PRD 必须包含全部 7 个模块
2. 所有交互必须定义状态机
3. 所有动画必须包含 `prefers-reduced-motion` 降级
4. 数据必须动态计算，禁止硬编码数量
5. 异常情况必须使用表格格式
