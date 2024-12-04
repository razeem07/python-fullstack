
# extract digit


number=int(input("enter number"))


while(number!=0):

    digit=number %10

    print(digit)

    number=number//10