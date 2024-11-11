class InputNumber:
    def Take_number(self):
        f_num = int(input("Enter first number:\n"))
        s_num = int(input("Enter another number:\n"))
        l_num = int(input("Enter last number:\n"))
        return f_num, s_num, l_num

    def check_condition(self):
        pp = InputNumber()
        f, l, s = pp.Take_number()

        if s >= s and f >= l:
            print('The highest number is ' + str(f))
        elif s > f and s >= l:
            print('The highest number is ' + str(s))
        elif l >= f and l > s:
            print('The highest number is ' + str(l))
        else:
            print('The numbers are equal')


j = InputNumber()
j.check_condition()
