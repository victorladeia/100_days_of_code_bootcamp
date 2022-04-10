import art
import os
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    '+': add, 
    '-': subtract,
    '*': multiply,
    '/': divide,
}

outFlag = 'n'

while( outFlag == 'n' ):
    os.system("clear")
    print(art.logo)
    n1 = int(input("Type the first number: "))
    for key in operations:
        print(key)
    operation = input("Select a operation: ")
    n2 = int(input("Type the second number: "))
    result = operations[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {result}")
    innerFlag = input(f"Type 'y' to continue the calculation with {result}, 'n' to a new calculation or 'l' to leave the application: ")
    if ( innerFlag == 'l' ):
        outFlag = innerFlag
    while( innerFlag == 'y' ):
        n1 = result
        for key in operations:
            print(key)
        operation = input("Select a operation: ")
        n2 = int(input("Type the second number: "))
        result = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
        innerFlag = input(f"Type 'y' to continue the calculation with {result}, 'n' to a new calculation or 'l' to leave the application: ")
   


