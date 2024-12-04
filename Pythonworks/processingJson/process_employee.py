
from json import load

f=open("C:\\Users\\Luminar\\Desktop\\Pythonworks\\datasets\\employee.json")

data=load(f)

for emp in data:

    print(emp)


