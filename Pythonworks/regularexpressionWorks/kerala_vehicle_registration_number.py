

# starting with KL

# 2digit

# alphabets minimum1 maxuimum 2
# 4 digit


from re import fullmatch

reg_num=input("enter registration number :")


pattern="(KL|kl)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,reg_num)

if matcher==None:

    print("invalid")

else:
    print("valid")

# passport
# aadhar number
# driving licence

