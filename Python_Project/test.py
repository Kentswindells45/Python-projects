msg = 'My very first day at school was awesome'
log = 'The logic behind my life is a coder'
display = f' {msg} [{log}] was my favorite thing to do in the first place '
# formatted string used to emphasized on a specific word to be highlighted.
print(msg.upper())
print(display)
print(msg.replace('awesome', 'absolutely awesome'))

birth_year = input('Enter your birth year: ')
age = 2021 - int(birth_year)
print(age)
