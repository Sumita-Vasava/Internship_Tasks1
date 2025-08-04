#Elevate Lab Internship
#Task1 : Building a Calculator CLI App
#Date: 4 Aug 2025
#Objective : Creating a command line calculator supporting basic operations
#======================================================================================
#creating function for each operations (+,-,*,/)
def add(a,b):
    return a+b
def subt(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "number cannot be divided by zero"
    return a/b

# creating a main loop for user input
def calculator():
    print("Welcome to the Command-Line Calculator")
    print("Available operations to use : +  -  *  /")
    print("Type 'exit' to quit the calculator.\n")

    while True:
        # We will take first number here
        num1_input = input("Enter the first number: ")
        if num1_input.lower() == 'exit':
            print("Thank you for using the calculator!")
            break
        try:
            num1 = float(num1_input)
        except ValueError:
            print(" Please enter a valid number.")
            continue

        # We will Take operation from user
        operator = input("Enter operator (+, -, *, /): ")
        if operator.lower() == 'exit':
            print("Thank you for using the calculator!")
            break
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator! Please choose from +, -, *, /")
            continue

        # We will take the second number from user
        num2_input = input("Enter the second number: ")
        if num2_input.lower() == 'exit':
            print("Thank you for using the calculator!")
            break
        try:
            num2 = float(num2_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Now we will calculate the result
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subt(num1, num2)
        elif operator == '*':
            result = multi(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)

        print(f"Result: {num1} {operator} {num2} = {result}\n")

# we will Run the calculator
if __name__ == "__main__":
    calculator()

