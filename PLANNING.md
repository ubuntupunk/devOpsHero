# Project Planning: DevOps Hero Book

## Project Overview
This project contains the manuscript for "DevOps Hero", a technical book covering command-line mastery, Git, and other DevOps topics. The book is organized into chapters with exercises and assets.

## Architecture
```
.
├── chapter01/              # Chapter 1: Command Line Mastery
│   ├── sections/           # Individual section files
│   ├── exercises/          # Chapter exercises
│   ├── assets/             # Images/diagrams
│   ├── assemble.py         # Chapter assembly script
│   └── README.md           # Chapter-specific notes
├── chapter02/              # Chapter 2: Git Mastery
│   └── [same structure]    
├── ...                     # Chapters 3-12
├── fact-checking/          # Verification materials
├── shared/                 # Cross-chapter resources
├── templates/              # Content templates
└── tools/                  # Project utilities
```

## Style Guide
- All content in Markdown (.md) format
- Consistent section numbering (01_introduction, 02_topic, etc.)
- Python scripts for content assembly
- Exercises in dedicated per-chapter directories
