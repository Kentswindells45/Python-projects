def get_data():
    name = input('what is your Name?\n')
    age = int(input("how old are you?\n"))
    return name, age


def check_age():
    # The returned values in get_data function is used to accept the check_age condition
    my_name, my_age = get_data()
    if my_age >= 18:
        print("congrats!! " + my_name + ' you can vote')
    else:
        print('sorry!! ' + my_name + ' you cannot vote')


check_age()
