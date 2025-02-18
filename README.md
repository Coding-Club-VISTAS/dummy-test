# Autograding Tests README

## Overview

This repository is designed to automatically grade code written in **C** and **Python** using GitHub Actions. It contains pre-configured workflows for running tests on two functionalities:

- **Divisibility by 5**
- **Sum Function**

These tests will run upon a push to the repository or can be manually triggered using GitHub's **workflow_dispatch** feature. The workflow will compile and run the corresponding shell or Python scripts and check their outputs. Based on the results, it will assign scores.

## Folder Structure

The repository contains two main folders for each language:

- `c/`: This folder contains C scripts and tests.
- `python/`: This folder contains Python scripts and tests.

### Language-Specific Tests

To run the tests for a specific language, you will need to follow the corresponding test steps.

### How to Use Git to Send Your Code

1. **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Add your changes** (e.g., C or Python code) to the respective language folder (`c/` or `python/`).

3. **Commit your changes**:
    ```bash
    git add .
    git commit -m "Your commit message"
    ```

4. **Push your changes** to GitHub:
    ```bash
    git push origin main
    ```

Alternatively, you can use the GitHub website to manually add your code and commit the changes.

## Workflow Overview

There are two main tests available in this workflow. Choose the correct test for the language you're working with.

### C Language Tests

If you're working with **C**, you will need to use the following tests:

1. **Divisibility by 5 Test (C)**:
   - Path: `./c/test_divisible_by_5.sh`
   - Command: `./c/test_divisible_by_5.sh`
   - Expected Output: `"TRUE"`

2. **Sum Function Test (C)**:
   - Path: `./c/test_sum.sh`
   - Command: `./c/test_sum.sh`
   - Expected Output: `"Sum: 12"`

To run these tests, ensure that the C files are in the `c/` folder and select the **C workflow** for your pull request or push event.

### Python Language Tests

If you're working with **Python**, you will need to use the following tests:

1. **Divisibility by 5 Test (Python)**:
   - Path: `python/test_divisible_by_5.py`
   - Command: `python3 python/test_divisible_by_5.py`
   - Expected Output: `"TRUE"`

2. **Sum Function Test (Python)**:
   - Path: `python/test_sum.py`
   - Command: `python3 python/test_sum.py`
   - Expected Output: `"Sum: 12"`

To run these tests, ensure that the Python files are in the `python/` folder and select the **Python workflow** for your pull request or push event.

## How It Works

Once you push your changes or manually trigger the workflow, the GitHub Actions workflow will run the tests on the selected language:

1. **Checkout Code**: Retrieves the latest changes from the repository.
2. **Make Shell Scripts Executable**: Ensures that the shell scripts (`test_divisible_by_5.sh` and `test_sum.sh`) have execution permissions.
3. **Test Execution**: The tests will run based on the language and test selected.
   - The C tests will be executed by shell scripts.
   - The Python tests will run Python scripts.
4. **Autograding Reporter**: The results of the tests are compiled, and a score report is generated.

## Customizing Tests

You can add new tests or modify existing ones by editing the scripts in the `c/` or `python/` folders. Make sure to update the expected output and scoring system in the workflow if you add new tests.

## Important: Clean Up Unused Tests in the Workflow

To avoid running unnecessary tests, **please delete the test entries in the workflow file that you're not using**. For example, if you're only working with C, remove the Python tests from the workflow, or if you're only working with Python, remove the C tests. This will keep your workflow focused and efficient.

### Example:

If you're using **C**, the workflow file should look like this:

```yaml
runners: divisibility-test,sum-test
```

For **Python**, your workflow file would look like this:

```yaml
runners: python-divisibility-test,python-sum-test
```

## How to Trigger a Manual Test

You can trigger the workflow manually using the **GitHub Actions UI**. To do so:

1. Go to the **Actions** tab in your repository.
2. Select the **Autograding Tests** workflow.
3. Click the **Run workflow** button and select the branch you want to test.

## Conclusion

This setup allows for efficient autograding of C and Python code, making it ideal for use in classrooms or automated testing environments. Simply select the appropriate test for your language, push your code, and let the workflow handle the rest!
