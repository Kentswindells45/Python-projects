# -*- encode: cp1252 -*-
print('------WELCOME TO UNIVERSAL BANKING APP-------')
client_name = ['Admin']
pin = ['1234']
deposit = 0
choice = int(input('Enter 1 if you have an account\n Enter 2 to create new account\n'))
if choice == 1:
    print('-------LOGIN PAGE--------')
    c_name = input('Enter Username:\n')
    c_pass = input('Enter Password:\n')
    for cn, cp in zip(client_name, pin):
        if c_name == cn and c_pass == cp:
            print("Login successful")
            option = int(input("Enter 1 to deposit an amount and check Balance\n Enter 2 to withdraw \n"))
            if option == 1:
                amount_deposit = float(input('Enter Amount You want to deposit\n'))
                new_amt = amount_deposit + deposit
                print(
                    f'An amount of {str(amount_deposit)} Cedis has been deposited to your account, and your account '
                    f'balance is ' + str(
                        new_amt) + ' Cedis')
            elif option == 2:
                withdraw_amount = int(input('Enter Amount you want to withdraw '))
                withdraw = deposit - withdraw_amount
                print('An amount of ' + str(withdraw_amount) + ' has been withdrawn successfully')
            else: 
                print('invalid Login credentials')
elif choice == 2:
    print('------REGISTRATION PAGE-------')
    client_name = str(input('Enter user name:\n'))

    pin = input("Enter your password:\n")
    print('------LOGIN PAGE-------')
    user_n = input("Enter your user name:\n")
    user_p = input("Enter your password:\n")

    for un, up in zip(user_p, user_n):
        if user_n == un and user_p == up:
            print('Log in successful')
            break
    else:
        print('invalid login credentials')
else:
    print('invalid option')
