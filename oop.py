"""Object-oriented programming exercises."""

# 1. Multilevel inheritance: Vehicle -> Car -> ElectricCar
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_vehicle(self):
        return f"Brand: {self.brand}"


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_kwh):
        super().__init__(brand, model)
        self.battery_kwh = battery_kwh

    def details(self):
        return f"{self.brand} {self.model}, battery: {self.battery_kwh} kWh"


# 2. Multiple inheritance: Teacher + Researcher -> Professor
class Teacher:
    def teach(self):
        return "Professor teaches students"


class Researcher:
    def research(self):
        return "Professor conducts research"


class Professor(Teacher, Researcher):
    pass


# 3. Hierarchical inheritance: Shape -> Circle, Rectangle, Triangle
class Shape:
    def description(self):
        return "This is a shape"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592653589793 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length, self.width = length, width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base, self.height = base, height

    def area(self):
        return 0.5 * self.base * self.height


# 4. Method overriding: Animal -> Dog/Cat
class Animal:
    def sound(self):
        return "Animal makes a sound"


class Dog(Animal):
    def sound(self):
        return "Dog barks"


class Cat(Animal):
    def sound(self):
        return "Cat meows"


# 5. Operator overloading: add two complex numbers
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real, self.imaginary = real, imaginary

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __str__(self):
        sign = "+" if self.imaginary >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imaginary)}i"


# 6. Private variable (__salary)
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = salary


# 7. ATM system using encapsulation: hide PIN and balance
class ATM:
    def __init__(self, pin, balance=0):
        self.__pin = str(pin)
        self.__balance = float(balance)

    def check_pin(self, entered_pin):
        return self.__pin == str(entered_pin)

    def get_balance(self, entered_pin):
        if not self.check_pin(entered_pin):
            raise PermissionError("Incorrect PIN")
        return self.__balance

    def withdraw(self, entered_pin, amount):
        if not self.check_pin(entered_pin):
            raise PermissionError("Incorrect PIN")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        return self.__balance


# 8. Game character base class and specialized subclasses
class GameCharacter:
    def __init__(self, name, health):
        self.name, self.health = name, health

    def attack(self):
        return f"{self.name} performs a basic attack"


class Warrior(GameCharacter):
    def attack(self):
        return f"{self.name} attacks with a sword"


class Mage(GameCharacter):
    def attack(self):
        return f"{self.name} casts a spell"


class Archer(GameCharacter):
    def attack(self):
        return f"{self.name} shoots an arrow"


if __name__ == "__main__":
    ev = ElectricCar("Tata", "Nexon EV", 40.5)
    print("1.", ev.details())
    prof = Professor()
    print("2.", prof.teach(), "|", prof.research())
    print("3. Areas:", Circle(3).area(), Rectangle(4, 5).area(), Triangle(4, 6).area())
    print("4.", Dog().sound(), "|", Cat().sound())
    print("5.", ComplexNumber(2, 3) + ComplexNumber(4, -1))
    employee = Employee(50000)
    print("6. Salary:", employee.get_salary())
    atm = ATM("1234", 5000)
    print("7. ATM balance:", atm.get_balance("1234"))
    print("8.", Warrior("Knight", 100).attack(), "|", Mage("Wizard", 80).attack(), "|", Archer("Ranger", 90).attack())
