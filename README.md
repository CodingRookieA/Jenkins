# Jenkins CI Pipeline with GitHub Integration (Python)

## Overview

This repository demonstrates a **production-style Continuous Integration (CI) pipeline** built using **Jenkins**, **GitHub webhooks**, and **Python**.  
The primary focus of this project is **automation, reliability, and preventing human error in the development workflow**, rather than application complexity.

A minimal Python application is intentionally used to keep attention on the CI pipeline design, failure handling, and branch protection behavior.

---

## Project Goals

- Automate builds and tests on every GitHub push using Jenkins
- Enforce code quality and correctness before changes reach the main branch
- Prevent broken or non-compliant code from being merged
- Simulate real-world CI failure scenarios and validate enforcement behavior

---

## CI Pipeline Features

### Automated Triggers
- Jenkins pipeline is automatically triggered on every push via **GitHub webhooks**
- No manual intervention required to start builds

### Environment Isolation
- Each build runs in a **clean Python virtual environment**
- Dependencies are installed consistently using `pip` and a requirements file

### Quality Gates
The pipeline enforces the following checks:
- **Linting** with `flake8` to enforce code style and detect static issues
- **Unit testing** with `pytest` to validate functionality
- Immediate pipeline failure if any stage does not pass

### Branch-Level Enforcement
- Implemented using a **Jenkins Multibranch Pipeline**
- Feature branches are built and tested independently
- Branches that fail CI checks are **blocked from merging** into the main branch
- Prevents regressions and human errors from impacting stable code

---

## Pipeline Stages

1. **Checkout**  
   Fetches the latest code from the GitHub repository

2. **Setup Python Environment**  
   Creates and activates a virtual environment  
   Installs project dependencies

3. **Lint**  
   Runs `flake8` on application source code  
   Fails the build on style or static analysis violations

4. **Test**  
   Executes unit tests using `pytest`  
   Fails the build on test errors or import issues

---

## Failure Scenarios Tested

This project intentionally validated real CI failure cases, including:

- Linting errors preventing pipeline success
- Missing or improperly structured tests causing build failure
- Import and module resolution errors detected during test collection
- Broken feature branches being isolated from the main branch via CI enforcement

These scenarios mirror common real-world failures in collaborative software teams.

---


