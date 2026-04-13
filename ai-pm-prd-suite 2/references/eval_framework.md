# Eval 框架设计

本文档定义 Eval 飞轮的设计模式和实现规范。

---

## Eval 飞轮模型

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│    │ Observe │ -> │ Analyze │ -> │ Evaluate│ -> │ Improve │
│    │  观察   │    │  分析   │    │  评估   │    │  改进   │
│    └─────────┘    └─────────┘    └─────────┘    └─────────┘
│         │              │              │              │
│         ▼              ▼              ▼              ▼
│      日志采集       信号提取       标准执行       迭代优化
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 四阶段详解

### 1. Observe（观察）

**目标**：采集用户与产品交互的原始数据

**数据源**：
- 用户查询日志
- 模型响应日志
- 用户行为日志（点击、停留、滚动）
- 用户反馈日志（点赞、点踩、评论）

**事件设计示例**：

```yaml
observe:
  events:
    - name: "user_query"
      fields:
        - query: string        # 用户输入
        - timestamp: datetime  # 时间戳
        - user_id: string      # 用户标识
        - session_id: string   # 会话标识
        - context: object      # 上下文信息
      
    - name: "model_response"
      fields:
        - response: string      # 模型输出
        - latency_ms: int       # 响应延迟
        - tokens_input: int     # 输入 token 数
        - tokens_output: int    # 输出 token 数
        - model_version: string # 模型版本
        
    - name: "user_feedback"
      fields:
        - rating: int          # 评分 1-5
        - action: string       # like/dislike/none
        - comment: string      # 文字评论
```

---

### 2. Analyze（分析）

**目标**：从原始数据中提取有意义的信号

**信号类型**：

| 信号类型 | 示例 | 计算方法 |
|----------|------|----------|
| 质量信号 | 响应质量评分 | `avg(user_feedback.rating)` |
| 效率信号 | P95 延迟 | `p95(model_response.latency_ms)` |
| 行为信号 | 追问率 | `count(second_query) / count(first_query)` |
| 业务信号 | 转化率 | `count(conversion) / count(session)` |

**信号提取配置**：

```yaml
analyze:
  signals:
    - name: "response_quality"
      source: "user_feedback.rating"
      aggregation: "avg"
      window: "7d"
      
    - name: "latency_p95"
      source: "model_response.latency_ms"
      aggregation: "p95"
      window: "1d"
      
    - name: "follow_up_rate"
      source: "session.query_count"
      aggregation: "avg"
      filter: "query_count > 1"
      window: "7d"
```

---

### 3. Evaluate（评估）

**目标**：基于信号判断产品是否达标

**评估规则**：

```yaml
evaluate:
  rules:
    - name: "quality_gate"
      description: "响应质量必须达标"
      condition: "response_quality >= 4.0"
      severity: "critical"
      action:
        pass: "continue"
        fail: "alert + trigger_investigation"
        
    - name: "latency_gate"
      description: "P95 延迟必须在阈值内"
      condition: "latency_p95 <= 2000"
      severity: "warning"
      action:
        pass: "continue"
        fail: "alert"
        
    - name: "safety_gate"
      description: "有害内容率必须极低"
      condition: "harmful_rate <= 0.001"
      severity: "critical"
      action:
        pass: "continue"
        fail: "immediate_rollback"
```

---

### 4. Improve（改进）

**目标**：基于评估结果触发改进动作

**改进类型**：

| 改进类型 | 触发条件 | 改进动作 |
|----------|----------|----------|
| 模型优化 | 质量下降 | 触发 fine-tuning |
| 提示词优化 | 特定场景表现差 | 更新 system prompt |
| 基础设施 | 延迟超标 | 扩容 / 优化推理 |
| 内容优化 | 引用不准确 | 更新知识库 |

**改进配置**：

```yaml
improve:
  triggers:
    - condition: "quality_gate.failed && trend == 'declining'"
      actions:
        - type: "trigger_retraining"
          params:
            dataset: "last_30d_feedback"
            strategy: "rlhf"
            
    - condition: "latency_gate.failed"
      actions:
        - type: "scale_infrastructure"
          params:
            scale_factor: 1.5
            
    - condition: "safety_gate.failed"
      actions:
        - type: "immediate_rollback"
          params:
            target_version: "previous_stable"
        - type: "notify_oncall"
          params:
            channel: "#ai-safety-alerts"
```

---

## Eval 框架完整配置示例

```yaml
eval_framework:
  product: "AI 问答助手"
  version: "v1.0"
  
  # 观察阶段
  observe:
    events:
      - user_query
      - model_response
      - user_feedback
    storage:
      type: "clickhouse"
      retention: "90d"
      
  # 分析阶段
  analyze:
    signals:
      - response_quality
      - latency_p95
      - follow_up_rate
      - helpfulness_score
    schedule: "every_1h"
    
  # 评估阶段
  evaluate:
    rules:
      - quality_gate
      - latency_gate
      - safety_gate
    dashboard: "grafana://eval-dashboard"
    
  # 改进阶段
  improve:
    triggers:
      - quality_decline_trigger
      - latency_trigger
      - safety_trigger
    automation_level: "semi_auto"  # full_auto / semi_auto / manual
    approval_required: true
```

---

## Eval 飞轮最佳实践

### 1. 渐进式自动化
- 初期：手动分析 → 手动改进
- 中期：自动分析 → 人工审核改进
- 成熟：全自动闭环（关键场景需人工确认）

### 2. 信号分层
- **L1 原始信号**：直接采集的原始数据
- **L2 聚合信号**：统计汇总后的指标
- **L3 业务信号**：与业务目标关联的指标

### 3. 灰度发布
- 新版本先在小流量上验证
- 通过 Eval 评估后再逐步放量
- 异常时自动回滚

### 4. 可解释性
- 每个信号都能追溯到原始事件
- 每个改进动作都有明确触发原因
- 保留完整的改进历史记录
