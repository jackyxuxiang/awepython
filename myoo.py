class Student(object):
    print('hello')
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.__score))

stu = Student('jacky',99)
stu.print_score()
stu.__score = 98
stu.print_score()