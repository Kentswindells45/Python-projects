class school_system:

    def login(self):
        name = input("Enter student name:\n")
        pin = int(input("Enter your pin:\n"))
        confirm = int(input("Confirm pin:\n"))
        return name, pin, confirm

    @property
    def login_condition(self):
        ss = school_system()
        nm, pi, co = ss.login()

        if pi == co:
            print("------Welcome to Student Platform-------")
            print("This is your portal " + nm + " you may proceed...")
            sc1 = int(input("Enter your first score:\n"))
            sc2 = int(input("Enter your last score:\n"))
            sc3 = int(input("Enter your last score:\n"))
            su = sc1 + sc2 + sc3
            print("Your total score is  " + str(su) + nm + "  proceeding to check your Average score eligibility......")
            avg = sc1 + sc2 + sc3 / 3
            print("Your Average Score is " + str(avg))
            if avg == 160:
                print("You are eligible to proceed to the next sem" + nm + " Congrats!!!")
            else:
                print("Sorry you are not eligible to  proceed " + nm)
                print("Failed!!!")
            return sc1, sc2
        else:
            print(" Error404!!!! Sorry invalid login credentials!!! " + nm + " please do you want to try again? yes/no")
            choice = input("""
            Press[yes] to try again!!
            press[no] to end session
            """)

        toggle = "no"
        prompt = "yes"
        if prompt.lower() == "yes":
            while prompt.lower() == "yes":
                self.login_condition()
                # sc = school_system()
                # sc.login_condition()
                break


mk = school_system()
mk.login_condition
