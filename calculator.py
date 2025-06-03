#calculator.py

def add(x, y):
    """Adds two numbers and returns the result."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers and returns the difference."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers and returns the product."""
    return x * y

def divide(x, y):
    """Divides two numbers and returns the quotient. Handles division by zero."""
    if y == 0:
        return "Error: Division by zero is not allowed!"
    return x / y

def calculator ():
    """Runs a simple command_Line calculator allowing multiple operations until the user chooses to exit."""
    
    print("Welcome to the simple Python Calculator!")
    print("You can perform +, -, *, / operations.")
    print("Type 'exit' at any time to quit.")
    print("-" * 30)
    
    
    while True:
        num1_input = input("Enter first number (or 'exit'): ").lower()
        if num1_input == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        # Input validation for the first number
        try:
            num1 = float (num1_input)
        except ValueError:
            print("Invalid input for thr first number. Please enter a valid number")
            continue #Go back to the start of the loop
        
        num2_input = input ("Enter second number: ").lower()
        if num2_input == 'exit': #Allow exiting on second number too
            print("Exiting the calculator. Goodbye!")
            break
        
        # Input validation for the second number
        try:
            num2 = float(num2_input)
        except ValueError:
            print("Invalid input for the second number. Please enter a valid number")
            continue #Go back to the start of the loop

        operator = input("Enter an operator (+, -, *, /): ")
        
        result = None #Intialize result
        
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)

        else:
            print("Invalid operator. Please enter one of +, -, *, /.")
            # No need to set result, as it remains None or gets a string error from divide()
            
        # Display the result
        if result is not None and not isinstance(result, str): #Check if result is not None and not an error string
            print(f"Result: {result}")
        elif isinstance(result, str): # If result is an error message from divide()
            print(result)
            
        print("-" * 30) # Separator for better readability
        
# This ensures that calculator( is called only when the script executed directly
if __name__=="__main__":
    calculator()