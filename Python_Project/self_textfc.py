class StudentInfo:

    def Take_student_info(self):
        print("------WELCOME TO STUDENT PORTAL-----")
        name = input("Enter your name:\n")
        batch = input("Enter your Batch code number:\n")
        gender = input("Enter your gender:\n")
        age = int(input("Enter your age:\n"))
        course = input("Enter your course:\n")
        return name, batch, gender, age, course

    def CheckInfo(self):
        # global first_scr, sec_score
        s = StudentInfo()
        name, batch, gender, age, course = s.Take_student_info()
        if age >= 18:
            print("Welcome " + name)
        else:
            print("Sorry you don't meet the age requirement for the student portal")
        first_scr = int(input("Enter your first score:\n"))
        sec_score = int(input("Enter your second score:\n"))
        return first_scr, sec_score, name

    def Check_Avg(self):
        s = StudentInfo()
        first_scr, sec_score, name = s.CheckInfo()
        avg = first_scr + sec_score // 2
        if avg >= 100:
            print("Congrats!! " + name + " You qualify to the next level of your studies!! "
                                         "Thanking You in Anticipation....\n")

            print("KENT INC. 2021 alright received... ")
        else:
            print("Sorry " + name + "You failed due to your average score \n"
                                    "Hint your average must be 400 marks upwards\n")

            print("KENT INC. 2021 alright received ")


ex = StudentInfo()
ex.Check_Avg()
