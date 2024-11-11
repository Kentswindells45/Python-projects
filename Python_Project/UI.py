class pools:

    def Bank_Checkins(self):
        print("-----Welcome To Universal Banking------\n")
        msg = int(input("Do you have an account?\n"
                        "Press[1] to login\n"
                        "Press[2] to register\n"))
        if msg == 1:
            print("----Welcome To Universal Banking Login Page-----\n")
            name = input("Enter Name:\n")
            pin = int(input("Enter your Pin:\n"))
            if name.upper() == "Admin" and pin == 1234:
                print("Login Successful!")
        else:
            print("Invalid Login Credentials!!!!")
            return msg

    def Option2(self):
        bank = pools()
        msg, name = bank.Bank_Checkins()
        if msg == 2:
            print("----Welcome to universal Banking Page-----\n")
            print("Please Fill the Form Below To Register an Account\n")
            name = input("Enter your name\n")
            gender = input("Enter your Gender\n")
            pin = int(input("Enter your pin\n"))
            config = int(input("Confirm Pin\n"))
            if name.upper() == "Admin" and pin == config:
                print("Welcome " + name + " !!to universal Banking System your account has been created successfully\n")
            else:
                print("Sorry your account could not be created dues to invalid inputs "
                      "please fill out the required form correctly...")


bb = pools()
bb.Option2()
