"""
QClaw Dev Workflow - 文档初始化脚本
在项目根目录运行此脚本创建 doc 文件夹结构
"""

import os
import sys
from datetime import datetime

def init_project_docs(project_name, project_path="."):
    """初始化项目文档结构"""
    
    doc_path = os.path.join(project_path, "doc")
    
    # 创建 doc 目录
    if not os.path.exists(doc_path):
        os.makedirs(doc_path)
        print(f"✅ 创建目录: {doc_path}")
    
    # 文档清单
    docs = [
        ("01-requirements.md", "需求文档"),
        ("02-design.md", "设计文档"),
        ("03-tasks.md", "任务计划"),
        ("04-dev-log.md", "开发记录"),
        ("05-test-cases.md", "测试用例"),
        ("06-code-review.md", "代码评审"),
        ("07-usage-stats.md", "使用统计"),
    ]
    
    created = []
    for filename, desc in docs:
        filepath = os.path.join(doc_path, filename)
        if not os.path.exists(filepath):
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {desc}\n\n")
                f.write(f"## 项目: {project_name}\n\n")
                f.write(f"*初始化时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
            created.append(filename)
            print(f"✅ 创建文件: {filename}")
    
    return created

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python init_docs.py <项目名称> [项目路径]")
        sys.exit(1)
    
    project_name = sys.argv[1]
    project_path = sys.argv[2] if len(sys.argv) > 2 else "."
    
    created = init_project_docs(project_name, project_path)
    print(f"\n📁 共创建 {len(created)} 个文档文件")
