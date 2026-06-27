#!/bin/bash

echo "Generating presentations..."

cd Task3 && python3 generate_presentation.py && cd ..
cd Task4 && python3 generate_presentation.py && cd ..
cd Task5 && python3 generate_presentation.py && cd ..

echo ""
echo "All presentations generated!"
echo ""
find . -name "*.pptx" -type f
