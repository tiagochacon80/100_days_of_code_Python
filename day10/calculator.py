from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():

    num1 = float(input("What's the first number: "))
    for symbols in operations:
        print(symbols)

    should_continue = True
    while should_continue:
        operation_symbols = input("Pick the operation: ")
        num2 = float(input("What's the next number: "))
        function_operation = operations[operation_symbols]
        answer = function_operation(num1, num2)
        print(f"{num1} {operation_symbols} {num2} = {answer}")

        if print(f"Type 'y' for continue calculating with {answer}, or 'n' to restart. ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()








