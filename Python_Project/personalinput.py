weight = int(input('Weight:\n'))
unit = input('(l)bs or (K)g:\n')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f'You are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} pounds')
