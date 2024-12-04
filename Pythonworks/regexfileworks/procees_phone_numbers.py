
from re import fullmatch

f=open("C:\\Users\\Luminar\\Desktop\\Pythonworks\\regexfileworks\\phone_numbers.txt")


for line in f:#line=9876543210\n

    phone=line.rstrip("\n")

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    if matcher !=None:

        print(phone)



