"""Conditional statement exercises."""


def electricity_bill(units):
    """Progressive slabs: first 100 at 5, next 200 at 7, remainder at 10."""
    if units < 0:
        raise ValueError("Units cannot be negative")
    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 200 * 7 + (units - 300) * 10
    if bill > 2000:
        bill *= 1.05
    return bill


def loan_approval(salary, credit_score, age):
    checks = [salary > 30000, credit_score >= 700, 21 <= age <= 60]
    if all(checks):
        return "Approved"
    if sum(checks) == 2:
        return "Conditionally Approved"
    return "Rejected"


def classify_number(number):
    sign = "Positive" if number > 0 else "Negative" if number < 0 else "Zero"
    parity = "Even" if number % 2 == 0 else "Odd"
    divisible_by_3_and_5 = number % 3 == 0 and number % 5 == 0
    return sign, parity, divisible_by_3_and_5


def exam_result(marks):
    if len(marks) != 5:
        raise ValueError("Enter marks for exactly 5 subjects")
    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")
    if any(mark < 33 for mark in marks):
        return {"status": "Fail", "average": sum(marks) / 5, "division": None}
    average = sum(marks) / 5
    division = "First" if average >= 60 else "Second" if average >= 50 else "Third" if average >= 40 else "Pass (no division specified)"
    return {"status": "Pass", "average": average, "division": division}


if __name__ == "__main__":
    units = float(input("Enter electricity units: "))
    print(f"Electricity bill: Rs. {electricity_bill(units):.2f}")

    salary = float(input("\nEnter salary: "))
    score = int(input("Enter credit score: "))
    age = int(input("Enter age: "))
    print("Loan status:", loan_approval(salary, score, age))

    number = int(input("\nEnter an integer: "))
    sign, parity, divisible = classify_number(number)
    print(sign, "|", parity, "| Divisible by both 3 and 5:", divisible)

    marks = [float(input(f"Marks in subject {i + 1}: ")) for i in range(5)]
    print("Exam result:", exam_result(marks))
