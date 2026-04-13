#!/usr/bin/env python3
"""
PRD Validator - 验证 PRD 是否符合开发友好标准

Usage:
    python3 validate_prd.py --file prd.md
    python3 validate_prd.py --content "..." --json
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Issue:
    module: str
    severity: str  # critical, high, medium, low
    issue: str
    suggestion: str


def validate_prd(content: str) -> Tuple[int, List[Issue]]:
    """
    验证 PRD 文档
    
    Returns:
        (score, issues) - 评分和问题列表
    """
    issues = []
    score = 100
    
    # 1. 检查 7 个必需模块
    required_modules = [
        ("1. 应用概述", r"##\s*1\.\s*应用概述"),
        ("2. 用户与使用场景", r"##\s*2\.\s*用户与使用场景"),
        ("3. 页面结构与功能说明", r"##\s*3\.\s*页面结构与功能说明"),
        ("4. 业务规则与逻辑", r"##\s*4\.\s*业务规则与逻辑"),
        ("5. 异常与边界情况", r"##\s*5\.\s*异常与边界情况"),
        ("6. 验收标准", r"##\s*6\.\s*验收标准"),
        ("7. 本期不实现功能", r"##\s*7\.\s*本期不实现功能"),
    ]
    
    for module_name, pattern in required_modules:
        if not re.search(pattern, content, re.IGNORECASE):
            issues.append(Issue(
                module="完整性",
                severity="critical",
                issue=f"缺少必需模块：{module_name}",
                suggestion=f"添加 {module_name} 模块"
            ))
            score -= 15
    
    # 2. 检查树状页面结构
    if not re.search(r'```\n.*├──', content, re.DOTALL):
        issues.append(Issue(
            module="3.1",
            severity="high",
            issue="缺少树状页面结构图",
            suggestion="使用树状结构（├──, └──）表达页面层级"
        ))
        score -= 10
    
    # 3. 检查 CSS 类名预设
    if not re.search(r'\.[a-z-]+\s*\{', content):
        issues.append(Issue(
            module="3.x",
            severity="medium",
            issue="缺少 CSS 类名预设",
            suggestion="为关键元素预设 CSS 类名（如 .card, .button-primary）"
        ))
        score -= 5
    
    # 4. 检查动画参数
    has_animation = re.search(r'(animation|transition|transform)', content, re.IGNORECASE)
    has_prefers_reduced_motion = re.search(r'prefers-reduced-motion', content, re.IGNORECASE)
    
    if has_animation and not has_prefers_reduced_motion:
        issues.append(Issue(
            module="3.2",
            severity="medium",
            issue="动画定义缺少 prefers-reduced-motion 降级方案",
            suggestion="添加 @media (prefers-reduced-motion: reduce) 样式"
        ))
        score -= 5
    
    # 5. 检查响应式断点
    if not re.search(r'@media.*max-width', content):
        issues.append(Issue(
            module="3.2",
            severity="medium",
            issue="缺少响应式断点定义",
            suggestion="添加媒体查询断点（如 @media (max-width: 900px)）"
        ))
        score -= 5
    
    # 6. 检查异常情况表格
    if not re.search(r'\|.*\|.*\|.*\|', content):
        issues.append(Issue(
            module="5",
            severity="high",
            issue="异常与边界情况未使用表格格式",
            suggestion="使用 Markdown 表格列出异常场景"
        ))
        score -= 10
    
    # 7. 检查验收标准列表
    if not re.search(r'-\s*\[.\]', content):
        issues.append(Issue(
            module="6",
            severity="medium",
            issue="验收标准未使用列表格式",
            suggestion="使用 - [ ] 格式列出验收项"
        ))
        score -= 5
    
    # 确保分数在 0-100 范围内
    score = max(0, min(100, score))
    
    return score, issues


def get_grade(score: int) -> str:
    """根据分数返回等级"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    parser = argparse.ArgumentParser(description='PRD Validator')
    parser.add_argument('--file', help='PRD 文件路径')
    parser.add_argument('--content', help='PRD 内容（直接传入）')
    parser.add_argument('--json', action='store_true', help='JSON 格式输出')
    
    args = parser.parse_args()
    
    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
    elif args.content:
        content = args.content
    else:
        print("错误：请提供 --file 或 --content 参数")
        sys.exit(1)
    
    score, issues = validate_prd(content)
    grade = get_grade(score)
    
    if args.json:
        result = {
            "status": "success",
            "score": score,
            "grade": grade,
            "passed": score >= 80,
            "issues": [
                {
                    "module": i.module,
                    "severity": i.severity,
                    "issue": i.issue,
                    "suggestion": i.suggestion
                }
                for i in issues
            ]
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"PRD 验证结果")
        print(f"=" * 50)
        print(f"评分：{score}/100")
        print(f"等级：{grade}")
        print(f"状态：{'✅ 通过' if score >= 80 else '❌ 未通过'}")
        print()
        
        if issues:
            print(f"发现问题 ({len(issues)} 个)：")
            print("-" * 50)
            for i in issues:
                print(f"[{i.severity.upper()}] {i.module}: {i.issue}")
                print(f"    建议：{i.suggestion}")
                print()


if __name__ == "__main__":
    main()
