#!/usr/bin/env python3
"""
Assemble Chapter 1 from individual sections
"""

import os

def assemble_chapter():
    """Assemble chapter from sections"""
    
    section_files = [
        '01_introduction.md',
        '02_terminal_anxiety.md', 
        '03_transformation.md',
        '04_why_cli_mastery.md',
        '05_navigation.md',
        '06_permissions.md',
        '07_process_management.md',
        '08_text_processing.md',
        '09_environment.md',
        '10_package_management.md',
        '11_text_editors.md',
        '12_shell_environments.md',
        '13_terminal_multiplexers.md',
        '14_practical_exercise.md',
        '15_customization.md',
        '16_troubleshooting.md',
        '17_chapter_summary.md',
        '18_conclusion.md',
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
    with open('chapter01_complete.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(assembled_content))
    
    print("Chapter assembled: chapter01_complete.md")

if __name__ == "__main__":
    assemble_chapter()
