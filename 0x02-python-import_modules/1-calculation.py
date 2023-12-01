#!/usr/bin/python3

if __name__ == "__main__":
    """print the sum of a and b """
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    """print the substration"""
    print("{} - {} = {}".format(a, b, sub(a, b)))
    """print the multiplication"""
    print("{} * {} = {}".format(a, b, mul(a, b)))
    """print the division"""
    print("{} / {} = {}".format(a, b, div(a, b)))
