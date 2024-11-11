class person:
    def take_data(self):
        name = input("Enter your name")
        age = int(input("Enter your age"))
        gender = input("Enter your gender")


# since the class "person" belongs to persons class,class Student will inherent the (person) class
# to avoid repetition of code, we use the same data to stand alone to be called by other users.
# for instance displaying name ,age etc

class student(person):
    def take_info(self):
        st = student()
        st.take_data()
        school = input("Enter your school")


s = student()
s.take_info()
