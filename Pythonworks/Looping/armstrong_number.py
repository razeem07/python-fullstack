number=int(input("enter number"))

original=number

digit_count=len(str(number))

total=0

while(number!=0):

    # step extract digit

    digit=number%10

    exponent=digit**digit_count

    total=total+exponent

    number=number//10

print("armstorng number" if total==original else "not armstrong number")


# for 

