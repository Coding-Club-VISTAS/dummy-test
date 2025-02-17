#!/bin/bash
gcc -o divisible divisible_by_5.c
output=$(echo "10" | ./divisible)
expected="Divisible by 5"
if [[ "$output" == *"$expected"* ]]; then
    echo "Test Passed"
    exit 0
else
    echo "Test Failed"
    exit 1
fi
