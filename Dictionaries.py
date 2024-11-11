costumer = {
    "name": "John Smith",
    "age": 32,
    "phone": "03444",
    "is_verified":True
}
print(costumer["name"])
# You can use the (get) function to pass a value
# which is not in the dictionary
print(costumer.get("birth date","1 Jan 1996"))
print(costumer["phone"])
print(costumer["is_verified"])
