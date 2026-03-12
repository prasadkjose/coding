# Practice Coding

A lightweight local setup for practicing coding problems in **Python**, **TypeScript**, and **C++** without logging into LeetCode or any online judge.

Focus on solving problems. Skip the sign-in walls.

---

## Why This Exists

Online judges are great but sometimes you just want:

- No login
- No browser tabs
- No copy-paste friction
- Full control over your test cases
- A distraction-free environment

## Features

- One folder per problem
- Auto-generates solution + test skeletons
- Simple test runner from a single entry point
- Works locally, no internet required
- Language support:
    - Python
    - TypeScript
    - C++ (TODO)

---

## Project Structure

Each problem lives in its own directory. Supports 2 level nesting of problems

```bash
arrays/
└── contains_duplicate/
    ├── contains_duplicate.py
    ├── contains_duplicate.ts
    ├── contains_duplicate.cpp
    └── test/
        ├── test_contains_duplicate.py
        ├── contains_duplicate.ts
        └── contains_duplicate.cpp
```

## Setup a new Problem

```bash
python3 run.py init <problem Path>
python3 run.py init arrays/contains_duplicate
```

Python script to take the problem name and create .py and .ts files.

## Test

```bash
python3 run.py test <problem Path>
python3 run.py test arrays/contains_duplicate
```

## Requirements

This project requires Python 3.10+ and Node.js for TypeScript support.

### Installation

1. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Install Node.js dependencies (for TypeScript support):

    ```bash
    npm install
    ```

3. Install pre-commit hooks:
    ```bash
    pre-commit install
    ```

## Pre-commit Setup

### Available Hooks

- **Black**: Python code formatting
- **Ruff**: Python linting and error detection
- **isort**: Import sorting
- **ESLint**: TypeScript/JavaScript linting
- **Prettier**: Code formatting for TypeScript/JavaScript

## TODO

- Reset and Remove ALL exisitng solution
- Take test cases from a common json or yaml file
- Add support for benchmarking (time + memory)
- Add CLI help command (`--help`)
- TS Implementation (DONE)
- C++ Implementation
- Setup Scripts to install dependecies like python3 and nodeJS for TS
- Additional language support in an existing solution
- A migrator to propogate breaking change to earlier versions.
- Add a total number of problems solved.
- Report/calender generation

---
