def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

operations = {"+":add, "-":subtract, "/":divide, "*":multiply}

def calculator():
    should_continue = True
    x = float(input("Enter first number: "))

    while should_continue:
        print("These are the available operations:")
        for key in operations.keys():
            print(f" -> {key}")
        operation = input("Enter desired operation: ")

        y = float(input("Enter second number: "))

        calculation_function = operations[operation]
        answer = calculation_function(x, y)
        print(f"{x} {operation} {y} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ") == "y":
            x = answer
        else:
            should_continue = False
            calculator()

calculator()