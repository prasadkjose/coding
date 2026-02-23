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
  - JavaScript (TODO)
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


## TODO

- Take custom test cases
- Add support for benchmarking (time + memory)
- Add CLI help command (`--help`)
- TS Implementation 
- C++ Implementation
- Setup Scripts to install dependecies like python3 and nodeJS for TS


---