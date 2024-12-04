from re import fullmatch

date=input("enter date")

pattern="(0?[1-9]|1[0-2])"

matcher=fullmatch(pattern,date)

if matcher==None:

    print("invalid")
else:
    print("valid")

# date 01,1,31