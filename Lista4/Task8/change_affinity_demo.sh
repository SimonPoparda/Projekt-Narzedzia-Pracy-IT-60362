#!/bin/bash

echo "=== Task 8: Changing Process CPU Affinity ==="
echo ""

echo "Step 1: Check available CPUs"
echo "Command: nproc"
nproc
echo ""

echo "Step 2: Check CPU topology"
echo "Command: lscpu | grep -E '^CPU|^NUMA'"
lscpu | grep -E "^CPU|^NUMA" || echo "CPU info:"
lscpu | head -20
echo ""

SLEEP_PID=""

echo "Step 3: Start a background process with taskset (CPU 0 only)"
echo "Command: taskset -c 0 sleep 300 &"
taskset -c 0 sleep 300 &
SLEEP_PID=$!
echo "Started sleep process with PID: $SLEEP_PID"
echo ""

echo "Step 4: Check current affinity using taskset"
echo "Command: taskset -cp $SLEEP_PID"
taskset -cp $SLEEP_PID
echo ""

echo "Step 5: Check affinity using ps"
echo "Command: ps -o pid,psr,comm -p $SLEEP_PID"
ps -o pid,psr,comm -p $SLEEP_PID
echo "(PSR column shows which CPU the process is on)"
echo ""

echo "Step 6: Change affinity to CPU 1 (if available)"
if [ $(nproc) -gt 1 ]; then
    echo "Command: taskset -cp 1 $SLEEP_PID"
    taskset -cp 1 $SLEEP_PID
else
    echo "Only 1 CPU available, cannot change to CPU 1"
fi
echo ""

echo "Step 7: Change affinity to multiple CPUs (0 and 1)"
if [ $(nproc) -gt 1 ]; then
    echo "Command: taskset -cp 0,1 $SLEEP_PID"
    taskset -cp 0,1 $SLEEP_PID
else
    echo "Only 1 CPU available, cannot set multiple CPUs"
fi
echo ""

echo "Step 8: Verify changed affinity"
echo "Command: taskset -cp $SLEEP_PID"
taskset -cp $SLEEP_PID
echo ""

echo "Cleaning up: Kill the background process"
kill $SLEEP_PID 2>/dev/null || true
echo "Process terminated"
echo ""

echo "=== Summary ==="
echo "Commands used for changing affinity:"
echo "  taskset -c CPUS ./program         (start with affinity)"
echo "  taskset -cp CPUS PID              (change running process)"
echo "  taskset -p CPUS PID               (display/change affinity)"
echo ""
echo "CPU list formats:"
echo "  0          = CPU 0 only"
echo "  0,2        = CPUs 0 and 2"
echo "  0-3        = CPUs 0, 1, 2, 3"
echo "  1,3-4      = CPUs 1, 3, and 4"
