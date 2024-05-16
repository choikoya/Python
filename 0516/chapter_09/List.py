
class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, id, name, age, year, dept):
        super().__init__(id, name, age)
        self.year = year
        self.dept = dept 

class Dept:
    def __init__(self, dname):
        self.dname = dname

dname = ("java","python","html","js","react")

s1 = Student("s1","kim",10, 3, dname[0] )
s2 = Student("s2","Lee",12, 5, dname[1])
s3 = Student("s3","Park",9, 2, dname[2] )
s4 = Student("s4","Choi",11, 4, dname[3] )
s5 = Student("s5","Kang",8, 1, dname[4] )

p1 = Person("p1","kim",10)
p2 = Person("p2","Cho",11)
p3 = Person("p3","kim",12)
p4 = Person("p4","Park",9)
p5 = Person("p5","Lee",13)

Students = [s1, s2, s3, s4, s5]
Persons = [p1, p2, p3, p4, p5]
ps = [*Students, *Persons]

for px in ps:
    px. #호출에 따라 students persons 나오게




