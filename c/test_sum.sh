#!/bin/bash
gcc -o ./c/sum ./c/sum_function.c
output=$(echo "5 7" | ./c/sum)
expected="Sum: 12"
if [[ "$output" == *"$expected"* ]]; then
    echo "$output"
    exit 0
else
    echo "Test Failed"
    exit 1
fi
