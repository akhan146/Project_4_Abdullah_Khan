import random
import string

# Local Password model
class Password:
    def __init__(self, value: str):
        self.value = value

    @property
    def length(self):
        return len(self.value)


# Enforces rules for passwords
class PasswordPolicy:
    def __init__(self, min_length=10):
        self.min_length = min_length

    def validate(self, password: Password):
        return password.length >= self.min_length


# Generates passwords
class PasswordGenerator:
    def __init__(self, policy: PasswordPolicy):
        self.policy = policy

    def generate(self, length=12):
        while True:
            chars = random.choices(
                string.ascii_letters + string.digits + string.punctuation,
                k=length
            )
            pwd = Password("".join(chars))
            if self.policy.validate(pwd):
                return pwd
