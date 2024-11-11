class student:
    #    global fn, sn

    def take_data(self):
        fname = input("Enter first name:\n")
        sname = input("Enter second name:\n")
        return fname, sname

    def show_data(self):
        s = student()
        fn, sn = s.take_data()
        print(fn + " " + sn)


# use a variable to call the class from the function st = Student()
# where st becomes the variable to call the class and Student() belongs to the class
st = student()
# use a variable to call the class (s) Student() above and call the function show_data()
st.show_data()
