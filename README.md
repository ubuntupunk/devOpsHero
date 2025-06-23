# DevOps Hero - Book Project

## Overview
This repository contains the complete manuscript and resources for "DevOps Hero", a technical book teaching command-line mastery, Git, and essential DevOps skills. The book is organized into 12 chapters with exercises, assets, and verification materials.

## Project Structure
```bash
.
├── chapter01/          # Command Line Mastery
├── chapter02/          # Git Mastery
├── ...                 # Chapters 3-12
├── fact-checking/      # Verification materials
├── shared/             # Cross-chapter resources
├── templates/          # Content templates
├── tools/              # Project utilities
├── PLANNING.md         # Project architecture documentation
├── TASK.md             # Task tracking system
└── README.md           # Project overview (this file)
```

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/devops-hero-book.git
   ```
2. Explore chapters:
   ```bash
   cd chapter01
   ls sections/
   ```

## Building Chapters
Each chapter contains an assembly script:
```bash
# Example: Build Chapter 1
cd chapter01
python assemble.py chapter01_complete.md
```

## Contributing
1. Check active tasks in `TASK.md`
2. Create new branch for your work
3. Add discovered tasks to "Discovered During Work" in `TASK.md`
4. Submit PR with completed tasks checked off

## Resources
- [Project Planning](PLANNING.md)
- [Task Tracking](TASK.md)
