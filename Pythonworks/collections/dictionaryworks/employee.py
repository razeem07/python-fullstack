# create dictionary employee with keys eid,name,salary,department,experience

employee={"eid":12,"name":"ram",
          "salary":25000,"department":"hr",
          "experience":6
          }

print(employee["salary"])

# add contact as 3456789
employee["contact"]=2345678
print(employee)

""" if experience > 5 update employee salary as current_salary+10000 
        else current_salary+5000
"""

if employee["experience"]>5:

    employee["salary"]+=10000

else:
    employee["salary"]+=5000

print(employee)


# add role as SDE if exp > 5 else add role as JDE
if employee["experience"]>5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"

print(employee)








