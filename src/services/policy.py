from domain.password import Password


class PasswordPolicy:
    def __init__(
        self,
        min_length=8,
        require_upper=True,
        require_lower=True,
        require_digit=True,
        require_special=True
    ):
        self.min_length = min_length
        self.require_upper = require_upper
        self.require_lower = require_lower
        self.require_digit = require_digit
        self.require_special = require_special

    def validate(self, password: Password) -> bool:
        return all([
            password.length >= self.min_length,
            not self.require_upper or password.has_upper,
            not self.require_lower or password.has_lower,
            not self.require_digit or password.has_digit,
            not self.require_special or password.has_special
        ])
