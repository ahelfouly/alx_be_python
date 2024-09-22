number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"The result is {number1 + number2}.")
    case "-":
        print(f"The result is {number1 - number2}.")
    case "*":
        print(f"The result is {number1 * number2}.")
    case "/":
        if number2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {number1 / number2}.")
