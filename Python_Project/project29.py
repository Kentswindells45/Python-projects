username = ['Admin']
password = ['12345']
opt = int(input('Enter 1 if you have an account\n Enter 2 if you do not have an account\n'))
if opt == 1:
    print('-------LOGIN PAGE--------')
    uname = input('Enter your username ')
    upass = input('Enter your password ')
    for un, up in zip(username, password):
        if uname == un and upass == up:
            print('Log in Successful')
        else:
            print('invalid Login credentials')

elif opt == 2:
    print('------REGISTRATION PAGE-------')
    Username = input('Enter your user Name')
    username.append(Username)
    upass = input('Enter your password')
    password.append(upass)
    print("-----LOGIN PAGE-----")
    uname = input('Enter your username')
    upass = input('Enter your password')
    for un, up in zip(username, password):
        if uname == un and upass == up:
            print('Log in successful')
        else:
            print('invalid login credentials')
else:
  print('invalid option')
