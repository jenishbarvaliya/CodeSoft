def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Oops! That's not a valid number. Please try again.")

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed."
    else:
        return "Unknown operation. Please use +, -, *, or /."

def main():
    print("Welcome to the Simple Calculator.")

    num1 = get_number("Enter the 1st number: ")
    num2 = get_number("Enter the 2nd number: ")

    print("Choose your operation which you want to perform:")
    print(" + ")
    print(" - ")
    print(" * ")
    print(" / ")

    operation = input("Which operation would you like to perform? ").strip()

    result = calculate(num1, num2, operation)

    print(f"The result of {num1} {operation} {num2} is: {result}")

if __name__ == "__main__":
    main()
