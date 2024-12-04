# validate years from 1800 - 2024





from re import fullmatch


pattern="((18|19)[0-9]{2}|20[01][0-9]|202[0-4])"


year=input("enter year")


matcher=fullmatch(pattern,year)

print("inavlid " if matcher==None else "valid")

# validate gmailid

# lowercase
# starts with an alphabet
# numbers optional
# @gmail.com
# before at 6 to 64 characters
