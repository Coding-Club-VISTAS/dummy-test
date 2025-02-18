#!/bin/bash

# Compile the C program silently (redirect output)
gcc -o ./c/divisible ./c/divisible_by_5.c 2>/dev/null

# Ensure compilation was successful
if [[ ! -f ./c/divisible ]]; then
    echo "Compilation failed!"
    exit 1
fi

# Run the program and capture output
output=$(echo "10" | ./c/divisible)

# Ensure only the output is printed
echo "$output"
