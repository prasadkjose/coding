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

## Features

| Status | Feature | GitHub Issue |
|--------|---------|--------------|
| ✅ | Add pre commit hooks to standardize commit messages | [Completed](https://github.com/prasadkjose/coding/issues/1) |
| ❌ | Reset and Remove ALL existing solution | [#4](https://github.com/prasadkjose/coding/issues/4) |
| ❌ | Take test cases from a common JSON or YAML file | [#5](https://github.com/prasadkjose/coding/issues/5) |
| ❌ | Add support for benchmarking (time + memory) | [#6](https://github.com/prasadkjose/coding/issues/6) |
| ❌ | Add CLI help command (`--help`) | [#7](https://github.com/prasadkjose/coding/issues/7) |
| ✅ | TypeScript Implementation | [Completed](https://github.com/prasadkjose/coding/issues/7) |
| ❌ | C++ Implementation | [#8](https://github.com/prasadkjose/coding/issues/8) |
| ❌ | Setup Scripts to install dependencies like python3 and nodeJS for TS | [#9](https://github.com/prasadkjose/coding/issues/9) |
| ❌ | Additional language support in an existing solution | [#10](https://github.com/prasadkjose/coding/issues/10) |
| ❌ | A migrator to propagate breaking change to earlier versions | [#11](https://github.com/prasadkjose/coding/issues/11) |
| ❌ | Add a total number of problems solved | [#12](https://github.com/prasadkjose/coding/issues/12) |
| ❌ | Report/calendar generation | [#13](https://github.com/prasadkjose/coding/issues/13) |

---
