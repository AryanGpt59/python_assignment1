"""Loop exercises."""


def is_automorphic(number):
    if number < 0:
        return False
    square = number * number
    return str(square).endswith(str(number))


def palindromes_in_range(start, end):
    if start > end:
        start, end = end, start
    return [n for n in range(start, end + 1) if str(n) == str(n)[::-1]]


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def password_retry():
    correct_password = "python123"  # Change this sample password as required.
    for attempt in range(1, 4):
        entered = input("Enter password: ")
        if entered == correct_password:
            print("Login successful")
            return
        print(f"Incorrect password. Attempts left: {3 - attempt}")
    print("Account blocked after 3 failed attempts")


def print_patterns(rows):
    print("\nTriangle")
    for i in range(1, rows + 1):
        print("* " * i)
    print("\nPyramid")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)
    print("\nDiamond")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "* " * (2 * i - 1))


if __name__ == "__main__":
    n = int(input("Enter a number to check automorphic: "))
    print("Automorphic" if is_automorphic(n) else "Not automorphic")
    low, high = map(int, input("Enter range (start end): ").split())
    print("Palindrome numbers:", palindromes_in_range(low, high))
    a, b = map(int, input("Enter two integers for GCD and LCM: ").split())
    print("HCF/GCD:", gcd(a, b), "LCM:", lcm(a, b))
    password_retry()
    print_patterns(int(input("Number of pattern rows: ")))
