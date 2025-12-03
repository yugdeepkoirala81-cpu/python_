#object oriented programming

# class ClassName:   ( class name starts with capital letter)
#     statements(attributes, methods)

#-------------------------------------------------------------#

#creating a class

class Student:

    #if any function is defined inside a class then the function is called method
    def __init__(self,name,roll,address):    #def _init_ is used to define constructor function which is requied to automatically call the class
        self.name= name
        self.roll= roll
        self.address= address
        print(self)

    def student_info(self):
            print(f"Name: {self.name} | Roll: {self.roll} | Address: {self.address}")
s1=Student("yugdeep","877","brt")

# s1.student_info()
print(s1.name, s1.address, s1.roll)
print (s1)
# s2=Student()
# s3=Student()
# s4=Student()
