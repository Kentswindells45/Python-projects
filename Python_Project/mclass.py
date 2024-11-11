# procedures to collect scores and find the avg
def TakeData():
    score1 = int(input('Enter score1 '))
    score2 = int(input('Enter score2 '))
    return score1, score2


def FindAverage():
    s1, s2 = TakeData()
    avg = (s1 + s2) // 2
    print('The average score is ' + str(avg))
    if avg >= 80:
        print("Your average score is " + str(avg))
        print("congrats!! you pass")
    else:
        print("Sorry!!! you need a resist due to this average score " + str(avg))
        print("your score should exceed 80")


# main program
FindAverage()
