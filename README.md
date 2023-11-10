[![CI](https://github.com/nogibjj/mini4-mz223/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/mini4-mz223/actions/workflows/cicd.yml)

# Week 4 Mini-project: Create a GitHub Actions Matrix Build that tests more than one than one version of Python.

## Overview
This repository contains a Python script (`main.py`) for loading a CSV file into a pandas DataFrame and printing its shape. The script is an introductory example of using pandas for data analysis, specifically for understanding the structure of a dataset.

## What's GitHub Matrix Build
GitHub Actions is a CI/CD (Continuous Integration and Continuous Delivery) platform that allows you to automate your build, test, and deployment workflows right within your GitHub repository.

A matrix build in GitHub Actions is a feature that allows you to run jobs across multiple versions of a language, multiple operating systems, or any other combination of variables you define. By using a matrix build, you can greatly simplify your workflow configuration and ensure that your code works as expected in different environments.

Here's a breakdown of how it works:

- `Define the Matrix`: In your workflow file (usually .github/workflows/main.yml), you define a matrix under the strategy key. This matrix includes the different variables you want to test against.

- `Parallel Execution`: GitHub Actions will then create a job for each combination of the variables you've defined in the matrix. These jobs run in parallel, saving time compared to running them sequentially.

- `Custom Configuration`: You can customize the matrix to include exclude rules or include additional specific combinations of the variables.

## GitHub Actions workflow file
It will tests at least 3 versions of Python (Version 3.7 or 3.8 or 3.9)
```
name: Test Multiple Python Versions using Github Actions Matrix
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7,3.8,3.9]
    steps:
      - uses: actions/checkout@v3
      - name: set up Python ${{ matrix.python-version }} 
        uses: actions/setup-python@v3
        with:
          python-version: ${{ matrix.python-version }} 
      - name: install packages
        run: make install
      - name: lint
        run: make lint
      - name: test
        run: make test
      - name: format
        run: make format
```

## Installation

Before running the script, ensure you have Python installed on your system. This script was written using Python 3.9.7, but it should be compatible with any Python 3.x version.

Additionally, you'll need to install pandas. It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install pandas
```

Usage
To execute the script, run the following command from the root of the repository:
```
python main.py
```
The script will load the data from ./assets/datasets/credit/train.csv and print the shape of the DataFrame to the console.

Project Structure
* `main.py`: The main script file.
* `assets/datasets/credit/train.csv`: The dataset file (not included in the repository).
* `requirements.txt`: The file listing the necessary Python dependencies.
* `test_main.py`: Contains unit tests for main.py to ensure the load function works correctly.

## Continuous Integration with GitHub Actions

The project uses GitHub Actions, employing the following commands:

- `make install`: Installs project dependencies.
- `make test`: Runs unit tests.
- `make format`: Formats the code according to the specified style.
- `make lint`: Checks the code for potential errors and style issues.
![Image](./images/WechatIMG792.jpg)

### CI Results
[Please click here](https://github.com/nogibjj/mini4-mz223/actions)
