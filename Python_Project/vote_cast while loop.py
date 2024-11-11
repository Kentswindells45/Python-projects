candidate_sam = 0
candidate_ken = 0
candidate_vida = 0
rejected = 0
j = 1
while j <= 10:
    print("---VOTING PAGE-----")
    ballot = int(input('PRESS [1] to vote candidate-Sam\n PRESS [2] to vote candidate-ken \n PRESS [3] to vote '
                       'candidate-Vida '))
    if ballot == 1:
        candidate_sam += 1
    elif ballot == 2:
        candidate_ken += 1
    elif ballot == 3:
        candidate_vida += 1
    else:
        rejected += 1
    j += 1
if candidate_sam > candidate_ken and candidate_sam > candidate_vida:
    print('Sam obtained ' + str(candidate_sam) + ' vote cast')
    print('Ken obtained ' + str(candidate_ken) + ' vote cast')
    print('Vida obtained ' + str(candidate_vida) + ' vote cast')
    print('The rejected ballots are ' + str(rejected) + ' vote cast')
    print("Sam is the Winner!!!")
elif candidate_ken > candidate_sam and candidate_ken > candidate_vida:
    print('Sam obtained ' + str(candidate_sam) + ' vote cast')
    print('Ken obtained ' + str(candidate_ken) + ' vote cast')
    print('Vida obtained ' + str(candidate_vida) + ' vote cast')
    print('The rejected ballots are ' + str(rejected) + 'vote cast')
    print("Ken is the Winner!!!")
elif candidate_vida > candidate_ken and candidate_vida > candidate_sam:
    print('Sam obtained ' + str(candidate_sam) + ' vote cast')
    print('Ken obtained ' + str(candidate_ken) + ' vote cast')
    print('Vida obtained ' + str(candidate_vida) + ' vote cast')
    print('The rejected ballots are ' + str(rejected) + ' vote cast')
    print("Vida is the Winner!!!")
else:
    print('Sam obtained ' + str(candidate_sam) + 'vote cast')
    print('Ken obtained' + str(candidate_ken) + 'vote cast')
    print('Vida obtained' + str(candidate_vida) + 'vote cast')
    print('The rejected ballots are ' + str(rejected) + ' vote cast')
    print("Call for Run-Off")