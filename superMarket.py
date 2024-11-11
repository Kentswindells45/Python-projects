print("""WELCOME DEAR VALUED COSTUMER,
This Super market is giving discounts to it's regular costumers on fridays.
 The TERMS and CONDITIONS are as follows...
 Any costumer who make purchases around GH500.00 will be given a discount
 depending on your gender.
  Males obtain a discount of 5 percent while females obtain a discount of 10 percent..
  Proceed the following to check your eligibility.
  Thank You Most Valued Costumer..... \n""")


class SuperMarket:

    def CheckDay(self):
        global day
        day = input("Enter the day:\n")
        if day == "Friday" or day == "friday":
            print("-----Welcome Costumer today is friday you may proceed:")
        else:
            print("Sorry you don't qualify the discount due to the day try again:")
            return day

    def Gender(self):
        c = SuperMarket()
        c.CheckDay()

        gender = input("Enter your gender:\n")
        if gender == "Male" or gender == "male":

            amount = float(input("Enter amount of items purchased:\n"))
            if amount == 500.00 and day == "Friday" or day == "friday":
                print("Congrats!!!!! you qualify for a discount of 5 percent")
        elif gender == "Female" or gender == "female":

            amount = float(input("Enter amount of items purchased:\n"))
            if amount == 500.00 and day == "Friday" or day == "friday":
                print("Congrats!!!!! you qualify for a discount of 10 percent")
        else:
            print("Sorry your day doesn't match with the amount of items purchased")


ss = SuperMarket()
ss.Gender()
