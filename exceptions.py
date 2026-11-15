"""Error handling and custom exception exercises."""


class AgeNotEligibleError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class PasswordValidationError(Exception):
    pass


def validate_age(age):
    if age < 18:
        raise AgeNotEligibleError("Age must be at least 18")
    return "Age validated successfully"


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        raise InsufficientBalanceError("Withdrawal exceeds available balance")
    return balance - amount


def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Length must be at least 8 characters")
    if not any(ch.isupper() for ch in password):
        errors.append("Must contain at least one uppercase letter")
    if not any(ch.isdigit() for ch in password):
        errors.append("Must contain at least one number")
    if errors:
        raise PasswordValidationError("; ".join(errors))
    return True


if __name__ == "__main__":
    try:
        print(validate_age(int(input("Enter age: "))))
    except AgeNotEligibleError as error:
        print("Age error:", error)

    try:
        balance = float(input("Enter bank balance: "))
        amount = float(input("Enter withdrawal amount: "))
        print("Remaining balance:", withdraw(balance, amount))
    except (InsufficientBalanceError, ValueError) as error:
        print("Withdrawal error:", error)

    try:
        validate_password(input("Enter password: "))
        print("Password is valid")
    except PasswordValidationError as error:
        print("Password error:", error)
