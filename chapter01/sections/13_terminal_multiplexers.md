## Terminal Multiplexers

Terminal multiplexers allow you to run multiple terminal sessions within a single window and keep sessions running even when disconnected.

### tmux (Terminal Multiplexer)

```bash
# Start new session
tmux                     # Start with default name
tmux new -s session_name # Start with custom name

# Basic tmux commands (prefix key: Ctrl+b)
Ctrl+b c                 # Create new window
Ctrl+b n                 # Next window
Ctrl+b p                 # Previous window
Ctrl+b %                 # Split vertically
Ctrl+b "                 # Split horizontally
Ctrl+b arrow_keys        # Navigate between panes

# Session management
tmux ls                  # List sessions
tmux attach -t session_name  # Attach to session
Ctrl+b d                 # Detach from session
```

### screen (Alternative)

```bash
# Start screen session
screen -S session_name

# Basic screen commands (prefix key: Ctrl+a)
Ctrl+a c                 # Create new window
Ctrl+a n                 # Next window
Ctrl+a p                 # Previous window
Ctrl+a d                 # Detach session

# Reattach to session
screen -r session_name
```

---