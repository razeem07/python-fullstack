
num1=int(input("enter number1")) #16

num2=int(input("enter number2"))#24

gcd=1

min_num=min(num1,num2)


for i in range(1,min_num+1):#(1,,,,16)

    if num1%i==0 and num2%i==0:

        gcd=i

print(gcd)


# lcm()


# logic=>program



