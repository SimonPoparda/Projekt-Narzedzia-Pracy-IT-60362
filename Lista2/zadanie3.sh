#!/bin/bash

# Log rotation script - shifts old logs and removes oldest
LOG_FILE="log"

if [[ -f "$LOG_FILE" ]]; then
    # Remove oldest backup
    if [[ -f "$LOG_FILE.3" ]]; then
        rm "$LOG_FILE.3"
    fi

    # Shift existing backups
    if [[ -f "$LOG_FILE.2" ]]; then
        mv "$LOG_FILE.2" "$LOG_FILE.3"
    fi

    if [[ -f "$LOG_FILE.1" ]]; then
        mv "$LOG_FILE.1" "$LOG_FILE.2"
    fi

    # Backup current log
    mv "$LOG_FILE" "$LOG_FILE.1"

    echo "Log rotated: $LOG_FILE -> $LOG_FILE.1"
else
    echo "No log file to rotate"
fi
