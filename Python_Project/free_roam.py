score = 0
option = "yes"
while option.lower() == "yes":
    sc = int(input("Enter your score:\n"))
    if score == 20:
        print("you pass")
    elif option.lower() != "yes":
        print("Sorry you failed")
        p = input("Is there any other student? yes/no")
