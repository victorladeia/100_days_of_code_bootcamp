def add( n1, n2 ):
    """Takes two numbers and returns the sum of them."""
    return n1 + n2

def subtract( n1, n2 ):
    """Returns the subtraction of two numbers."""
    return n1 - n2

def multiply( n1, n2 ):
    """Returns the product of two given numbers."""
    return n1 * n2

def divide( n1, n2 ):
    """Return the division of two given numbers."""
    return n1 / n2

operations ={
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():

    num1 = float( input( "What's the first number?: " ) )

    should_continue = True

    while should_continue:
        for operation in operations:
            print( operation )
        operation_symbol = input( "Pick an operation from the line above: " )
        num2 = float( input( "What's the next number?: ") )

        answer = operations[operation_symbol]( num1, num2 )

        print( f"{num1} {operation_symbol} {num2} = {answer}" )
        continue_calculation = input( f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: " )
        if continue_calculation == 'n':
            should_continue = False
            calculator()

        num1 = answer

calculator()