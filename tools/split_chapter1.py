#!/usr/bin/env python3
"""
Script to split Chapter 1 into individual section files
"""

import os
import re

def read_chapter():
    """Read the complete Chapter 1 file"""
    with open('Chapter1_CommandLineMastery.md', 'r', encoding='utf-8') as f:
        return f.read()

def split_into_sections(content):
    """Split content into logical sections"""
    
    sections = {}
    
    # Define section boundaries based on major headings
    section_patterns = [
        (r'# Chapter 1.*?(?=## The Terminal Anxiety)', '01_introduction.md'),
        (r'## The Terminal Anxiety.*?(?=## The Transformation)', '02_terminal_anxiety.md'),
        (r'## The Transformation.*?(?=## Why Command Line Mastery)', '03_transformation.md'),
        (r'## Why Command Line Mastery.*?(?=## Your First Steps)', '04_why_cli_mastery.md'),
        (r'## Your First Steps.*?(?=## File Permissions)', '05_navigation.md'),
        (r'## File Permissions.*?(?=## Process Management)', '06_permissions.md'),
        (r'## Process Management.*?(?=## Text Processing)', '07_process_management.md'),
        (r'## Text Processing.*?(?=## Environment Variables)', '08_text_processing.md'),
        (r'## Environment Variables.*?(?=## Package Management)', '09_environment.md'),
        (r'## Package Management.*?(?=## Text Editors)', '10_package_management.md'),
        (r'## Text Editors.*?(?=## Shell Environments)', '11_text_editors.md'),
        (r'## Shell Environments.*?(?=## Terminal Multiplexers)', '12_shell_environments.md'),
        (r'## Terminal Multiplexers.*?(?=## Setting Up)', '13_terminal_multiplexers.md'),
        (r'## Setting Up.*?(?=## Practical Exercise)', '14_customization.md'),
        (r'## Practical Exercise.*?(?=## Troubleshooting)', '15_practical_exercise.md'),
        (r'## Troubleshooting.*?(?=## Your Transformation)', '16_troubleshooting.md'),
        (r'## Your Transformation.*?(?=## The Hero)', '17_chapter_summary.md'),
        (r'## The Hero.*', '18_conclusion.md'),
    ]
    
    for pattern, filename in section_patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            sections[filename] = match.group(0).strip()
    
    return sections

def write_sections(sections):
    """Write sections to individual files"""
    
    # Ensure sections directory exists
    os.makedirs('chapter01/sections', exist_ok=True)
    
    for filename, content in sections.items():
        filepath = f'chapter01/sections/{filename}'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created: {filepath}")

def create_section_index():
    """Create an index of all sections"""
    
    index_content = """# Chapter 1: Command Line Mastery - Section Index

## Sections

1. [Introduction](sections/01_introduction.md) - Chapter overview and motivation
2. [Terminal Anxiety](sections/02_terminal_anxiety.md) - Overcoming command line fear
3. [Transformation](sections/03_transformation.md) - Learning objectives and journey
4. [Why CLI Mastery](sections/04_why_cli_mastery.md) - DevOps superpower explanation
5. [Navigation](sections/05_navigation.md) - File system navigation and basics
6. [Permissions](sections/06_permissions.md) - File permissions and ownership
7. [Process Management](sections/07_process_management.md) - Managing system processes
8. [Text Processing](sections/08_text_processing.md) - Log analysis and text manipulation
9. [Environment](sections/09_environment.md) - Environment variables and PATH
10. [Package Management](sections/10_package_management.md) - Software installation
11. [Text Editors](sections/11_text_editors.md) - Vim, Emacs, and the holy war
12. [Shell Environments](sections/12_shell_environments.md) - Zsh and shell customization
13. [Terminal Multiplexers](sections/13_terminal_multiplexers.md) - tmux and screen
14. [Customization](sections/14_customization.md) - Setting up productive environment
15. [Practical Exercise](sections/15_practical_exercise.md) - Log analysis pipeline
16. [Troubleshooting](sections/16_troubleshooting.md) - Common issues and solutions
17. [Chapter Summary](sections/17_chapter_summary.md) - Transformation complete
18. [Conclusion](sections/18_conclusion.md) - Hero's moment and next steps

## Assembly

To assemble the complete chapter:
```bash
python ../tools/assemble_chapter.py chapter01
```

## Editing Workflow

1. Edit individual section files in `sections/`
2. Test changes by assembling the chapter
3. Commit individual sections for better version control
4. Run fact-checking on modified sections
"""
    
    with open('chapter01/README.md', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Created: chapter01/README.md")

def main():
    """Main function"""
    print("Splitting Chapter 1 into sections...")
    
    # Read the complete chapter
    content = read_chapter()
    
    # Split into sections
    sections = split_into_sections(content)
    
    # Write individual section files
    write_sections(sections)
    
    # Create section index
    create_section_index()
    
    print(f"\nSplit complete! Created {len(sections)} section files.")
    print("Files are in: chapter01/sections/")

if __name__ == "__main__":
    main()