import random
import string
from domain.password import Password
from services.policy import PasswordPolicy


class PasswordGenerator:
    def __init__(self, policy: PasswordPolicy):
        self.policy = policy

    def generate(self, length=12) -> Password:
        if length < self.policy.min_length:
            raise ValueError("Length below policy minimum")

        while True:
            chars = [
                random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase),
                random.choice(string.digits),
                random.choice(string.punctuation),
            ]

            chars += random.choices(
                string.ascii_letters + string.digits + string.punctuation,
                k=length - 4
            )

            random.shuffle(chars)
            pwd = Password("".join(chars))

            if self.policy.validate(pwd):
                return pwd
