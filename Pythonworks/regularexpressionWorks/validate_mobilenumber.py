


# rule 10 digit
# vaildate mobile number


from re import fullmatch

mobile_number=input("enter mobile number :")

pattern="(91)+[0-9]{10}"

matcher=fullmatch(pattern,mobile_number)


if matcher==None:

    print("invalid")

else:
    print("valid")
