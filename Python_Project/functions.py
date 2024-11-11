def addvalues():
    name = input("What is your name?\n")
    return name
def agevalues():
    age = int(input("Enter your Age\n"))
    return age
# when calling a function we call it with a variable thus (my_name) below
my_name = addvalues()
print("Your name is " + my_name)
my_age = agevalues()
print("Your age is " + str(my_age))
