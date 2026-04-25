# Task 1: Simple File Operations - Bash Version

## Overview
Linux/bash equivalent of the Windows CMD task. Creates directory structure and files using standard bash commands.

## Quick Start

```bash
chmod +x task1_bash.sh
./task1_bash.sh
```

## What It Does

Creates `~/tmp_SO/` directory with three files:

### readme.txt
- Directory listing (using `ls -lah`)
- Shows all files and permissions in tmp_SO

### author.txt
- Author name and surname
- Assignment information
- Directory listing with detailed file info

### history.txt
- Bash command history
- All commands executed in the session

## Key Differences from Windows Version

| Windows CMD | Bash Equivalent |
|------------|-----------------|
| `mkdir C:\tmp_SO` | `mkdir ~/tmp_SO` |
| `dir` | `ls -lah` |
| `doskey /history` | `history` |
| `type filename.txt` | `cat filename.txt` |
| `cd` | `cd` |
| `echo` | `echo` |

## Expected Output Structure

```
~/tmp_SO/
├── readme.txt       (directory listing)
├── author.txt       (author info + listing)
└── history.txt      (command history)
```

## Running the Script

### Method 1: Direct execution
```bash
./task1_bash.sh
```

### Method 2: With bash explicitly
```bash
bash task1_bash.sh
```

### Method 3: Manual execution
```bash
# Create directory
mkdir -p ~/tmp_SO
cd ~/tmp_SO

# Create readme.txt
ls -lah > readme.txt

# Create author.txt
{
    echo "Author Information"
    echo "Name and Surname: Megan Poparda"
    echo "Date: $(date)"
    echo ""
    ls -lah
} > author.txt

# Create history.txt
history > history.txt

# Display results
ls -lah
cat readme.txt
cat author.txt
cat history.txt
```

## Verification

Check files were created:
```bash
ls -lah ~/tmp_SO
```

Display file contents:
```bash
cat ~/tmp_SO/readme.txt
cat ~/tmp_SO/author.txt
cat ~/tmp_SO/history.txt
```

## Notes
- Script creates files in user's home directory (`~/tmp_SO`)
- Uses relative paths compatible with Linux/Mac
- File contents use standard Unix commands
- Timestamps use ISO 8601 format (YYYY-MM-DD)
- Permissions displayed with `-lah` flag for full details
