def collect_credentials():
    user_name = input('Enter your user name:\n')
    print(user_name)
    date_of_birth = input('Enter your date of birth:\n')
    print(date_of_birth)
    country = input("Enter your country of origin:\n")
    print(country)
    residence = input("Enter your residence:\n")
    print(residence)
    password = input("Enter your password:\n")
    confirm_password = input('Confirm password')
    return user_name, date_of_birth, country, residence, password, confirm_password


def check_credentials():
    un, dob, c, r, pw, cpw = collect_credentials()
    if pw == cpw:
        print("Login access granted " + un)
        print("Your details are as follows: " + dob + '' + c + '' + r)
        print("You are good to go")
    else:
        print("Invalid login credentials " + un)
        print("Try again")


check_credentials()
