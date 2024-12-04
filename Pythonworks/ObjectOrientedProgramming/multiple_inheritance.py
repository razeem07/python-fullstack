class Person:

    name:str

    age:int

    def __init__(self,age,name):

        self.name=name

        self.age=age

    def display_person_info(self):

        print(self.name,self.age)


class Employee:

    eid:int

    salary:int

    def __init__(self,eid,salay):

        self.eid=eid

        self.salary=salay

    def display_employee_info(self):

        print(self.eid,self.salary)
    


class Manger(Person,Employee):


    department:str

    def __init__(self, age,name,eid,salary,department):

       
       Person.__init__(self,age,name)

       Employee.__init__(self,eid,salary)

       self.department=department

    def dispaly_manager_info(self):

      self.display_person_info()

      self.display_employee_info()
      print(self.department)



manage_instance=Manger(32,"hari","eo1",54000,"hr")

manage_instance.dispaly_manager_info()



# 