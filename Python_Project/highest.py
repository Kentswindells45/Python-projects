num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
num3 = int(input("Enter the third number "))

if num1 == num2 and num2 == num3:
    print("Equal ")
elif num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
elif num3 > num1 and num3 > num2:
    print(num3)
elif num1 == num2 and num2 > num3:
    print(num1, num2)
elif num1 == num3 and num1 > num2:
    print(num1, num3)
else:
    print(num3, num2)

