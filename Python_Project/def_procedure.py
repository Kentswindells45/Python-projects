def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select an Operation:\n")
print("Press [1] to ADD\n")
print("Press [2] to SUBTRACT\n")
print("Press [3] to MULTIPLY\n")
print("Press [4] to DIVIDE\n")

while True:
    choice = input("Enter your Option[1,2,3,4]\n")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter First number:\n"))
        num2 = float(input("Enter Second number:\n"))
        if choice == 1:
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == 2:
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == 3:
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == 4:
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid Option!!!")
