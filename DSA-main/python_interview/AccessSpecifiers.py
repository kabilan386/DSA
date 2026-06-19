class Student:
    def __init__(self):
        # Public
        self.name = 'Kabilan'
        # Protected 
        self._age = 21
        # Private
        self.__marks = 95


obj = Student()

print(obj.name)
print(obj._age)
print(obj._Student__marks)