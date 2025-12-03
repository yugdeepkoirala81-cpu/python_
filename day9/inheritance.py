# class Parent:
#     hair= "curly"

# class Child(Parent):
#     pass

# child1=Child()
# print(child1.hair)

#----------------------------#

class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    
    def introduce(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll
    def student_info(self):
        print (f" I am {self.name} and I am {self.age}years old. MY roll is {self.roll}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject= subject
    def teach(self):
        print(f"I am {self.name}, of {self.age} and teach {self.subject} ")

individual= Person("Shristab","18")
teach=Teacher("Sks","55","organic and dadagiri")
std=Student("Yugdeep","17","877")

teach.teach()
individual.introduce()
std.student_info()