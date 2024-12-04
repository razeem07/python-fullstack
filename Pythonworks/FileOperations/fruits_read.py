

f=open("C:\\Users\\Luminar\\Desktop\\Pythonworks\\datasets\\fruits.txt","r")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)