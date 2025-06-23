## Environment Variables and PATH Management

Understanding environment variables is crucial for configuring tools and managing system behavior.

### Working with Environment Variables

```bash
# View environment variables
env                      # Show all environment variables
echo $PATH              # Show PATH variable
echo $HOME              # Show home directory
echo $USER              # Show current user

# Set environment variables
export VAR_NAME="value"                    # Set for current session
export PATH="$PATH:/new/directory"         # Add to PATH

# Make permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export VAR_NAME="value"' >> ~/.bashrc
source ~/.bashrc                           # Reload configuration
```

### PATH Management Best Practices

```bash
# Check if command exists
which docker            # Show path to docker command
command -v docker       # Alternative way to check

# Add local bin directory to PATH
export PATH="$HOME/.local/bin:$PATH"

# Add current directory to PATH (use with caution)
export PATH=".:$PATH"
```

---