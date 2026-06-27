#!/bin/bash

# Recursively display directory tree structure with proper formatting
tree_display() {
    local dir="$1"
    local prefix="$2"

    local files=()
    local dirs=()

    # Separate files and directories
    for item in "$dir"/*; do
        if [[ -d "$item" ]]; then
            dirs+=("$item")
        elif [[ -f "$item" ]]; then
            files+=("$item")
        fi
    done

    # Display all files in current directory
    for file in "${files[@]}"; do
        echo "${prefix}├── $(basename "$file")"
    done

    # Recursively display subdirectories
    for ((i=0; i<${#dirs[@]}; i++)); do
        dir_item="${dirs[$i]}"
        if [[ $i -eq $((${#dirs[@]} - 1)) ]]; then
            echo "${prefix}└── $(basename "$dir_item")/"
            tree_display "$dir_item" "${prefix}    "
        else
            echo "${prefix}├── $(basename "$dir_item")/"
            tree_display "$dir_item" "${prefix}│   "
        fi
    done
}

# Use provided directory or current directory
if [[ -z "$1" ]]; then
    start_dir="."
else
    start_dir="$1"
fi

echo "$(basename "$start_dir")/"
tree_display "$start_dir" ""
