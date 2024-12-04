# dictionary methods
# employee id,name,department,age,salary


employee={"id":100,"name":"hari","department":"hr","age":32,"salary":25000}


# print(employee.get("department")) #get(key)
# invalid key return none

# pop(key) remove

employee.pop("salary")

print(employee)
 
# return all keys =>keys()

# for k in employee.keys():

#     print(k)

# fetch all values =>values()

for v in employee.values():

    print(v)

# get(key),pop(key),keys(),values(),
# fetch keyand values items()

for k,v in employee.items():

    print(k,v)