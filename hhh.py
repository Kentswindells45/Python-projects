class general:
    def ask_general_question(self):
        qt1 = input(
            "1. What does the term ROM stands for?\nA. Read on memory\nB. Random only memory\nC. Read only memory\n")
        qt2 = input("2.Which of the following is a storage device?\nA. Mouse\nB. Keyboard\nC.Pen drive\n")
        qt3 = input("3. Which of the following is a peripheral device?\nA. Joy stick\nB. Floppy Disk \nC.Keyboard\n")
        return qt1, qt2, qt3

    def mark_gen_question(self):
        g = general()
        qt1, qt2, qt3 = g.ask_general_question()
        score = 0
        if qt1 == "C" or qt1 == "c":
            score += 5
        else:
            score += 0
        if qt2 == "C" or qt2 == "c":
            score += 5
        else:
            score += 0
        if qt3 == "A" or qt3 == "a":
            score += 5
        else:
            score += 0
        return score

