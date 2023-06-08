#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv[1:]
    if len(argv) != 3:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
    a = int(argv[0])
    b = int(argv[2])
    op = argv[1]

    if op == "+":
        print("{} + {} = {}" .format(a, b, add(a, b)))

    elif op == "-":
        print("{} - {} = {}" .format(a, b, sub(a, b)))

    elif op == "*":
        print("{} {} {} {} {}" .format(a, "*", b, "=", mul(a, b)))

    elif op == "/":
        print("{} {} {} {} {}" .format(a, "/", b, "=", div(a, b)))

    else:
        print("{}".format
              ("Unknown operator. Available operators: +, -, * and /"))
        exit(1)
