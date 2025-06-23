# DevOps Hero: Project Structure

## Overview
This document outlines the organizational structure for "DevOps Hero: How to go from I suck to I rock in 12 chapters" to prevent file corruption and improve maintainability.

## Directory Structure

```
devOpsHero/
├── PROJECT_STRUCTURE.md           # This file
├── devopsHero.md                  # Main book outline
├── devopsHero_FactChecking_Strategy.md  # Fact-checking methodology
├── 
├── chapter01/                     # Chapter 1: Command Line Mastery
│   ├── sections/                  # Individual section files
│   │   ├── 01_introduction.md
│   │   ├── 02_navigation.md
│   │   ├── 03_file_operations.md
│   │   ├── 04_permissions.md
│   │   ├── 05_process_management.md
│   │   ├── 06_text_processing.md
│   │   ├── 07_package_management.md
│   │   ├── 08_text_editors.md
│   │   ├── 09_shell_environments.md
│   │   ├── 10_terminal_multiplexers.md
│   │   ├── 11_customization.md
│   │   └── 12_exercises.md
│   ├── assets/                    # Images, diagrams, etc.
│   ├── exercises/                 # Practical exercises
│   └── chapter01_complete.md      # Assembled chapter
│
├── chapter02/                     # Chapter 2: Git Fundamentals
│   ├── sections/
│   ├── assets/
│   ├── exercises/
│   └── chapter02_complete.md
│
├── chapter03/                     # Chapter 3: Git Crisis Recovery
│   ├── sections/
│   ├── assets/
│   ├── exercises/
│   └── chapter03_complete.md
│
├── [chapters 04-12 follow same pattern]
│
├── shared/                        # Shared content across chapters
│   ├── glossary.md
│   ├── common_commands.md
│   ├── troubleshooting.md
│   └── resources.md
│
├── templates/                     # Templates for consistency
│   ├── chapter_template.md
│   ├── section_template.md
│   └── exercise_template.md
│
├── tools/                         # Build and utility scripts
│   ├── assemble_chapter.py
│   ├── fact_check.py
│   ├── validate_links.py
│   └── generate_toc.py
│
└── fact-checking/                 # Fact-checking records
    ├── chapter01_verification.md
    ├── chapter02_verification.md
    └── [verification files for each chapter]
```

## Chapter Structure

Each chapter follows this pattern:

### sections/
Individual markdown files for each major section:
- **01_introduction.md** - Chapter intro and learning objectives
- **02-XX_[topic].md** - Main content sections
- **XX_exercises.md** - Practical exercises and examples

### assets/
- Images, diagrams, screenshots
- Code examples
- Configuration files
- Reference materials

### exercises/
- Hands-on labs
- Practice scenarios
- Solution files
- Assessment questions

### chapter_complete.md
- Assembled final chapter
- Generated from individual sections
- Ready for publication

## Benefits of This Structure

### 1. **Prevents File Corruption**
- Smaller files are less prone to corruption
- Individual sections can be edited safely
- Easy to restore individual pieces if needed

### 2. **Improves Collaboration**
- Multiple people can work on different sections
- Clear ownership and responsibility
- Easier to track changes

### 3. **Enhances Maintainability**
- Easy to update specific sections
- Modular content management
- Consistent structure across chapters

### 4. **Enables Automation**
- Scripts can assemble chapters automatically
- Automated fact-checking per section
- Link validation and consistency checks

### 5. **Better Version Control**
- Granular commit history
- Easier to see what changed
- Reduced merge conflicts

## Workflow

### 1. **Writing Process**
```bash
# Work on individual sections
vim chapter01/sections/02_navigation.md

# Test assembly
python tools/assemble_chapter.py chapter01

# Fact-check specific section
python tools/fact_check.py chapter01/sections/02_navigation.md
```

### 2. **Chapter Assembly**
```bash
# Assemble complete chapter from sections
python tools/assemble_chapter.py chapter01

# Generate table of contents
python tools/generate_toc.py chapter01

# Validate all links
python tools/validate_links.py chapter01
```

### 3. **Quality Assurance**
```bash
# Run fact-checking on entire chapter
python tools/fact_check.py chapter01

# Check for consistency
python tools/check_consistency.py

# Generate verification report
python tools/generate_verification.py chapter01
```

## File Naming Conventions

### Sections
- Use two-digit prefixes: `01_`, `02_`, etc.
- Use underscores for spaces: `file_operations.md`
- Be descriptive but concise: `package_management.md`

### Assets
- Include chapter reference: `ch01_terminal_screenshot.png`
- Use descriptive names: `vim_keybindings_diagram.svg`
- Group by type: `images/`, `code/`, `configs/`

### Exercises
- Number sequentially: `exercise_01_navigation.md`
- Include difficulty: `advanced_log_analysis.md`
- Provide solutions: `exercise_01_solution.md`

## Templates

### Section Template
```markdown
# Section Title

## Learning Objectives
- Objective 1
- Objective 2

## Content
[Main content here]

## Key Takeaways
- Takeaway 1
- Takeaway 2

## Next Steps
[Link to next section]
```

### Exercise Template
```markdown
# Exercise: [Title]

## Difficulty: [Beginner/Intermediate/Advanced]

## Objectives
- What you'll learn

## Prerequisites
- Required knowledge/setup

## Instructions
[Step-by-step instructions]

## Expected Output
[What success looks like]

## Troubleshooting
[Common issues and solutions]

## Further Reading
[Additional resources]
```

## Migration Plan

### Phase 1: Setup Structure ✅
- Create directory structure
- Move existing files
- Create templates

### Phase 2: Break Down Chapter 1
- Split into individual sections
- Create fact-checking records
- Test assembly process

### Phase 3: Create Tools
- Chapter assembly script
- Fact-checking automation
- Link validation

### Phase 4: Apply to All Chapters
- Replicate structure for chapters 2-12
- Migrate existing content
- Establish workflow

## Best Practices

### 1. **One Concept Per Section**
- Keep sections focused
- Aim for 500-1500 words per section
- Clear learning objectives

### 2. **Consistent Formatting**
- Use templates
- Follow naming conventions
- Maintain style guide

### 3. **Regular Assembly**
- Test chapter assembly frequently
- Validate links and references
- Check for consistency

### 4. **Version Control**
- Commit individual sections
- Meaningful commit messages
- Tag chapter releases

### 5. **Fact-Checking**
- Verify each section independently
- Maintain verification records
- Regular update cycles

This structure will make our DevOps Hero project much more manageable and professional!