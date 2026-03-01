import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        return None, None


def main():
    while True:
        print("\n====== Python Calculator ======")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Exiting calculator... 👋")
            sys.exit()

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please select a valid option.")
            continue

        num1, num2 = get_numbers()
        if num1 is None:
            continue

        try:
            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)

            print(f"Result: {result}")

        except ZeroDivisionError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
