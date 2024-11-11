def findproduct(num1, num2):
    multi = num1 * num2
    print('The product is ' + str(multi))


# You can take the user inputs outside the function as below (n1,n2)
n1 = int(input('Enter a number:\n'))
n2 = int(input('Enter another number:\n'))
findproduct(n1, n2)
