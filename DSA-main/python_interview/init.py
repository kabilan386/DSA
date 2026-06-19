from datetime import date

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name,self.age)

    @classmethod
    def from_birth_year(cls,name,birth_year):
        return cls(name,date.today().year - birth_year)



ob1 = Student("Kabilan",21)
ob1.display()

ob2 = Student.from_birth_year("Kabilan",2005)
ob2.display()