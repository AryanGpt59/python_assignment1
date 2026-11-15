"""Run from the assignment root: python -m modules.geometry_demo"""
from geometry.circle import area as circle_area, circumference
from geometry.rectangle import area as rectangle_area, perimeter

if __name__ == "__main__":
    radius = float(input("Circle radius: "))
    length = float(input("Rectangle length: "))
    width = float(input("Rectangle width: "))
    print("Circle area:", circle_area(radius))
    print("Circle circumference:", circumference(radius))
    print("Rectangle area:", rectangle_area(length, width))
    print("Rectangle perimeter:", perimeter(length, width))
