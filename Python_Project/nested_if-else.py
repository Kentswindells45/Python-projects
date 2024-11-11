exam1 = float(input('Enter your first score '))
if exam1 >= 50:
    exam2 = float(input('Enter your second score '))
    if exam2 >= 50:
        avg = (exam1 + exam2) / 2
        if avg >= 80:
            print('Congrats!!, You Passed')
        else:
            print('Oops!!, Your average is too low')
    else:
        print('Sorry!!, You Failed test 2 ')
else:
    print('sorry!!, You Failed test 1')
