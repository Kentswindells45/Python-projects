class Student:

    def take_info(self):
        name = input("Enter Student name:\n")
        pin = int(input("Enter your pin, your pin must be at least 5 numbers:\n"))
        c_pin = int(input("Confirm pin code:\n"))
        return name, pin, c_pin


    def check_info(self):
        first_sem = 0
        second_sem = 0
        check = 0
        s = Student()
        n, p, cp = s.take_info()
        if p == cp:
            check = 1
            print("Welcome to the Student page " + n + "!!!")
            first_sem = int(input("Enter your first semester score:\n"))
            second_sem = int(input("Enter your second semester score:\n"))

        else:
            check = 0
            print("Sorry!!! " + n + " invalid pin code credential")
            # return check
        return first_sem, second_sem, check

    def student_average(self):
        s2 = Student()
        fs, ss, ch = s2.check_info

        if ch == 1:
            avg = (fs + ss) // 2

            if avg >= 240:
                print("Congrats your average score is " + str(avg) + " you can proceed to the next semester")
                print("Thank you!!!!!")
            else:
                print("Sorry your average score is low with the mark: " + str(avg) + " resit awaits you!!!")


st = Student()
st.student_average()
