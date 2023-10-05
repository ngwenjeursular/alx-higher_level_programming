#!/usr/bin/python3

if __name__ =="__main__":
    """print sum, diff, multiplication and division of 10 and 5"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")
