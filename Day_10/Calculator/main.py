import art
import os

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def calc(operation, a, b):
    if ( operation == '+' ) :
        return sum(a, b)
    elif ( operation == '-' ):
        return sub(a, b)
    elif ( operation == '*' ):
        return mult(a, b)
    elif operation == '/':
        return div(a, b)


flagOut = 'n'

while( flagOut == 'n' ):
    os.system('clear')
    print( art.logo )
    n1 = int(input("What's the first number?: "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    n2 = int(input("What's the next number?: "))
    result = calc(operation, n1, n2)
    print(f"{n1} {operation} {n2} = {result}")
    flagfIn = input("Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    while( flagfIn == 'y' ):
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        n2 = int(input("What's the next number?: "))
        result = calc(operation, result, n2)
        print(f"{result} {operation} {n2} = {result}")
        flagfIn = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
   
