# 内部 Skill：PRD 整合 (prd-skill)

> 此 Skill 仅供 Sub Agent 内部调用，不直接暴露给用户

---

## 功能

整合所有讨论，生成最终 PRD 文档。

---

## 输入格式

```json
{
  "product": "AI 客服助手",
  "decisions": {
    "pain_point": {
      "problem": "客服响应太慢",
      "impact": "70% 用户抱怨",
      "current_solution": "增加人工客服",
      "user_expectation": "秒级响应"
    },
    "ai_suitability": {
      "score": 20,
      "conclusion": "适合"
    },
    "boundary": {
      "ai_good_at": ["FAQ", "订单查询"],
      "ai_need_help": ["复杂投诉"],
      "ai_must_retreat": ["法律问题"]
    },
    "confidence": {
      "threshold": 0.7,
      "transfer_rate_limit": 0.2
    },
    "hallucination": {
      "fact_error_tolerance": "zero",
      "prevention": ["引用溯源"]
    }
  }
}
```

---

## 输出格式

```markdown
# AI 原生 PRD

## 产品：AI 客服助手

---

## 1. 产品定位

### 核心问题
客服响应太慢，70% 用户抱怨

### AI 角色
辅助 + 主导混合模式

---

## 2. AI 能力边界声明

### ✅ AI 擅长的领域
- FAQ 类问题
- 订单状态查询

### ⚠️ AI 需要人工辅助的领域
- 复杂投诉

### ❌ AI 必须撤退的领域
- 法律问题

---

## 3. 置信度机制

- 置信度阈值：0.7
- 转人工比例上限：20%

---

## 4. 幻觉应对策略

- 事实错误：零容忍
- 预防机制：引用溯源

---

## 5. 验收标准

- AI 处理比例 ≥ 70%
- 用户满意度 ≥ 80%
- 转人工比例 ≤ 20%

---

## 6. 人类决策锚点

以下决策由 PM 确认：
- AI 能力边界
- 置信度阈值
- 幻觉容忍度

---

## 决策记录

| 节点 | 决策 | PM 确认 |
|------|------|---------|
| AI 适用性 | 适合 | ✅ |
| 能力边界 | 已定义 | ✅ |
| 置信度阈值 | 0.7 | ✅ |
| 幻觉容忍度 | 事实错误零容忍 | ✅ |
```

---

## 使用示例

```
教练：好的，让我整合所有讨论生成 PRD...

[内部调用 prd-skill]

教练：PRD 已生成！这是我们的讨论结果：

      [显示 PRD 摘要]

      你确认吗？有需要修改的吗？
```
