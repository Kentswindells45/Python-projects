class school:

    def Take_logins(self):
        name = input("Enter student name:\n")
        print("Enter your pin code\n  Pin must be at least 4 numbers")
        pin = int(input("Enter pin:\n"))
        confirm_pi = int(input("Confirm Pin:"))
        return name, pin, confirm_pi

    def Check_login(self):
        sc = school()
        nm, pi, con = sc.Take_logins()
        if pi == con:
            print("Welcome to the student portal " + nm)
            print("Proceeding to check your status......Loading........")
        else:
            print("Error 404!!!.......invalid login credentials ...")
            print("Please try again later...")
        return nm

    def Take_inputs(self):
        mk = school()
        nn = mk.Check_login()
        print("----Welcome to the Score inputs you may proceed to put your scores below----")
        score_1 = int(input("Enter your score on English:\n"))
        score_2 = int(input("Enter your score on Science:\n"))
        score_3 = int(input("Enter your score on Maths:\n"))
        score_4 = int(input("Enter your score on Social STDs:\n"))
        print("Dear " + nn + " Below are your scores for the following subjects:\n")
        print("English: " + str(score_1))
        print("Science: " + str(score_2))
        print("Maths: " + str(score_3))
        print("Social STDs: " + str(score_4))
        print("Proceeding to check your eligibility....")
        return score_1, score_2, score_3, score_4, nn

    def AVG_SUM(self):
        nk = school()
        sc1, sc2, sc3, sc4, n = nk.Take_inputs()
        sum = sc1 + sc2 + sc3 + sc4
        print("Dear " + n + " The sum of your results is: " + str(sum))
        print("Proceeding to check your Average score....")
        avg_score = sc1 + sc2 + sc3 + sc4 / 4
        print("Dear " + n + " your average score is: " + str(avg_score))
        if avg_score >= 200:
            print("Congrats!! " + n + " You passed...")
            print("Thank You")
        else:
            print("Sorry " + n + "you failed...try again ")
            print("You average score must be between 200 upwards")


kent = school()
kent.AVG_SUM()
