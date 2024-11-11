def take_info():
    name_1 = input("Enter first name:\n")
    name_2 = input("Enter last name:\n")
    password = input("Enter password:\n")
    confirm_pass = input("Confirm password:\n")
    return name_1, name_2, password, confirm_pass


def login():
    n1, n2, p, cp = take_info()
    if p == cp:
        print("Welcome " + n1 + " " + n2)
    else:
        print("sorry!!! " + 'Invalid login credentials ' + n1 + ' ' + n2)


login()
