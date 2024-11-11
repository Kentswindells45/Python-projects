class student:
    #    global fn, sn

    # use a global variable to define first_name and second_name.
    def take_data(self):
        first_name = input("Enter first name:\n")
        second_name = input("Enter second name:\n")
        return first_name, second_name

    def show_data(self):
        s = student()
        fn, sn = s.take_data()
        print(fn + " " + sn)


class Teacher:
    def show_teacher(self):
        print("This is the teacher class")


# use a variable to call a function thus st to call the Student function and tc to call the teacher function
# use the variable . the function to call a function thus (st = Student() call the function from the Student class
# st.show_data)

st = student()
st.show_data()
tc = Teacher()
tc.show_teacher()
