# Architecture Overview

This project is a password analysis system designed to generate, evaluate, and persist password strength data.

## High-Level Structure

The system follows a layered design:

- Domain Layer: Core data models (Password)
- Services Layer: Business logic (generation, analysis, policies)
- Persistence Layer: Saving and loading results
- Reporting Layer: Formatting and displaying results
- Tests: Unit, integration, and system-level validation

## Execution Flow

1. The application starts in `main.py`
2. A password is generated using a policy
3. The password is analyzed using multiple analyzers
4. Results are displayed to the user
5. Results are saved to disk and reloaded for verification

This separation improves maintainability and testability.
