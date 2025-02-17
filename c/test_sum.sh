#!/bin/bash
gcc -o sum sum_function.c
output=$(echo "5 7" | ./sum)
expected="Sum: 12"
if [[ "$output" == *"$expected"* ]]; then
    echo "Test Passed"
    exit 0
else
    echo "Test Failed"
    exit 1
fi
