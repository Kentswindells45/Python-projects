# Accept 20 scores from a Student and calculate the total score and find the average and loop 10 times
score = 0
total_score = 0
i = 1
while i <= 10:
    exam_score = int(input('Enter your score: \n'))
    if exam_score >= 1:
        score = total_score / 20
        print(total_score)
        print(score)
    else:
        total_score += score
        i += 1
