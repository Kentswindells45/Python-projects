# procedures to collect scores and find the avg
def TakeData():
    score1 = int(input('Enter score1: '))
    score2 = int(input('Enter score2: '))
    return score1, score2


def find_average():
    s1, s2 = TakeData()
    avg = (s1 + s2) // 2
    print("Your average score is " + str(avg))


find_average()
