import string
import math
import random
from abc import ABC, abstractmethod


class Password:
    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Password must be a string")
        if not value:
            raise ValueError("Password cannot be empty")
        self.value = value

    @property
    def masked(self) -> str:
        return "*" * len(self.value)

    @property
    def length(self) -> int:
        return len(self.value)

    @property
    def has_upper(self) -> bool:
        return any(c.isupper() for c in self.value)

    @property
    def has_lower(self) -> bool:
        return any(c.islower() for c in self.value)

    @property
    def has_digit(self) -> bool:
        return any(c.isdigit() for c in self.value)

    @property
    def has_special(self) -> bool:
        return any(c in string.punctuation for c in self.value)


class AbstractPasswordAnalyzer(ABC):
    def __init__(self, password: Password):
        self.password = password

    @abstractmethod
    def analyze(self) -> dict:
        pass


class BasicPasswordAnalyzer(AbstractPasswordAnalyzer):
    COMMON = {"password", "123456", "qwerty", "abc123"}

    def entropy(self) -> float:
        pool = 0
        if self.password.has_lower:
            pool += 26
        if self.password.has_upper:
            pool += 26
        if self.password.has_digit:
            pool += 10
        if self.password.has_special:
            pool += len(string.punctuation)

        return round(self.password.length * math.log2(pool), 2) if pool else 0

    def strength(self) -> str:
        score = sum([
            self.password.length >= 8,
            self.password.has_lower,
            self.password.has_upper,
            self.password.has_digit,
            self.password.has_special,
        ])

        if score <= 2:
            return "Weak"
        elif score <= 4:
            return "Medium"
        return "Strong"

    def analyze(self) -> dict:
        return {
            "length": self.password.length,
            "entropy": self.entropy(),
            "strength": self.strength(),
            "is_common": self.password.value.lower() in self.COMMON,
        }


class AdvancedPasswordAnalyzer(BasicPasswordAnalyzer):
    def analyze(self) -> dict:
        data = super().analyze()
        data["has_repeated_chars"] = len(set(self.password.value)) < self.password.length
        return data


class PasswordPolicy:
    def __init__(self, min_length=10):
        self.min_length = min_length

    def validate(self, password: Password) -> bool:
        return password.length >= self.min_length


class PasswordGenerator:
    def __init__(self, policy: PasswordPolicy):
        self.policy = policy

    def generate(self, length=12) -> Password:
        while True:
            chars = random.choices(
                string.ascii_letters + string.digits + string.punctuation,
                k=length
            )
            password = Password("".join(chars))
            if self.policy.validate(password):
                return password


class PasswordReport:
    def __init__(self, results: dict):
        self.results = results

    def display(self):
        print("Password Analysis Report")
        print("-" * 25)
        for key, value in self.results.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def save_results(filename: str, results: dict):
    path = DATA_DIR / filename
    with open(path, "w") as file:
        json.dump(results, file, indent=2)

def load_results(filename: str) -> dict:
    path = DATA_DIR / filename
    with open(path, "r") as file:
        return json.load(file)




def main():
    policy = PasswordPolicy()
    generator = PasswordGenerator(policy)
    password = generator.generate()

    print(f"Generated Password: {password.masked}")

    analyzers = [
        BasicPasswordAnalyzer(password),
        AdvancedPasswordAnalyzer(password),
    ]

    combined_results = {}

    for analyzer in analyzers:
        results = analyzer.analyze()
        combined_results.update(results)

        report = PasswordReport(results)
        print()
        report.display()

    save_results("latest_analysis.json", combined_results)
    print("\nResults saved to data/latest_analysis.json")

    loaded = load_results("latest_analysis.json")
    print("Loaded results:", loaded)



if __name__ == "__main__":
    main()

