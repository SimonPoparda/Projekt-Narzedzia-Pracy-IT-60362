#!/bin/bash

echo "=== Task 7: Changing Process Priority ==="
echo ""

SLEEP_PID=""

echo "Step 1: Start a background process"
echo "Command: sleep 300 &"
sleep 300 &
SLEEP_PID=$!
echo "Started sleep process with PID: $SLEEP_PID"
echo ""

echo "Step 2: Check current priority using ps"
echo "Command: ps -o pid,nice,comm -p $SLEEP_PID"
ps -o pid,nice,comm -p $SLEEP_PID
echo ""

echo "Step 3: Check priority using top (waiting 2 seconds)"
echo "Command: top -b -n 1 -p $SLEEP_PID | grep sleep"
top -b -n 1 -p $SLEEP_PID | grep -E "sleep|PID|NI" || true
echo ""

echo "Step 4: Change priority to +5 (lower priority)"
echo "Command: renice +5 -p $SLEEP_PID"
renice +5 -p $SLEEP_PID
echo ""

echo "Step 5: Verify changed priority with ps"
echo "Command: ps -o pid,nice,comm -p $SLEEP_PID"
ps -o pid,nice,comm -p $SLEEP_PID
echo ""

echo "Step 6: Change priority to -5 (higher priority, requires permissions)"
echo "Command: sudo renice -5 -p $SLEEP_PID"
sudo renice -5 -p $SLEEP_PID 2>/dev/null || echo "Note: Cannot set negative priority without root"
echo ""

echo "Step 7: Final priority check"
echo "Command: ps -o pid,nice,comm -p $SLEEP_PID"
ps -o pid,nice,comm -p $SLEEP_PID
echo ""

echo "Cleaning up: Kill the background process"
kill $SLEEP_PID 2>/dev/null || true
echo "Process terminated"
echo ""

echo "=== Summary ==="
echo "Commands used for changing priority:"
echo "  nice -n VALUE ./program      (start with priority)"
echo "  renice VALUE -p PID          (change running process)"
echo "  chrt -p PRIORITY PID         (change real-time priority)"
