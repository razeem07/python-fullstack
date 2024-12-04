# valiadte Pancard number

# 3alphabets
# 4th place alphabet[PCAFHT]
# 1alphabet
# 4digit
# 1alphabet


from re import fullmatch


pancard_number=input("enter pancard number :")


pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard_number)

if matcher==None:

    print("invalid")

else:
    print("valid")


# validate month 01-12
# dat 1 2 3 4 5 6 7 8 9
#     01 02 03 04 05 06 07 08 09
#     10 11 12