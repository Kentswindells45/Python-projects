def add():
    x = input('Enter x: ')
    y = input('Enter y: ')
    sum = int(x) + int(y)
    print(f'The sum total of {x} and {y}is {sum}')


def sub():
    x = input('Enter x: ')
    y = input('Enter y: ')
    if x > y:
        sub=x-y
        print(f'The subtraction of {y} from {x} is {sub}')
    elif y > x:
        sub = y - x
        print(f'THe subtraction of{x} from {y} is {sub}')
    else:
        sub = 0
        print(f'The subtraction of{x}from{y}is {sub}')

def multi():
    x = input('Enter x: ')
    y = input('Enter y: ')
    multi =int(x)*int(y)
    print(f'The product of {x}and{y}is {multi}')
