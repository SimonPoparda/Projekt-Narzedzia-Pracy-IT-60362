#!/bin/bash

# Task 1 - Simple File Operations (Bash version)
# This script creates directory structure and files using bash commands

echo "=================================================="
echo "Task 1 - Simple File Operations (Bash)"
echo "=================================================="
echo ""

# Set up directory path
WORK_DIR="$HOME/tmp_SO"

# Create tmp_SO directory
if [ ! -d "$WORK_DIR" ]; then
    mkdir -p "$WORK_DIR"
    echo "[+] Created directory: $WORK_DIR"
else
    echo "[*] Directory $WORK_DIR already exists"
fi

# Change to tmp_SO
cd "$WORK_DIR"
echo "[+] Current directory: $(pwd)"
echo ""

# Step 1: Create readme.txt with directory listing
echo "Creating readme.txt..."
{
    echo "Task 1 - Simple File Operations"
    echo "================================"
    echo ""
    echo "Directory listing of $WORK_DIR:"
    echo ""
    ls -lah
} > readme.txt
echo "[+] readme.txt created"
echo ""

# Step 2: Create author.txt with author information and directory listing
echo "Creating author.txt..."
{
    echo "Author Information"
    echo "=================="
    echo "Name and Surname: Megan Poparda"
    echo "Assignment: Task 1 - File Operations"
    echo "Date Created: $(date '+%Y-%m-%d')"
    echo "Time Created: $(date '+%H:%M:%S')"
    echo ""
    echo "Files in $WORK_DIR:"
    echo ""
    ls -lah
} > author.txt
echo "[+] author.txt created"
echo ""

# Step 3: Capture bash history to history.txt
echo "Creating history.txt..."
history > history.txt 2>/dev/null || {
    echo "# Bash Command History" > history.txt
    echo "# Note: History only shows commands from this session" >> history.txt
}
echo "[+] history.txt created"
echo ""

# Display results
echo "=================================================="
echo "Files created in $WORK_DIR"
echo "=================================================="
ls -lah
echo ""

echo "=================================================="
echo "Content of readme.txt"
echo "=================================================="
cat readme.txt
echo ""

echo "=================================================="
echo "Content of author.txt"
echo "=================================================="
cat author.txt
echo ""

echo "=================================================="
echo "Content of history.txt"
echo "=================================================="
cat history.txt
echo ""

echo "=================================================="
echo "Task 1 completed successfully!"
echo "=================================================="
