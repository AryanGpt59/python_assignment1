"""Examples using Python's math, random and datetime modules."""
import math
import random
from datetime import date, datetime


def math_examples(number, base, exponent, angle_degrees):
    if number < 0:
        raise ValueError("Square root example requires a non-negative number")
    angle_radians = math.radians(angle_degrees)
    return {
        "square_root": math.sqrt(number),
        "power": math.pow(base, exponent),
        "factorial": math.factorial(int(number)),
        "sin": math.sin(angle_radians),
        "cos": math.cos(angle_radians),
        "tan": math.tan(angle_radians),
    }


def generate_otp(length=6):
    if length <= 0:
        raise ValueError("OTP length must be positive")
    return "".join(random.choices("0123456789", k=length))


def generate_password(length=12):
    if length < 4:
        raise ValueError("Use a password length of at least 4")
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    return "".join(random.SystemRandom().choices(alphabet, k=length))


def random_numbers(count, low=1, high=100):
    if count < 0 or low > high:
        raise ValueError("Invalid count or range")
    return [random.randint(low, high) for _ in range(count)]


def calculate_age(birth_date):
    today = date.today()
    years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1
    return years


if __name__ == "__main__":
    number = float(input("Enter a non-negative number (factorial uses its integer part): "))
    base = float(input("Enter base for power: "))
    exponent = float(input("Enter exponent: "))
    angle = float(input("Enter angle in degrees: "))
    print("Math results:", math_examples(number, base, exponent, angle))
    print("OTP:", generate_otp())
    print("Random password:", generate_password())
    print("Random list:", random_numbers(5))
    print("Current date/time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    dob = date.fromisoformat(input("Enter date of birth (YYYY-MM-DD): "))
    print("Age:", calculate_age(dob))
