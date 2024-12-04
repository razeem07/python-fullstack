
f1=open("C:\\Users\\Luminar\\Desktop\\Pythonworks\\datasets\\all_students.txt")
f2=open("C:\\Users\\Luminar\\Desktop\\Pythonworks\\datasets\\failed.txt")

all_students_set=set()

failed_students_set=set()

for line in f1:

    line=line.rstrip("\n")

    all_students_set.add(line)

for line in f2:

    line=line.rstrip("\n")

    failed_students_set.add(line)

passed_students=all_students_set.difference(failed_students_set)

print(passed_students)

f1.close()
f2.close()