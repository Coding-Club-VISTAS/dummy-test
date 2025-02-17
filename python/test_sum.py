import subprocess

def test_sum():
    process = subprocess.run(["python3", "sum_function.py"], input="5\n7\n", text=True, capture_output=True)
    assert "Sum: 12" in process.stdout, "Test Failed"

test_sum()
print("Test Passed")
