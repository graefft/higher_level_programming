#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print('Usage: ./100-mycalculator.py <a> <operator> <b>')
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print('{:d} + {:d} = {:d}'.format(a, b, add(int(a, b))))
        elif argv[2] == "-":
            print('{:d} - {:d} = {:d}'.format(a, b, sub(int(a, b))))
        elif argv[2] == "*":
            print('{:d} * {:d} = {:d}'.format(a, b, mul(int(a, b))))
        elif argv[2] == "/":
            print('{:d} / {:d} = {:d}'.format(a, b, div(int(a, b))))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
