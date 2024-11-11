class store_management:

    def product_details(self):
        print("""      -----Welcome To SuperMarket-------\n"
        ------------Below are the list of items available in the market------\n
         press[1] Sugar Gh 2.00\n
         press[2] Rice Gh 3.00\n
         press[3] Can Beef Gh 18.00\n
         press[4] Vegetable oil Gh 10.00\n
         press[5] Tomato paste Gh 12.00\n""")

    def customer_details(self):
        ss = store_management()
        ss.product_details()

        name = input("Enter Customer Name:\n")
        contact = input("Enter your phone:\n")
        opt = int(input("Enter product List you want to purchase:\n"))
        choice = input("Do you want to buy any other item? yes/no :\n")
        return name, contact, opt, choice

    def Product_conditions(self):
        mnt = store_management()
        nm, ct, op, ch = mnt.customer_details()

        ch = "yes"
        while ch.lower() == "yes":
            self.product_details()
            if op == 1:
                print("Your order item is " + str(op))
            else:
                print("Thank you for your purchase!! come back any time ")


pt = store_management()
pt.Product_conditions()
