# use an attributes of a costumer

# costumer = {
# "name": "Kevin Kent",
#  "age": "23",
#   "is_verified": True
# }
# costumer["birthdate"] = "1 jan 1999"
# print(costumer["birthdate"])

phone = input(" Enter Phone number:\n")
digits_mapping = {
    "0": "zero",
    "1": "one",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch) + " "
print(output)
