import subprocess

def test_divisibility():
    process = subprocess.run(["python3", "divisible_by_5.py"], input="10\n", text=True, capture_output=True)
    assert "Divisible by 5" in process.stdout, "Test Failed"

test_divisibility()
print("Test Passed")
