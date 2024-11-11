class Clerk_Check:

    def login_info(self):
        print("-----WELCOME TO LOGIN PAGE-----")
        user = input("Enter user name:\n")
        password = input("Enter your password:\n")
        confirm_password = input("Confirm password:\n")
        return user, password, confirm_password

    def info_process(self):
        c = Clerk_Check()
        u, p, cp = c.login_info()
        check = 0
        if p == cp:
            check = 1
            print("You're Welcome " + u + "you may proceed your work\n")
            print("Take cautions")
        else:
            check = 0
            print("Sorry!! " + u + "invalid password credentials")
            return check


pc = Clerk_Check()
pc.info_process()


class user_menu:

    def menu(self):
        menu = input("press [1] to check your payslip:\npress [2] to see ")
