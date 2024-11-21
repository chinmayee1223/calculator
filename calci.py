def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    # Prompt the user to input the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user to input the second number
    num2 = float(input("Enter the second number: "))
    
    # Display the operations menu
    print("Choose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    # Prompt the user to choose an operation
    choice = input("Enter the operation (1/2/3/4): ")
    
    # Perform the calculation based on the user's choice
    if choice == '1':
        result = add(num1, num2)
        operation = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "*"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "/"
    else:
        result = "Invalid choice"
        operation = ""
    
    # Display the result
    if result != "Invalid choice":
        print(f"The result of {num1} {operation} {num2} is: {result}")
    else:
        print(result)

# Run the main function to start the calculator program
if __name__ == "__main__":
    main()
