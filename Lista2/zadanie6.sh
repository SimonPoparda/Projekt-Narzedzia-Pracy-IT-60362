#!/bin/bash

# Demonstrate until loop - increments counter until exceeding index value
index=60362
counter=1

until [[ $counter -gt $index ]]; do
    ((counter++))
done

echo "Until loop completed - processed $index iterations"
