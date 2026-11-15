"""Functions and recursion exercises."""


def factorial_loop(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers")
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result


def sum_natural_recursive(n):
    if n < 0:
        raise ValueError("Enter a non-negative integer")
    if n == 0:
        return 0
    return n + sum_natural_recursive(n - 1)


def reverse_string_recursive(text):
    if len(text) <= 1:
        return text
    return reverse_string_recursive(text[1:]) + text[0]


def power_recursive(x, n):
    """Calculates x**n for integer n, including negative exponents."""
    if n == 0:
        return 1
    if n < 0:
        if x == 0:
            raise ZeroDivisionError("Zero cannot have a negative exponent")
        return 1 / power_recursive(x, -n)
    half = power_recursive(x, n // 2)
    return half * half if n % 2 == 0 else x * half * half


if __name__ == "__main__":
    n = int(input("Enter a number for factorial: "))
    print("Factorial:", factorial_loop(n))
    n = int(input("Enter n for sum 1..n: "))
    print("Sum:", sum_natural_recursive(n))
    print("Reverse:", reverse_string_recursive(input("Enter a string: ")))
    x = float(input("Enter base: "))
    exponent = int(input("Enter integer exponent: "))
    print("Power:", power_recursive(x, exponent))
