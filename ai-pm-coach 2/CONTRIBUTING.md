# 贡献指南

感谢你对 AI PM Coach 的关注！

## 🎯 贡献方式

### 报告问题

如果你发现了 bug 或有功能建议：

1. 搜索现有 Issues 确保问题未被报告
2. 创建新 Issue，包含：
   - 清晰的标题和描述
   - 复现步骤（如果是 bug）
   - 预期行为 vs 实际行为

### 提交代码

1. Fork 仓库
2. 创建分支 (`git checkout -b feature/amazing-feature`)
3. 进行更改
4. 提交更改 (`git commit -m "feat: add amazing feature"`)
5. 推送到 GitHub
6. 创建 Pull Request

---

## 📝 代码规范

### SKILL.md 规范

- 必须包含 `name` 和 `description`
- `metadata.hermes.runtime` 必须设置为 `subagent`
- 使用引导式语言，而非命令式语言

### 对话设计规范

**好的引导**：
- 提问而非陈述
- 一步步深入
- 让用户做决策
- 记录用户的选择

**避免**：
- 直接给答案
- 假设用户需求
- 跳过决策节点
- 替用户做决定

---

## 🏗️ 项目结构

```
ai-pm-coach/
├── SKILL.md           # 主文档（必需）
├── README.md          # 项目说明
├── CHANGELOG.md       # 变更日志
├── CONTRIBUTING.md    # 贡献指南
├── ARCHITECTURE.md    # 架构说明
├── GUIDE.md           # 使用指南
├── LICENSE            # 许可证
├── examples/          # 示例对话
└── skills/            # 内部 Skills
```

---

## 🎯 设计原则

贡献时请遵循以下原则：

### 1. 教练思维

- 不替用户做决策
- 引导用户思考
- 在关键节点暂停

### 2. 留白设计

- 不追求解决所有问题
- 让用户在协作中找到价值
- 用户才是导演

### 3. 渐进式引导

- 从简单问题开始
- 逐步深入
- 让用户建立信心

---

## ✅ 检查清单

提交 PR 前请确认：

- [ ] 文档已更新
- [ ] 提交信息清晰
- [ ] 没有引入敏感信息
- [ ] 遵循教练式引导原则

---

## 📮 联系方式

- 问题：GitHub Issues
- 讨论：GitHub Discussions

---

感谢你的贡献！❤️
