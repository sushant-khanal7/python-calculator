def calculator():
    num1 = float(input("Enter your 1st Number: "))
    num2 = float(input("Enter your 2nd Number: "))
    operator = input("Enter the operator: ")
    
    if (operator == "+"):
        sum = num1 + num2
        print(f"Sum is: {sum}")
    elif (operator == "-"):
        difference = num1 - num2
        print(f"Difference is: {difference}")
    elif (operator == "*"):
        product = num1 * num2
        print(f"Product is: {product}")
    elif (operator == "/"):
        # Here the program will pass Error if user try to divide by 0
        if (num2 == 0):
            print("Error: You cannot divide by zero!")
        else:
            divide = num1 / num2
            print(f"Divide is: {divide}")
    else:
        print("Enter the correct operator")

calculator()
