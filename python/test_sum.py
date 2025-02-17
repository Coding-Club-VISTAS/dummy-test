import subprocess

print("Running Python Test for Sum Function...")

def test_sum():
    process = subprocess.run(["python3", "python/sum_function.py"], input="5\n7\n", text=True, capture_output=True)

    # Debugging: Print the actual captured output
    print("Exit Code:", process.returncode)
    print("Captured Output:", repr(process.stdout))  # Use repr() to see hidden characters
    print("Captured Errors:", repr(process.stderr))

    assert process.returncode == 0, "Script encountered an error"
    assert "Sum: 12" in process.stdout.strip(), "Test Failed"

test_sum()
print("Python Test for Sum Function Passed")
