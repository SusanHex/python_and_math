
from typing import Tuple


def roots(a: float, b: float, c: float) -> tuple:
    D = (b*b - 4*a*c)**0.5
    return ((-b + D)/(2/a), (-b - D)/(2/a))


def main():
    while True:
        numbers = input("What are your three numbers? (use spaces): ").split(" ")
        if len(numbers) == 3:
            temp = []
            for num in numbers:
                temp.append(float(num))
            numbers = temp
            two_roots = roots(*numbers)
            print(f"x1: {two_roots[0]}, x2: {two_roots[1]}")
            break
        else:
            print("Must have three numbers")
            
if __name__ == "__main__":
    main()