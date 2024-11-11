class Window:
    def display(self):
        costumer_name = input("Enter Costumer Name:\n")
        costumer_details = input("Enter Costumer details:\n")
        quantity = int(input("Enter Quantity of products purchase:\n"))
        return costumer_name, costumer_details, quantity

    def Check(self):
        w = Window()
        cn, cd, q = w.display()

        if cn == "Kevin" or cn == "kevin":
            print("you Qualify to shop here")
        else:
            print("Sorry you can't be recognized by the system")
        if cd != q:
            print("Allow costumer to roam freely in the shop")
        else:
            print("Secure shop system ")


wt = Window()
wt.Check()
