# Task 1 - Simple File Operations Instructions

## Overview
This task requires creating a directory structure and files using Windows CMD commands, capturing directory listings, and command history.

## Requirements
- Windows operating system with CMD.EXE access
- Administrator privileges (optional, but recommended)
- Writing permissions to C: drive

## Execution Steps

### Option 1: Automated Batch Script
1. Open Windows Command Prompt (CMD.EXE)
2. Edit the file `execute_task1.bat` and replace `[Your Name Here]` with your actual name and surname
3. Run the batch script:
   ```cmd
   execute_task1.bat
   ```
4. The script will automatically:
   - Create `C:\tmp_SO` directory
   - Create `readme.txt` with directory listing
   - Create `author.txt` with your name and directory listing
   - Create `history.txt` with Doskey command history
   - Display all created files and their contents

### Option 2: Manual Execution
If you prefer to execute commands manually:

```cmd
REM 1. Create directory
cd C:\
mkdir tmp_SO
cd tmp_SO

REM 2. Create readme.txt with directory listing
dir > readme.txt

REM 3. Create author.txt with name and directory listing
echo Author Information > author.txt
echo Name and Surname: [Your Name] >> author.txt
dir >> author.txt

REM 4. Capture Doskey history
doskey /history > history.txt

REM 5. View all files
dir

REM 6. Display file contents
type readme.txt
type author.txt
type history.txt
```

## Expected Output

After execution, you should have in `C:\tmp_SO`:

### readme.txt
- Contains directory listing showing all files and subdirectories
- Documents what files exist in the tmp_SO catalog

### author.txt
- Contains your name and surname
- Includes directory listing of tmp_SO
- Shows all files present

### history.txt
- Contains command history from Doskey
- Shows all previously executed commands

## Screenshots Required
Take screenshots of:
1. CMD window showing directory creation
2. CMD window showing `dir` command output
3. CMD window showing content of each file (readme.txt, author.txt, history.txt)
4. Final directory listing with all three files

## Notes
- All files must be located in `C:\tmp_SO`
- File contents should be visible in CMD.EXE
- Ensure your name and surname are clearly written in author.txt
- The history.txt file captures all commands used during execution

## Submission Checklist
- [ ] `C:\tmp_SO` directory created
- [ ] `readme.txt` file created with directory listing
- [ ] `author.txt` file created with name and directory listing
- [ ] `history.txt` file created with command history
- [ ] Screenshots of all files and CMD output captured
- [ ] All files are readable and accessible
