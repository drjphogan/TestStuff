#!/usr/bin/python3.4

from sys import argv 


def is_palindrone(x):
    return x == x[::-1]


if __name__ == "__main__":
    print(is_palindrone(argv[1])) 
