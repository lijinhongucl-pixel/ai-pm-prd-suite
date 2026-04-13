# Contributing to AI PM PRD Suite

感谢你有兴趣为 AI PM PRD Suite 做贡献！

## 🎯 贡献方式

### 报告问题

如果你发现了 bug 或有功能建议：

1. 搜索 [现有 Issues](https://github.com/openclaw/ai-pm-prd-suite/issues) 确保问题未被报告
2. 创建新 Issue，包含：
   - 清晰的标题和描述
   - 复现步骤（如果是 bug）
   - 预期行为 vs 实际行为
   - 截图或日志（如有帮助）

### 提交代码

1. **Fork 仓库**

   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-pm-prd-suite.git
   cd ai-pm-prd-suite
   ```

2. **创建分支**

   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **进行更改**

   - 遵循现有代码风格
   - 添加必要的注释
   - 更新相关文档

4. **提交更改**

   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```

   提交信息格式：
   - `feat:` 新功能
   - `fix:` Bug 修复
   - `docs:` 文档更新
   - `refactor:` 代码重构
   - `test:` 测试相关

5. **推送到 GitHub**

   ```bash
   git push origin feature/amazing-feature
   ```

6. **创建 Pull Request**

   - 描述你的更改
   - 关联相关 Issue
   - 等待代码审查

---

## 📝 代码规范

### Python 代码

- 遵循 PEP 8
- 使用类型提示
- 添加 docstring

```python
def generate_prd(idea: str, target_users: list = None) -> str:
    """
    生成 PRD 文档
    
    Args:
        idea: 产品构想描述
        target_users: 目标用户列表
    
    Returns:
        PRD Markdown 文档
    """
    pass
```

### Markdown 文档

- 使用标准 Markdown 格式
- 标题层级清晰
- 代码块指定语言

### SKILL.md 规范

- 必须包含 `name` 和 `description`
- `description` 应清晰描述触发场景
- 使用简洁的指令，避免冗余解释

---

## 🏗️ 项目结构

```
ai-pm-prd-suite/
├── SKILL.md           # 主文档（必需）
├── scripts/           # Python 脚本
├── references/        # 参考文档
├── assets/            # 静态资源
└── examples/          # 示例文件
```

---

## ✅ 检查清单

提交 PR 前请确认：

- [ ] 代码通过测试
- [ ] 文档已更新
- [ ] 提交信息清晰
- [ ] 没有引入敏感信息

---

## 📮 联系方式

- 问题：[GitHub Issues](https://github.com/openclaw/ai-pm-prd-suite/issues)
- 讨论：[GitHub Discussions](https://github.com/openclaw/ai-pm-prd-suite/discussions)

---

感谢你的贡献！❤️
