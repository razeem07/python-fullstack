


def swap_dec(fn):#fn=division(2,10)

    def wrapper(n1,n2):#n1=2,n2=10

        if n1<n2:#2<10
            (n1,n2)=(n2,n1)#n1=10,n2=2
        
        return fn(n1,n2)#division(10,2)
    
    return wrapper
    


def round_dec(fn):

    def wrapper(num1,num2):

        num1=round(num1)

        num2=round(num2)

        return fn(num1,num2)
    return wrapper




@round_dec
@swap_dec
def add_number(num1,num2):

    return num1+num2

@round_dec
@swap_dec
def subtraction(num1,num2):

    return num1-num2

@round_dec
@swap_dec
def division(num1,num2):

    return num1/num2




# print(add_number(2.5,3.6)) 

print(subtraction(2.8,12.2))
# 2.8=>3
# 12.2=12
# 12-3=9



lst1=list()
# lst1 


lst2=list()

