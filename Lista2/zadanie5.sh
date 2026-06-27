#!/bin/bash

# Demonstrate while loop - increments counter until reaching index value
index=60362
counter=1

while [[ $counter -le $index ]]; do
    ((counter++))
done

echo "While loop completed - processed $index iterations"
