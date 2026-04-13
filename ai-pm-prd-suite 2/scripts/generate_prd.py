#!/usr/bin/env python3
"""
PRD Generator - 生成生产级 PRD 文档

Usage:
    python3 generate_prd.py --idea "产品构想" --output prd.md
"""

import argparse
import json
import sys
from datetime import datetime


def generate_prd(idea: str, target_users: list = None, constraints: list = None) -> str:
    """
    生成 PRD 文档的骨架结构
    
    注意：此脚本生成的是 PRD 结构框架，
    实际内容需要由 AI 基于产品构想填充。
    """
    
    prd_template = f'''# 需求文档

## 1. 应用概述

### 应用名称
[待填充]

### 应用描述
{idea}

---

## 2. 用户与使用场景

### 目标用户
{chr(10).join([f"- **{u}**：[用户画像描述]" for u in (target_users or ["主要用户"])]))}

### 核心使用场景
1. **场景一**：[场景描述]
   - 触发条件：[什么情况下使用]
   - 用户目标：[用户想达成什么]
   - 预期结果：[产品如何满足]

---

## 3. 页面结构与功能说明

### 3.1 整体页面结构

```
页面名称
├── 顶部导航区 (Header)
│   ├── Logo
│   ├── 导航菜单
│   └── 用户操作区
├── 主内容区 (Main)
│   ├── 区块 A
│   └── 区块 B
└── 底部信息区 (Footer)
```

### 3.2 全局视觉与交互规范

#### 色彩体系
- 主色：`#1890ff`（品牌蓝）
- 辅助色：`#52c41a`（成功绿）、`#faad14`（警告黄）、`#ff4d4f`（错误红）

#### 动画规范
- 默认缓动：`cubic-bezier(0.4, 0, 0.2, 1)`
- 标准动画：`300ms`
- 降级方案：`prefers-reduced-motion: reduce` → `0.01ms`

#### 响应式断点
```css
@media (max-width: 900px) {{ /* 平板 */ }}
@media (max-width: 700px) {{ /* 手机 */ }}
```

---

## 4. 业务规则与逻辑

### 规则 1：[规则名称]
- **触发条件**：[什么情况下触发]
- **处理逻辑**：[具体的处理步骤]
- **输出结果**：[处理后的结果]

---

## 5. 异常与边界情况

| 场景 | 异常类型 | 处理方式 | 用户提示 |
|------|----------|----------|----------|
| 数据缺失 | 空状态 | 显示占位图 | "暂无数据" |
| 边界溢出 | 浮层超出屏幕 | 自动翻转方向 | - |
| 网络错误 | 请求失败 | 显示错误状态 | "网络异常，请重试" |

---

## 6. 验收标准

### 功能验收
- [ ] 用户可以通过 [操作] 完成 [目标]
- [ ] 系统在 [场景] 下正确显示 [结果]

### 性能验收
- [ ] 页面首屏加载时间 < 2s
- [ ] 交互响应时间 < 100ms

### 兼容性验收
- [ ] Chrome/Safari/Firefox 最新版正常
- [ ] 移动端正常显示

---

## 7. 本期不实现功能

| 功能 | 原因 | 计划排期 |
|------|------|----------|
| [功能名称] | [不实现的原因] | [后续排期] |

---

<!--
生成时间：{datetime.now().isoformat()}
产品构想：{idea}
约束条件：{json.dumps(constraints or [], ensure_ascii=False)}
-->
'''
    return prd_template


def main():
    parser = argparse.ArgumentParser(description='PRD Generator')
    parser.add_argument('--idea', required=True, help='产品构想')
    parser.add_argument('--users', nargs='+', default=[], help='目标用户列表')
    parser.add_argument('--constraints', nargs='+', default=[], help='约束条件')
    parser.add_argument('--output', default=None, help='输出文件路径')
    parser.add_argument('--json', action='store_true', help='JSON 格式输出')
    
    args = parser.parse_args()
    
    prd = generate_prd(args.idea, args.users, args.constraints)
    
    if args.json:
        result = {
            "status": "success",
            "prd": prd,
            "metadata": {
                "idea": args.idea,
                "users": args.users,
                "constraints": args.constraints,
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
