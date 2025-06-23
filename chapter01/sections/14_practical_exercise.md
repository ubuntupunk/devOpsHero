## Practical Exercise: Log Analysis Pipeline

Let's put together what we've learned with a real-world scenario: analyzing web server logs.

### Scenario Setup

```bash
# Create a sample log file (in real scenarios, this would be your actual log)
cat > access.log << 'EOF'
192.168.1.100 - - [15/Dec/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.101 - - [15/Dec/2024:10:31:12 +0000] "GET /about.html HTTP/1.1" 200 2345
192.168.1.102 - - [15/Dec/2024:10:31:45 +0000] "GET /missing.html HTTP/1.1" 404 567
192.168.1.100 - - [15/Dec/2024:10:32:15 +0000] "POST /login HTTP/1.1" 200 890
192.168.1.103 - - [15/Dec/2024:10:32:45 +0000] "GET /admin HTTP/1.1" 403 234
192.168.1.101 - - [15/Dec/2024:10:33:12 +0000] "GET /api/data HTTP/1.1" 500 345
EOF
```

### Analysis Tasks

```bash
# 1. Count total requests
wc -l access.log

# 2. Find all 404 errors
grep " 404 " access.log

# 3. Count 404 errors
grep " 404 " access.log | wc -l

# 4. List unique IP addresses
awk '{print $1}' access.log | sort | uniq

# 5. Count requests per IP
awk '{print $1}' access.log | sort | uniq -c | sort -nr

# 6. Find all errors (4xx and 5xx status codes)
grep -E " [45][0-9][0-9] " access.log

# 7. Extract just the requested URLs
awk '{print $7}' access.log

# 8. Find the most requested pages
awk '{print $7}' access.log | sort | uniq -c | sort -nr

# 9. Show requests in the last minute (assuming current time)
grep "10:33" access.log

# 10. Create a summary report
echo "=== Log Analysis Report ===" > report.txt
echo "Total requests: $(wc -l < access.log)" >> report.txt
echo "404 errors: $(grep -c " 404 " access.log)" >> report.txt
echo "Unique IPs: $(awk '{print $1}' access.log | sort | uniq | wc -l)" >> report.txt
cat report.txt
```

---