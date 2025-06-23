## Text Processing: Becoming a Data Detective

Here's where the magic happens. Text processing is like being a detective with superpowers—you can sift through massive amounts of data, find patterns, extract clues, and solve mysteries that would take humans hours to uncover manually.

**The Reality Check:** In DevOps, you'll spend a surprising amount of time reading logs, analyzing configurations, and extracting data from text files. Master these skills, and you'll feel like Neo seeing the Matrix code.

### Reading Files: Your Investigation Tools

```bash
# The basic file readers
cat file.txt             # "Show me everything" (dumps entire file)
less file.txt            # "Let me browse" (page through file, q to quit)
head file.txt            # "Show me the beginning" (first 10 lines)
head -n 20 file.txt      # "Show me the first 20 lines"
tail file.txt            # "Show me the end" (last 10 lines)
tail -f logfile.log      # "Follow the action" (watch file changes in real-time)
```

**The `tail -f` Superpower:** This is the command that makes you look like a wizard. While others are refreshing log files manually, you're watching them update in real-time. It's like having a live feed of your system's thoughts.

**War Story:** I once debugged a production issue by running `tail -f` on the error log while a colleague reproduced the problem. As soon as they clicked the button, I saw the error appear in real-time and identified the issue in seconds. The look of amazement on their face was priceless.

### Searching and Filtering

```bash
# Search within files
grep "pattern" file.txt              # Find lines containing pattern
grep -i "pattern" file.txt           # Case-insensitive search
grep -r "pattern" directory/         # Recursive search in directory
grep -n "pattern" file.txt           # Show line numbers
grep -v "pattern" file.txt           # Show lines NOT containing pattern

# Advanced pattern matching
grep "^start" file.txt               # Lines starting with "start"
grep "end$" file.txt                 # Lines ending with "end"
grep -E "pattern1|pattern2" file.txt # Multiple patterns (extended regex)
```

### Text Processing with awk and sed

```bash
# awk - powerful text processing
awk '{print $1}' file.txt            # Print first column
awk '{print $1, $3}' file.txt        # Print first and third columns
awk '/pattern/ {print $2}' file.txt  # Print second column of matching lines
awk -F: '{print $1}' /etc/passwd     # Use colon as field separator

# sed - stream editor
sed 's/old/new/' file.txt            # Replace first occurrence per line
sed 's/old/new/g' file.txt           # Replace all occurrences
sed -i 's/old/new/g' file.txt        # Edit file in-place
sed -n '10,20p' file.txt             # Print lines 10-20
```

### Pipelines and Redirection

```bash
# Redirection
command > file.txt       # Redirect output to file (overwrite)
command >> file.txt      # Redirect output to file (append)
command 2> error.log     # Redirect errors to file
command &> all.log       # Redirect both output and errors

# Pipelines
cat file.txt | grep "pattern"                    # Basic pipe
ps aux | grep nginx | awk '{print $2}'          # Complex pipeline
cat access.log | grep "404" | wc -l             # Count 404 errors
```

---