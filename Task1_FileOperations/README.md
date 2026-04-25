# Task 1: Simple File Operations (25%)

## Task Description
Create a directory structure using CMD commands and capture file listings and command history.

## Files Provided

### Batch Scripts
- **task1_simple.bat** - Ready-to-run batch script (easiest option)
- **execute_task1.bat** - Alternative batch script with template

### Templates
- **tmp_SO/readme.txt** - Template for readme file
- **tmp_SO/author.txt** - Template for author info file
- **INSTRUCTIONS.md** - Detailed step-by-step instructions

## Quick Start

### On Windows CMD:
```cmd
cd Task1_FileOperations
task1_simple.bat
```

The script will automatically:
1. Create `C:\tmp_SO` directory
2. Generate `readme.txt` with directory listing
3. Generate `author.txt` with author name and listing
4. Generate `history.txt` with command history
5. Display all results

## What Gets Created

```
C:\tmp_SO\
├── readme.txt       (directory listing)
├── author.txt       (name + listing)
└── history.txt      (command history)
```

## Output Expectations

**readme.txt** should contain:
- Directory listing of files in tmp_SO
- List of all catalogs and files

**author.txt** should contain:
- Author information (name and surname)
- Directory listing appended
- All files in the directory

**history.txt** should contain:
- Doskey command history
- All commands executed in the session

## Screenshots Required
Capture CMD window showing:
1. Directory creation and navigation
2. `dir` command output
3. Contents of each file using `type` command
4. Final state of C:\tmp_SO directory

## Submission
Provide:
- Screenshots of CMD execution
- Contents of all three files (readme.txt, author.txt, history.txt)
- Proof that files are located in C:\tmp_SO

## Notes
- All operations must be done in Windows CMD.EXE
- Files must be in C:\tmp_SO directory
- Use standard CMD commands (dir, mkdir, doskey)
- Include your actual name in author.txt
