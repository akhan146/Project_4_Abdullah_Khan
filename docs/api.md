# API Documentation

## Password

Represents a password and exposes read-only properties.

### Properties
- `length`: Length of the password
- `masked`: Masked version for display
- `has_upper`: Contains uppercase letters
- `has_lower`: Contains lowercase letters
- `has_digit`: Contains digits
- `has_special`: Contains special characters

---

## PasswordGenerator

Generates passwords that comply with a policy.

### Methods
- `generate(length=12)`: Returns a valid password

---

## PasswordAnalyzer

Analyzes password strength and entropy.

### Output
Returns a dictionary containing:
- Length
- Entropy
- Strength
- Common-password flag
