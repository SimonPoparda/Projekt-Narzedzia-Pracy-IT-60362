@echo off
REM Task 1 - File Operations with CMD
REM This script creates directory structure and executes required commands

REM Create tmp_SO directory in C:
cd C:\
if not exist tmp_SO (
    mkdir tmp_SO
    echo Directory tmp_SO created
) else (
    echo Directory tmp_SO already exists
)

REM Navigate to tmp_SO
cd tmp_SO

REM Create readme.txt with directory listing
dir > readme.txt
echo. >> readme.txt
echo ===== Directory contents listed above ===== >> readme.txt

REM Create author.txt with name and surname
(
echo Author Information
echo Name and Surname: [Your Name Here]
echo Date: %date%
echo Time: %time%
) > author.txt

REM Append directory listing to author.txt
echo. >> author.txt
echo ===== Current Directory Listing ===== >> author.txt
dir >> author.txt

REM Capture Doskey history to history.txt
doskey /history > history.txt

REM Display the contents created
echo.
echo ===== Files created in C:\tmp_SO =====
dir

echo.
echo ===== Content of readme.txt =====
type readme.txt

echo.
echo ===== Content of author.txt =====
type author.txt

echo.
echo ===== Content of history.txt =====
type history.txt

pause
