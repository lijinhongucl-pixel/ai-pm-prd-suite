#!/usr/bin/env python3
"""
Pain to PRD Converter - 将痛点分析转换为完整 PRD

与 auto-prd-hunter 联动，将痛点数据转化为生产级 PRD 文档。

Usage:
    python3 pain_to_prd.py --input pain_points.json --output prd.md
    python3 pain_to_prd.py --pain-points '[{"id": "PP-001", "title": "..."}]'
"""

import argparse
import json
import sys
from datetime import datetime
from typing import List, Dict


def pain_to_prd(pain_points: List[Dict], user_stories: List[Dict] = None, 
                mvp_features: List[Dict] = None) -> str:
    """
    将痛点数据转换为 PRD 文档
    
    Args:
        pain_points: 痛点列表
        user_stories: 用户故事列表（可选）
        mvp_features: MVP 功能列表（可选）
    """
    
    # 提取产品名称（基于第一个痛点）
    product_name = "待命名产品"
    if pain_points:
        first_pain = pain_points[0]
        title = first_pain.get('title', '')
        # 尝试从标题推断产品方向
        if 'AI' in title or '智能' in title:
            product_name = "AI 助手产品"
    
    # 构建痛点描述
    pain_points_md = "\n".join([
        f"- **{p.get('id', 'PP-???')}**：{p.get('title', '未命名痛点')}（严重程度：{p.get('severity', 'unknown')}）"
        for p in pain_points
    ])
    
    # 构建用户故事
    if user_stories:
        user_stories_md = "\n".join([
            f"- 作为 **{s.get('as_a', '用户')}**，我希望 **{s.get('i_want_to', '...')}**，以便 **{s.get('so_that', '...')}**"
            for s in user_stories
        ])
    else:
        user_stories_md = "- [待填充用户故事]"
    
    # 构建 MVP 功能
    if mvp_features:
        mvp_features_md = "\n".join([
            f"- **{f.get('id', 'F-???')}**：{f.get('title', '未命名功能')} - {f.get('description', '')}"
            for f in mvp_features
        ])
    else:
        mvp_features_md = "- [待填充 MVP 功能]"
    
    prd = f'''# 需求文档

## 1. 应用概述

### 应用名称
{product_name}

### 应用描述
基于用户痛点分析，打造解决核心问题的产品。

**核心痛点来源：**
{pain_points_md}

---

## 2. 用户与使用场景

### 目标用户
- **主要用户**：[基于痛点分析的目标用户]

### 核心使用场景

**用户故事：**
{user_stories_md}

---

## 3. 页面结构与功能说明

### 3.1 整体页面结构

```
{product_name}
├── 首页
│   ├── 核心功能区
│   └── 导航区
├── 功能页面
│   └── [基于 MVP 功能拆解]
└── 用户中心
    ├── 个人设置
    └── 历史记录
```

### 3.2 全局视觉与交互规范

#### 色彩体系
- 主色：`#1890ff`（品牌蓝）
- 辅助色：`#52c41a`（成功绿）、`#faad14`（警告黄）、`#ff4d4f`（错误红）

#### 动画规范
- 默认缓动：`cubic-bezier(0.4, 0, 0.2, 1)`
- 标准动画：`300ms`
- 降级方案：`prefers-reduced-motion: reduce` → `0.01ms`

---

## 4. 业务规则与逻辑

### MVP 功能列表
{mvp_features_md}

### 痛点 → 功能映射

| 痛点 ID | 痛点描述 | 对应功能 | 优先级 |
|---------|----------|----------|--------|
{chr(10).join([f"| {p.get('id', 'PP-???')} | {p.get('title', '')[:20]} | [待映射] | {p.get('severity', 'medium')} |" for p in pain_points])}

---

## 5. 异常与边界情况

| 场景 | 异常类型 | 处理方式 | 用户提示 |
|------|----------|----------|----------|
| 数据缺失 | 空状态 | 显示占位图 | "暂无数据" |
| 网络错误 | 请求失败 | 显示错误状态 | "网络异常，请重试" |
| 权限不足 | 未授权 | 引导登录 | "请先登录" |

---

## 6. 验收标准

### 功能验收
- [ ] 核心痛点对应的解决方案可用
- [ ] 用户故事中的主要路径可走通
- [ ] MVP 功能全部实现

### 性能验收
- [ ] 页面首屏加载时间 < 2s
- [ ] 交互响应时间 < 100ms

---

## 7. 本期不实现功能

| 功能 | 原因 | 计划排期 |
|------|------|----------|
| [基于痛点优先级判断] | 非核心功能 | 后续版本 |

---

<!--
生成时间：{datetime.now().isoformat()}
痛点来源：auto-prd-hunter
痛点数量：{len(pain_points)}
用户故事数量：{len(user_stories) if user_stories else 0}
MVP 功能数量：{len(mvp_features) if mvp_features else 0}
-->
'''
    
    return prd


def main():
    parser = argparse.ArgumentParser(description='Pain to PRD Converter')
    parser.add_argument('--input', help='痛点 JSON 文件路径')
    parser.add_argument('--pain-points', help='痛点 JSON 字符串')
    parser.add_argument('--output', default=None, help='输出 PRD 文件路径')
    parser.add_argument('--json', action='store_true', help='JSON 格式输出')
    
    args = parser.parse_args()
    
    # 解析输入
    if args.input:
        with open(args.input, 'r', encoding='utf-8') as f:
            data = json.load(f)
        pain_points = data.get('pain_points', [])
        user_stories = data.get('user_stories', [])
        mvp_features = data.get('mvp_features', [])
    elif args.pain_points:
        pain_points = json.loads(args.pain_points)
        user_stories = []
        mvp_features = []
    else:
        print("错误：请提供 --input 或 --pain-points 参数")
        sys.exit(1)
    
    prd = pain_to_prd(pain_points, user_stories, mvp_features)
    
    if args.json:
        result = {
            "status": "success",
            "prd": prd,
            "metadata": {
                "pain_points_count": len(pain_points),
                "user_stories_count": len(user_stories) if user_stories else 0,
                "mvp_features_count": len(mvp_features) if mvp_features else 0,
                "generated_at": datetime.now().isoformat()
            }
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(prd)
            print(f"PRD 已保存至：{args.output}")
        else:
            print(prd)


if __name__ == "__main__":
    main()
