#!/bin/bash

# Backup all .txt files with .bak extension
for file in *.txt; do
    if [[ -f "$file" ]]; then
        cp "$file" "$file.bak"
        echo "Backed up: $file -> $file.bak"
    fi
done

echo "Backup complete"
