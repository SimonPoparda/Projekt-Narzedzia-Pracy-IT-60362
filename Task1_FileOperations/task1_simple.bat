@echo off
cls
echo ===================================================
echo Task 1 - Simple File Operations
echo ===================================================
echo.

REM Navigate to root
cd /d C:\

REM Create tmp_SO directory
if not exist tmp_SO (
    mkdir tmp_SO
    echo [+] Created directory C:\tmp_SO
) else (
    echo [*] Directory C:\tmp_SO already exists
)

REM Change to tmp_SO
cd tmp_SO
echo [+] Current directory: %cd%
echo.

REM Step 1: Create readme.txt
echo Creating readme.txt...
dir > readme.txt
echo [+] readme.txt created with directory listing
echo.

REM Step 2: Create author.txt
echo Creating author.txt...
(
    echo Author Information
    echo Name and Surname: Megan Poparda
    echo Assignment: Task 1 - File Operations
    echo Date Created: %date%
    echo Time Created: %time%
    echo.
    echo Files in tmp_SO directory:
) > author.txt
dir >> author.txt
echo [+] author.txt created with author info and directory listing
echo.

REM Step 3: Capture Doskey history
echo Creating history.txt...
doskey /history > history.txt
echo [+] history.txt created with command history
echo.

REM Display results
echo ===================================================
echo Results - Files created in C:\tmp_SO
echo ===================================================
dir
echo.

echo ===================================================
echo Content of readme.txt
echo ===================================================
type readme.txt
echo.

echo ===================================================
echo Content of author.txt
echo ===================================================
type author.txt
echo.

echo ===================================================
echo Content of history.txt
echo ===================================================
type history.txt
echo.

echo ===================================================
echo Task 1 completed successfully!
echo ===================================================
pause
