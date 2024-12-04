

number=int(input("enter number"))#123

original=number

total=0

while(number !=0):

    digit=number%10

    digit_square=digit**3

    total=total+digit_square

    number=number//10#12 1 0

print("same" if total==original else "different")






