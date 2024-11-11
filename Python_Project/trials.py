class Apollo:
    def takeInfo(self):
        name = input("Enter Astronaut's name:\n")
        IC_code = int(input("Enter code hint: code shouldn't be less than 12 digits\n"))
        confirm_IC_code = int(input("Confirm code:\n"))

        return name, IC_code, confirm_IC_code

    def validatInfo(self):
        A = Apollo()
        na, IC, co = A.takeInfo()
        if IC == co:
            print("Initiate Personnel database.......")
            print("loading.......")
        else:
            print("Personnel info Error!!!")


App = Apollo()
App.validatInfo()
