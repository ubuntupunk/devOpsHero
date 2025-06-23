#!/usr/bin/env python3
"""
Assemble Chapter 2 from individual sections
"""

import os

def assemble_chapter():
    """Assemble chapter from sections"""
    
    section_files = [
        '01_introduction.md',
        '02_git_anxiety.md', 
        '03_git_philosophy.md',
        '04_basic_workflow.md',
        '05_branching_strategy.md',
        '06_collaboration.md',
        # Add more sections as we create them
    ]
    
    assembled_content = []
    
    for filename in section_files:
        filepath = f'sections/{filename}'
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                assembled_content.append(content)
                assembled_content.append('')  # Add blank line between sections
        else:
            print(f"Warning: {filepath} not found")
    
    # Write assembled chapter
    with open('chapter02_complete.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(assembled_content))
    
    print("Chapter 2 assembled: chapter02_complete.md")
    print(f"Sections included: {len([f for f in section_files if os.path.exists(f'sections/{f}')])}")

if __name__ == "__main__":
    assemble_chapter()