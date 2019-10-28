#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: October 2019
# This program outputs the factorial of a positive integer


def main():
    # This function outputs the factorial of a positive integer

    # Variables
    factorial = 1
    counter = 0

    # Input
    integer = int(input("Enter a positive integer: "))
    print("")

    # Process
    while integer > counter:
        print("{0}".format(counter))
        counter += 1
        factorial = factorial*counter

    # Output
    print("The factorial is ", factorial)


if __name__ == "__main__":
    main()
