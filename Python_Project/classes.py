class MyClass:
    def __init__(self):
        self.name = "Henry"

    pass


class MyClass:
    name = "Henry"
    age = 45
    scaffold = name + str(age)
    scaffold = MyClass()
    print(scaffold.name + str(age))
