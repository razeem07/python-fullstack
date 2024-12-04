# Movie
# title,rating,run_time,director,genre

# ARM
# KGF

class Faculty:

    id:int

    name:str

    age:int

    course:str

    experience:int

    salary:int

    def set_faculty(self,id,name,age,course,experience,salary):

        self.id=id

        self.age=age

        self.name=name

        self.course=course

        self.experience=experience
        
        self.salary=salary

    def display_faculty(self):

        print(self.name,self.age,self.course)

# refernce_name=ClassName()

faculty_instance1=Faculty()

faculty_instance2=Faculty()

faculty_instance2.set_faculty(100,"sabir",27,"bigdata",4,75000)

faculty_instance2.display_faculty()

