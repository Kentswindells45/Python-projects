has_good_income = True
has_high_income = False
if has_good_income and has_high_income:
    print("Eligible for loan")
else:
    print("High income is required for loan ")
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")

approval_is_required = True
name = input('Enter your name \n')
favorite_color = input('Enter your favorite color \n')
if approval_is_required:
    print(name + " likes " + favorite_color)
else:
    print("Sorry invalid input ")
