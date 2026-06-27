#!/bin/bash

# Interactive wrapper for bubble sort function
source ./sortowanie.sh

echo "Enter three numbers to sort:"
read -p "First number: " num1
read -p "Second number: " num2
read -p "Third number: " num3

sortuj $num1 $num2 $num3
