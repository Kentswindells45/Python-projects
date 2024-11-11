
j = 1
while j <= 7:
    score = int(input('Enter your Score:\n'))
    print(score)
    j += 1
    if score >= 50:
        print("Pass")
    elif score <= 50:
        print('fail')
