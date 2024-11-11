class general:
    def ask_general_question(self):
        qt1 = input(
            "1. What does the term ROM stands for?\nA. Read on memory\nB. Random only memory\nC. Read only memory\n")
        qt2 = input("2.Which of the following is a storage device?\nA. Mouse\nB. Keyboard\nC.Pen drive\n")
        qt3 = input("3. Which of the following is a peripheral device?\nA. Joy stick\nB. Floppy Disk \nC.Keyboard\n")
        return qt1, qt2, qt3

    def mark_gen_question(self):
        g = general()
        q1, q2, q3 = g.ask_general_question()
        score = 0
        if q1 == "C" or q1 == "c":
            score += 5
        else:
            score += 0
        if q2 == "C" or q2 == "c":
            score += 5
        else:
            score += 0
        if q3 == "A" or q3 == "a":
            score += 5
        else:
            score += 0
        return score


# inheritance from the Class general
class python_programming(general):
    def start_python_test(self):
        pp = python_programming()
        sc = pp.mark_gen_question()
        qt4 = input("4. Who invented Python Programming?\n A.James Gosling\n B.Guido Van Rossum\nC.Dominic\n")
        qt5 = input("Python can be use for Web development?\nA.True\nB.False\nC.None\n")
        if qt4 == "B" or "b":
            sc += 5
        else:
            sc += 0
        if qt5 == "A" or "a":
            sc += 5
        else:
            sc += 0
        print("Your total score is " + str(sc))


class Database(general):
    def database_test(self):
        pp = python_programming()
        sc = pp.mark_gen_question()
        qt4 = input(
            "4. What does RDMS stands for?\nA.Relational Database Management system\nB.Relational db "
            "msys\nC.Relational management system\n")
        qt5 = input("5. What does DBMS stands for?\nA.Database Management System\nB.Relational Database"
                    "Management System\nC.Documented Database Management System")

        if qt4 == "A" or "a":
            sc += 5
        else:
            sc += 0
        if qt5 == "A" or "a":
            sc += 5
        else:
            sc += 0

        print("Your total score is " + str(sc))


course = int(input("-----Menu----\npress 1. for python programming\n press 2. for Database test\n"))
if course == 1:
    py = python_programming()
    py.start_python_test()
elif course == 2:
    db = Database()
    db.database_test()
else:
    print("Invalid Course")
