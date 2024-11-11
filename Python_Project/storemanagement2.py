class store_management:

    def Products_client_details(self):
        print("---Welcome to Supermarket------\n")
        print("""
        ------------Below are the list of items available in the market------\n
        Sugar Gh 2.00\n
        Rice Gh 3.00\n
        Can Beef Gh 18.00\n
        Vegetable oil Gh 10.00\n
        Tomato paste Gh 12.00\n""")

        name = input("Enter your name:\n")
        contact = int(input("Enter your phone:\n"))
        add = input("Enter your address:\n")
        prod = input("Enter product name:\n")
        amt = float(input("Enter amount of product item:\n"))
        return name, contact, add, prod, amt

    def product_Condition(self):
        ss = store_management()
        nm, cn, ad, prd, amt = ss.Products_client_details()

        if prd.lower() == "sugar" and amt == 2.00:
            print(
                "Dear " + nm + " your item\n " + prd + " has been successfully purchased!! with an amount of GH " + str(
                    amt))
        elif prd.lower == "rice " and amt == 3.00:
            print(
                "Dear " + nm + " your item\n " + prd + " has been successfully purchased!! with an amount of GH " + str(
                    amt))
        elif prd.lower() == "Beef" and amt == 18.00:
            print(
                "Dear " + nm + " your item\n " + prd + " has been successfully purchased!! with an amount of GH " + str(
                    amt))
        elif prd.lower() == "vegetable oil" and amt == 10.00:
            print(
                "Dear " + nm + " your item\n " + prd + " has been successfully purchased!! with an amount of GH " + str(
                    amt))
        elif prd.lower() == "Tomato paste" and amt == 12.00:
            print(
                "Dear " + nm + " your item\n " + prd + " has been successfully purchased!! with an amount of GH " + str(
                    amt))
        else:
            print("""
            ERROR 404!!!!
            Invalid input or item does not exist
            if problem persist check your item details and try again
            """)
        ent = input("Do you want to buy any new item? yes/no:\n")
        return ent

    def Processing(self):
        ph = store_management()
        prompt = ph.product_Condition()

        while prompt.lower() == "yes":
            self.product_Condition()


pp = store_management()
pp.Processing()
