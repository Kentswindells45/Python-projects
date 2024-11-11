has_good_income = True
has_good_credit = False

if has_good_income or has_good_credit:
    print('Eligible for loan ')
else:
    print('High income and credit is required for loan ')

Female_Discount = 10
Male_Discount = 5
Female_Amount = 500
print(input('Enter Female Amount '))

if Female_Amount >= Female_Discount >= Female_Amount:
    print('10 percent discount is obtained')
else:
    Male_Amount = 500
    print(input('Enter Male Amount '))
    if Male_Discount <= Male_Amount and Male_Amount > Male_Discount:
        print('5 percent discount is obtained')
    else:
        print("Sorry you don't qualify for the discount")
