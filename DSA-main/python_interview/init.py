class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name,self.age)



ob1 = Student("Kabilan",21)
ob1.display()