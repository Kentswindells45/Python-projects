score = 0
option = "yes"
while option.lower() == "yes":
    sc = int(input("Enter your score:\n"))
    if score <= 20:
        print("you pass")
        if option.lower() == "yes":
            p = input("Is there  any other student? yes/no ")
    else:
        print("Sorry you failed")
