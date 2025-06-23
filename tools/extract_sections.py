#!/usr/bin/env python3
"""
Extract sections from Chapter 1 based on ## headings
"""

import re
import os

def extract_sections():
    """Extract sections from Chapter 1"""
    
    # Read the file
    with open('Chapter1_CommandLineMastery.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Define sections with their start patterns and filenames
    sections = [
        ('# Chapter 1:', '01_introduction.md'),
        ('## The Terminal Anxiety is Real', '02_terminal_anxiety.md'),
        ('## The Transformation: From Clicking', '03_transformation.md'),
        ('## Why Command Line Mastery is Your DevOps Superpower', '04_why_cli_mastery.md'),
        ('## Your First Steps: Navigation', '05_navigation.md'),
        ('## File Permissions: The Bouncer System', '06_permissions.md'),
        ('## Process Management: Becoming the System Whisperer', '07_process_management.md'),
        ('## Text Processing: Becoming a Data Detective', '08_text_processing.md'),
        ('## Environment Variables and PATH Management', '09_environment.md'),
        ('## Package Management: The Great Liberation', '10_package_management.md'),
        ('## Text Editors: The Holy War That Defines You', '11_text_editors.md'),
        ('## Shell Environments: The Zsh Cult', '12_shell_environments.md'),
        ('## Terminal Multiplexers', '13_terminal_multiplexers.md'),
        ('## Practical Exercise: Log Analysis Pipeline', '14_practical_exercise.md'),
        ('## Setting Up a Productive Terminal Environment', '15_customization.md'),
        ('## Troubleshooting Common Issues', '16_troubleshooting.md'),
        ('## Your Transformation is Complete', '17_chapter_summary.md'),
        ('## The Hero\'s Moment', '18_conclusion.md'),
    ]
    
    # Create sections directory
    os.makedirs('chapter01/sections', exist_ok=True)
    
    # Extract each section
    for i, (start_pattern, filename) in enumerate(sections):
        # Find start of this section
        start_match = re.search(re.escape(start_pattern), content)
        if not start_match:
            print(f"Warning: Could not find start pattern: {start_pattern}")
            continue
        
        start_pos = start_match.start()
        
        # Find start of next section (or end of file)
        if i + 1 < len(sections):
            next_pattern = sections[i + 1][0]
            end_match = re.search(re.escape(next_pattern), content)
            end_pos = end_match.start() if end_match else len(content)
        else:
            end_pos = len(content)
        
        # Extract section content
        section_content = content[start_pos:end_pos].strip()
        
        # Write to file
        filepath = f'chapter01/sections/{filename}'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(section_content)
        
        print(f"Created: {filepath} ({len(section_content)} characters)")

def create_assembly_script():
    """Create a script to reassemble the chapter"""
    
    script_content = '''#!/usr/bin/env python3
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
        f.write('\\n'.join(assembled_content))
    
    print("Chapter assembled: chapter01_complete.md")

if __name__ == "__main__":
    assemble_chapter()
'''
    
    with open('chapter01/assemble.py', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print("Created: chapter01/assemble.py")

def main():
    """Main function"""
    print("Extracting Chapter 1 sections...")
    extract_sections()
    create_assembly_script()
    print("\\nExtraction complete!")
    print("\\nTo reassemble the chapter:")
    print("cd chapter01 && python assemble.py")

if __name__ == "__main__":
    main()