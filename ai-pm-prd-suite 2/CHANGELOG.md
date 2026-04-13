# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-04-14

### Added

- **PRD 生成功能** (`/prd-generate`)
  - 支持从产品构想生成完整 7 模块 PRD
  - 自动生成树状页面结构图
  - 自动定义 CSS 类名、动画参数、响应式断点

- **PRD 验证功能** (`/prd-validate`)
  - 完整性检查（7 模块）
  - 开发友好性检查（CSS 类名、动画参数）
  - 逻辑闭环检查（跨模块联动）
  - 异常覆盖检查（边界情况表格）
  - 输出评分和问题列表

- **原型生成功能** (`/prototype`)
  - PRD → HTML/CSS/JS 前端代码
  - 数据驱动的动态渲染
  - 响应式布局支持
  - `prefers-reduced-motion` 降级支持

- **Benchmark 设计功能** (`/benchmark`)
  - 场景化 Benchmark 模板
  - 可量化评测维度定义
  - AI 产品专用评测框架

- **Eval 框架生成功能** (`/eval-framework`)
  - Eval 飞轮配置生成
  - Observe → Analyze → Evaluate → Improve 完整流程
  - YAML 配置输出

- **痛点转化功能** (`/pain-to-prd`)
  - 与 auto-prd-hunter 联动
  - 痛点数据 → 完整 PRD 转换
  - 痛点映射到用户故事和功能

### Documentation

- 添加 README.md
- 添加 PRD 模板文档
- 添加 Benchmark 模式库
- 添加 Eval 框架设计文档

### Scripts

- `scripts/generate_prd.py` - PRD 生成核心逻辑
- `scripts/validate_prd.py` - PRD 验证检查器
- `scripts/pain_to_prd.py` - 痛点到 PRD 转换

### Assets

- 前端原型模板（HTML/CSS/JS）
- 数据配置示例

---

## [Unreleased]

### Planned

- 支持多语言 PRD 生成
- 集成更多数据源（用户反馈平台）
- AI 自动优化 PRD 建议
- 团队协作功能
