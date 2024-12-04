
# initialize attributes (instance variables)
# constructor

# initializing instance variables  constructor
# java(classname)


class Student:

    name:str

    rolnumber:int

    age:int

    course:str

    # initializing attributes of Student class 
    def __init__(self,name,rolnumber,age,course):

        self.name=name

        self.rolnumber=rolnumber

        self.age=age

        self.course=course

    def display(self):

        print(self.name,self.age,self.rolnumber,self.course)

# refence_name=ClassName()

student_instance1=Student("vyshnav",100,35,"django")





student_instance1.display()
    

