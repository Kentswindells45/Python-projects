# number1 = int(input('Enter a number: \n'))
# number2 = int(input('Enter another number: \n'))
# sum = number1 + number2
# avg = number1 + number2 // 2
# print('The sum is ' + str(sum))
# print('The avg is ' + str(avg))

# value = int(input('Enter a number \n'))
# if value % 2 == 0:
#    print('The number you entered is an Even number')
# else:
#    print('The number you entered is an odd number')

# Accept 3 numbers from a user and find the highest with all conditions.
num1 = int(input('Enter first number: \n'))
num2 = int(input('Enter second number: \n'))
num3 = int(input('Enter third number: \n'))

if num1 == num2 and num2 == num3:
    print('The numbers are equal')
elif num1 > num2 and num1 > num3:
    print('The highest number is ' + str(num1))
elif num2 > num1 and num2 > num3:
    print('The highest number is ' + str(num2))
elif num3 > num1 and num3 > num2:
    print('The highest number is ' + str(num3))
elif num1 == num2 and num2 > num3:
    print('The number ' + str(num1) + ' and ' + str(num2) + ' are the highest numbers')
elif num1 == num3 and num3 > num2:
    print('The number ' + str(num1) + ' and ' + str(num3) + ' are the highest numbers')
else:
    print('The number ' + str(num3) + ' and ' + str(num2))
