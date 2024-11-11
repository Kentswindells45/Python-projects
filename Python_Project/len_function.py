name = input('Enter your name\n')

if len(name) < 3:
    print("Name must be at least three characters")
elif len(name) > 10:
    print('Name must be at least ten characters')
else:
    print(name + " name looks good!!!")
