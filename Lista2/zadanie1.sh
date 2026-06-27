#!/bin/bash

# Create directory structure and populate with files
mkdir -p tmp_SO
cd tmp_SO

# Create author file
echo "Szymon Poparda" > author.txt

# Create subdirectory
mkdir subdir

# List directory contents
ls -la > readme.txt

# Append command history
history >> author.txt

echo "Script completed"
echo "Contents of tmp_SO:"
ls -la
