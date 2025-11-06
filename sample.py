def add(a, b):
    """Add two numbers."""
    return a + b

 def subtract(a, b):
     """Subtract the second number from the first."""
     return a - b

# def multiply(a, b):
#     """Multiply two numbers."""
#     return a * b

# def divide(a, b):
#     """Divide the first number by the second with a check for division by zero."""
#     if b == 0:
#         return "Error: Cannot divide by 0"
#     return a / b

def main():
    """Main function to test arithmetic operations."""
    # Example numbers
    num1 = 10
    num2 = 5
    
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    # # print(f"{num1} * {num2} = {multiply(num1, num2)}")
    # print(f"{num1} / {num2} = {divide(num1, num2)}")
    
    # # Test divide by zero
    # num2 = 0
    # print(f"{num1} / {num2} = {divide(num1, num2)}")

# Call main function to run the program
if __name__ == "__main__":
    main()
