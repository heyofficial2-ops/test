def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract the second number from the first."""
    return a - b


def main():
    """Main function to test arithmetic operations."""
    # Example numbers
    num1 = 10
    num2 = 5
    
    # Call the functions and print the results
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    

# Call main function to run the program
if __name__ == "__main__":
    main()
