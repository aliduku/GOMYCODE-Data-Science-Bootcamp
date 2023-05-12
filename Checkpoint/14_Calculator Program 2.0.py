import math

another = 'y'
def get_input(prompt, valid_inputs=None):
    while True:
        user_input = input(prompt)
        if valid_inputs is None:
            if user_input.isdigit():
                return float(user_input)
            print("Invalid input. Please enter a valid number.")
        elif user_input in valid_inputs:
            return user_input
        else:
            print("Invalid input. Please enter a valid input from the following options: " + ", ".join(valid_inputs))

class Calculator:
    def __init__(self):
        self.operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y
        }

    def add_operation(self, operation, function):
        self.operations[operation] = function

    def calculate(self, x, operation, y = None):
        return self.operations[operation](x, y)
        
calc = Calculator()
calc.add_operation("^", lambda x, y: x ** y)
calc.add_operation("sqrt", lambda x, y: math.sqrt(x))
calc.add_operation("log", lambda x, y: math.log(x))

while another in ['y', 'Y']:
    x = get_input("Enter the first number: ")
    y = get_input("Enter the second number: ")
    
    print("These are the available operations:")
    for key in calc.operations.keys():
        print(f" -> {key}")
    print("For single parameter operations, the first number will be used.")
    operation = get_input("Enter desired operation: ", calc.operations.keys())

    result = calc.calculate(x, operation, y)
    print(f"Result = {result}")
    
    another = input("Do you want to perform another calculation? (y/n): ")