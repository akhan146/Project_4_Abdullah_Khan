from __future__ import annotations
import math
import string
from abc import ABC, abstractmethod
from domain.password import Password


class AbstractPasswordAnalyzer(ABC):
    def __init__(self, password: Password):
        self.password = password

    @abstractmethod
    def analyze(self) -> dict:
        pass


class BasicPasswordAnalyzer(AbstractPasswordAnalyzer):
    COMMON_PASSWORDS = {"password", "123456", "qwerty", "abc123"}

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

        if pool == 0:
            return 0.0

        return round(self.password.length * math.log2(pool), 2)

    def strength(self) -> str:
        score = sum([
            self.password.length >= 8,
            self.password.has_lower,
            self.password.has_upper,
            self.password.has_digit,
            self.password.has_special
        ])

        if score <= 2:
            return "Weak"
        elif score <= 4:
            return "Medium"
        return "Strong"

    def analyze(self) -> dict:
        return {
            "masked": self.password.masked,
            "length": self.password.length,
            "entropy": self.entropy(),
            "strength": self.strength(),
            "is_common": self.password.value.lower() in self.COMMON_PASSWORDS
        }


class AdvancedPasswordAnalyzer(BasicPasswordAnalyzer):
    def has_repeats(self) -> bool:
        pw = self.password.value
        n = len(pw)

        for size in range(1, n // 2 + 1):
            for i in range(n - size * 2 + 1):
                if pw[i:i + size] == pw[i + size:i + size * 2]:
                    return True
        return False

    def analyze(self) -> dict:
        data = super().analyze()
        data["has_repeated_patterns"] = self.has_repeats()
        return data
