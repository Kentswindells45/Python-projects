def findgreatest():
    # the arguments in the parameters are used to take two inputs before it gets execute
    num1 = int(input("Enter a number:\n"))
    num2 = int(input("Enter another number:\n"))
    if num1 > num2:
        print(str(num1) + ' is the highest')
    elif num2 > num1:
        print(str(num2) + " is the highest")
    else:
        print(str(num1) + ' and ' + str(num2) + 'are equal')


findgreatest()
