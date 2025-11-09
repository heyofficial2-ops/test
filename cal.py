def add(a, b):
    return a + b

def subtract(a, b):
<<<<<<< HEAD:cal.py
    """Subtract the second number from the first."""
    return a - b
=======
    return a - b
    
#def multiply(a, b):
 #   return a * b
>>>>>>> 611e1c952eaa01fa0e08da35698686083e83523d:sample.py

#def divide(a, b):
 #   if b == 0:
  #      return "Error: Cannot divide by 0"
   # return a / b

def main():
    num1 = 10
    num2 = 5
    
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
<<<<<<< HEAD:cal.py
    # # print(f"{num1} * {num2} = {multiply(num1, num2)}")
    # print(f"{num1} / {num2} = {divide(num1, num2)}")
=======
    #print(f"{num1} * {num2} = {multiply(num1, num2)}")
    #print(f"{num1} / {num2} = {divide(num1, num2)}")
>>>>>>> 611e1c952eaa01fa0e08da35698686083e83523d:sample.py
    
    #Test divide by zero
   # num2 = 0
    #print(f"{num1} / {num2} = {divide(num1, num2)}")

# Call main function to run the program
if __name__ == "__main__":
    main()
