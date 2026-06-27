#!/bin/bash

echo "=== Task 9: Processes Using Maximum Resources ==="
echo ""

echo "Step 1: Display top processes by CPU usage (ps command)"
echo "Command: ps aux --sort=-%cpu | head -6"
ps aux --sort=-%cpu | head -6
echo ""

echo "Step 2: Display top processes by memory usage (ps command)"
echo "Command: ps aux --sort=-%mem | head -6"
ps aux --sort=-%mem | head -6
echo ""

echo "Step 3: Process using maximum operational memory"
echo "Command: ps aux --sort=-%mem | head -2"
MAX_MEM_PROC=$(ps aux --sort=-%mem | tail -1)
echo "$MAX_MEM_PROC"
MAX_MEM_PID=$(echo $MAX_MEM_PROC | awk '{print $2}')
MAX_MEM_SIZE=$(echo $MAX_MEM_PROC | awk '{print $6}')
MAX_MEM_PERCENT=$(echo $MAX_MEM_PROC | awk '{print $4}')
echo "Process using maximum memory:"
echo "  PID: $MAX_MEM_PID"
echo "  Memory (KB): $MAX_MEM_SIZE"
echo "  Memory %: $MAX_MEM_PERCENT%"
echo ""

echo "Step 4: Process using maximum CPU time"
echo "Command: ps aux --sort=-%cpu | head -2"
MAX_CPU_PROC=$(ps aux --sort=-%cpu | tail -1)
echo "$MAX_CPU_PROC"
MAX_CPU_PID=$(echo $MAX_CPU_PROC | awk '{print $2}')
MAX_CPU_PERCENT=$(echo $MAX_CPU_PROC | awk '{print $3}')
MAX_CPU_TIME=$(echo $MAX_CPU_PROC | awk '{print $10}')
echo "Process using maximum CPU:"
echo "  PID: $MAX_CPU_PID"
echo "  CPU %: $MAX_CPU_PERCENT%"
echo "  CPU Time: $MAX_CPU_TIME"
echo ""

echo "Step 5: Real-time monitoring with top (5 seconds)"
echo "Command: top -b -n 1 | head -15"
top -b -n 1 | head -15
echo ""

echo "Step 6: Display memory summary"
echo "Command: free -h"
free -h
echo ""

echo "Step 7: Display CPU information"
echo "Command: lscpu | grep -E '^CPU|^Core'"
lscpu | grep -E "^CPU|^Core" || lscpu | head -10
echo ""

echo "=== Summary ==="
echo "System Resource Usage Commands:"
echo "  ps aux --sort=-%cpu        (sort by CPU usage)"
echo "  ps aux --sort=-%mem        (sort by memory usage)"
echo "  top -b -n 1                (batch mode, single iteration)"
echo "  top -b -n 1 | head -15     (show top processes)"
echo "  free -h                    (display memory summary)"
echo "  vmstat                     (virtual memory statistics)"
echo "  iostat                     (I/O statistics)"
echo ""
echo "Columns in ps output:"
echo "  %CPU  = CPU percentage"
echo "  %MEM  = Memory percentage"
echo "  RSS   = Resident set size (actual memory used in KB)"
echo "  TIME  = CPU time used by process"
