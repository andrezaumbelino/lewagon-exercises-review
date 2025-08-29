# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys


def main():
    """Implement the calculator"""
    num1 = int(sys.argv[1])
    oper = sys.argv[2]
    num2 = int(sys.argv[3])
    total = 0

    if oper == "+":
        total = num1 + num2
    if oper == "-":
        total = num1 - num2
    if oper == "/":
        total = num1/num2
    if oper == "*":
        total = num1 * num2
    return total

if __name__ == "__main__":
    print(main())
