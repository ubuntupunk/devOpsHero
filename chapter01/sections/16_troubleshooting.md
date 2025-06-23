## Troubleshooting Common Issues

### Permission Denied Errors

```bash
# Problem: Permission denied when running script
./script.sh
# bash: ./script.sh: Permission denied

# Solution: Add execute permission
chmod +x script.sh
./script.sh
```

### Command Not Found

```bash
# Problem: Command not found
docker --version
# bash: docker: command not found

# Solutions:
# 1. Check if installed
which docker

# 2. Check PATH
echo $PATH

# 3. Install if missing
sudo apt install docker.io  # Ubuntu
brew install docker         # macOS
```

### Disk Space Issues

```bash
# Check disk usage
df -h                    # Show disk space
du -sh *                 # Show directory sizes
du -sh * | sort -hr      # Sort by size

# Find large files
find / -type f -size +100M 2>/dev/null | head -10
```

### Process Issues

```bash
# Find processes using a port
sudo lsof -i :8080
sudo netstat -tulpn | grep :8080

# Kill processes using a port
sudo fuser -k 8080/tcp
```

---