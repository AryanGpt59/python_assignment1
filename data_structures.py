"""List, tuple, set and dictionary exercises."""


def rotate_list(values, k, direction="right"):
    if not values:
        return []
    k %= len(values)
    if direction.lower() == "right":
        return values[-k:] + values[:-k] if k else values[:]
    if direction.lower() == "left":
        return values[k:] + values[:k]
    raise ValueError("direction must be 'left' or 'right'")


def remove_duplicates_preserve_order(values):
    result, seen = [], set()
    for item in values:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def find_missing_number(values, n=None):
    """Input should contain distinct values from 1..n with one value missing."""
    if n is None:
        n = len(values) + 1
    return n * (n + 1) // 2 - sum(values)


def tuple_operations(subjects):
    subjects = tuple(subjects)
    if len(subjects) != 5:
        raise ValueError("Exactly five subjects are required")
    return subjects[2], len(subjects), subjects.index(subjects[0])


def pairs_to_dictionary(pairs):
    return dict(pairs)


def swap_tuple_ends(values):
    if len(values) < 2:
        return tuple(values)
    return (values[-1],) + tuple(values[1:-1]) + (values[0],)


def is_subset(first, second):
    return set(first).issubset(set(second))


def student_marks_analyzer(marks):
    """marks: {student_name: marks}; returns topper, class average, failures."""
    if not marks:
        return {"topper": None, "average": 0, "failures": []}
    topper = max(marks, key=marks.get)
    average = sum(marks.values()) / len(marks)
    failures = [name for name, score in marks.items() if score < 33]
    return {"topper": topper, "top_marks": marks[topper], "average": average, "failures": failures}


class Library:
    def __init__(self):
        self.books = {}  # book title -> available quantity

    def add_book(self, title, quantity=1):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.books[title] = self.books.get(title, 0) + quantity

    def borrow_book(self, title, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.books.get(title, 0) < quantity:
            return False
        self.books[title] -= quantity
        return True

    def display(self):
        return self.books.copy()


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Rotate right by 2:", rotate_list(nums, 2, "right"))
    print("Rotate left by 2:", rotate_list(nums, 2, "left"))
    print("Remove duplicates:", remove_duplicates_preserve_order([1, 2, 2, 3, 1]))
    print("Missing number:", find_missing_number([1, 2, 4, 5]))
    subjects = ("Python", "DBMS", "OS", "CN", "Maths")
    print("Third, total, index:", tuple_operations(subjects))
    print("Tuple to dictionary:", pairs_to_dictionary(((1, "A"), (2, "B"))))
    print("Swap tuple ends:", swap_tuple_ends((1, 2, 3, 4)))
    print("Subset:", is_subset({1, 2}, {1, 2, 3}))
    print("Marks:", student_marks_analyzer({"Aman": 80, "Riya": 92, "Dev": 25}))
    library = Library()
    library.add_book("Python Basics", 5)
    print("Borrow successful:", library.borrow_book("Python Basics", 2))
    print("Library stock:", library.display())
