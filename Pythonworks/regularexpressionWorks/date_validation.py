

from re import fullmatch


pattern="(0?[1-9]|[12][0-9]|3[01])"


date=input("enter date")


matcher=fullmatch(pattern,date)

print("inavlid " if matcher==None else "valid")

