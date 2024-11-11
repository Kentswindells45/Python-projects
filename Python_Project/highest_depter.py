def check_debtors():
    name = input('Enter Student name:\n')
    amount = int(input('Enter the amount remaining \n'))
    return name, amount


ch = 'Y'
h_amount = 0
name_stud = ''
while ch == 'y' or ch == 'Y':
    st_name, st_amount = check_debtors()

    if st_amount > h_amount:
        h_amount = st_amount
        name_stud = st_name

    ch = input('Is there any Student? (Y/N) ')
print('Student Name : ' + name_stud)
print("Amount pending : " + str(h_amount))
