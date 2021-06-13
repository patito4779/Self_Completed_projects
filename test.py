
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def printName(p):
        print("This is the way " + p.fname + str(p.age))

p1 = Person("Patrick", "Okwe", 34)
print(p1.printName())

class Student(Person):
    def __init__(self, fname, lname, age,  year):
        super().__init__(fname, lname, age)
        self.graduationYear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, " to the class of",
         self.graduationYear)

y = Student("Mike", "Ogbakpah", 45, 2019)

print(y.welcome())

        