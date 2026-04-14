# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-04-14

### Added

**核心架构**
- Sub Agent 架构设计
- 教练式引导对话模式
- 6 阶段工作流程

**内部 Skills**
- `pain-check-skill`：痛点评估工具
- `boundary-skill`：能力边界定义工具
- `confidence-skill`：置信度设计工具
- `hallucination-skill`：幻觉应对工具
- `prd-skill`：PRD 整合工具

**决策节点系统**
- 痛点确认节点
- 边界确认节点
- 阈值设置节点
- 容忍度定义节点
- 责任划分节点

**文档**
- README.md：项目说明
- ARCHITECTURE.md：架构说明
- GUIDE.md：使用指南
- CONTRIBUTING.md：贡献指南

**示例**
- 示例对话：AI 客服助手设计流程
- 示例对话：AI 问答助手设计流程

### Design Philosophy

- 不替用户做决策，引导用户思考
- 在关键节点暂停，让用户选择
- 让用户在协作中学习 AI 产品设计
- 用户是导演，AI 是教练

---

## 版本规划

### [1.1.0] - Planned

- 多语言支持
- 对话历史保存
- 决策记录导出
- 更多示例对话

### [1.2.0] - Planned

- 团队协作模式
- 决策投票机制
- 版本对比功能
