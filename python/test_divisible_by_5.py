import subprocess

print("Running Python Test for Divisibility by 5...")

def test_divisibility():
    process = subprocess.run(["python3", "python/divisible_by_5.py"], input="10\n", text=True, capture_output=True)

    # Debugging: Print the actual captured output
    print("Exit Code:", process.returncode)
    print("Captured Output:", repr(process.stdout))  # Use repr() to see any hidden characters
    print("Captured Errors:", repr(process.stderr))

    assert process.returncode == 0, "Script encountered an error"
    assert "Divisible by 5" in process.stdout.strip(), "Test Failed"

test_divisibility()
print("Python Test for Divisibility Passed")
