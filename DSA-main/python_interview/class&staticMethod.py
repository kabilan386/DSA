# Class and Static Method:
# Instance Method:
#  - Access instance variables
#  - Access class variables
#  - Access static variables
# Class Method:
#  - Access class variables
#  - Access static variables
# Static Method:
#  - Access static variables



class Student:
    school = "ABC School"

    # Instance Method
    def display(self,name,age):
        self.name = name
        self.age = age
        print(self.name,self.age,self.school)

    # Class Method
    @classmethod
    def getSchool(cls):
        print(cls.school)

    # Static Method
    @staticmethod
    def info():
        print("This is a static method" + Student.school)



s = Student()

# Instance Method
s.display("Kabilan",21)

# Class Method
Student.getSchool()

# Static Method
Student.info()