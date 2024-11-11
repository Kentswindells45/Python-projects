# a list containing duplicate names

names = ["Kelvin", "Penny", "Ricky", "Ricky", "Penny", "Kelvin", "Samuel", "Samuel"]

# an empty list which will contain the duplicates from the original list
real_names = []
for name in names:
    if name not in real_names:
        real_names.append(name)
print(real_names)
