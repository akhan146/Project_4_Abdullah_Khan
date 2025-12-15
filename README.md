# Project 4 – Password Analysis System

## Project Overview

This project is a Python-based password analysis system designed to demonstrate object-oriented programming, abstraction, modular design, and testing practices.

The application generates secure passwords, analyzes their strength using multiple strategies, and saves analysis results for later review. It is structured to separate domain logic, services, persistence, reporting, and testing concerns.

---

## Domain Problem

Weak passwords are a common security risk. This project addresses that problem by:
- Generating secure passwords
- Evaluating password strength and entropy
- Detecting weak or repeated patterns
- Persisting analysis results for verification

---

## Team Members and Contributions

- **Abdullah Khan** – Design, implementation, testing, documentation

---

## Project Structure

C:.
│   LICENSE
│   README.md
│   
├───data
│       exports
│       imports
│       latest_analysis.json
│       saves
│       
├───docs
│       api.md
│       architecture.md
│       testing.md
│       
├───src
│   │   domain
│   │   main.py
│   │   persistence
│   │   reports
│   │   __init__.py
│   │   
│   ├───services
│   │   │   analyzer.py
│   │   │   generator.py
│   │   │   policy.py
│   │   │   report.py
│   │   │   __init__.py
│   │   │   
│   │   └───__pycache__
│   │           generator.cpython-313.pyc
│   │           __init__.cpython-313.pyc
│   │
│   └───__pycache__
│           main.cpython-313.pyc
│
└───tests
        integration
        system
        unit

        