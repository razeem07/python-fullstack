# validate years from 1800 - 2024





from re import fullmatch


pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"


gmail_id=input("enter gamil")


matcher=fullmatch(pattern,gmail_id)

print("inavlid " if matcher==None else "valid")

# validate gmailid

# lowercase
# starts with an alphabet
# numbers optional
# @gmail.com
# before at 6 to 64 characters

# re+file

