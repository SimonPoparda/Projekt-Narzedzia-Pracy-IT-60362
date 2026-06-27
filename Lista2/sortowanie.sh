#!/bin/bash

# Bubble sort three numbers in ascending order
sortuj() {
    local a=$1
    local b=$2
    local c=$3

    local arr=($a $b $c)

    # Bubble sort algorithm
    for ((i=0; i<3; i++)); do
        for ((j=0; j<3-i-1; j++)); do
            if [[ ${arr[j]} -gt ${arr[$((j+1))]} ]]; then
                # Swap elements
                temp=${arr[j]}
                arr[$j]=${arr[$((j+1))]}
                arr[$((j+1))]=$temp
            fi
        done
    done

    echo "Sorted values: ${arr[0]} ${arr[1]} ${arr[2]}"
}

# Call sort function with arguments
sortuj $1 $2 $3
