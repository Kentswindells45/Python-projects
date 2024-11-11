class parents:

    def take_parents_info(self):
        p_name = input("Enter your parent name:\n")
        p_add = input("Enter parent's address:\n")
        return p_name, p_add

    def display_parents_info(self):
        p = parents()
        n, dd = p.take_parents_info()
        print(n + " " + dd)


pa = parents()
pa.display_parents_info()


class student:

    def learner_info(self) -> object:
        print("-------STUDENT LOGIN INFO--------")
        name = input("Enter Student name:\n")
        pin = int(input("Enter Student pin code:\n"))
        c_pin = int(input("Confirm pin code"))
        return name, pin, c_pin

    def check_pin(self) -> object:
        c = student()
        n, p, cp = c.check_pin()
        if p == cp:
            print("WELCOME " + n)
        else:
            print("Oops!!! invalid pin code")
            breakpoint()

        first_sem = int(input("Enter your first semester score:\n "))
        second_sem = int(input("Enter your second semester score:\n"))
        return first_sem, second_sem

    def display_learner_info(self):
        l = student()
        n, a, f, sm, = l.learner_info()
        avg = (f + sm) // 2
        print(n + " is " + str(a) + " years " + "and your average semester score is " + str(avg))
        if avg >= 400:
            print("Congrats!! " + n + "You qualify to the next semester good luck!!")
        else:
            print("Sorry!!! " + n + " resit awaits you in no time buck up!!!")


#pt = Student()
#pt.check_pin()
s = student()
s.display_learner_info()
