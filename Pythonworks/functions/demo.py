
# def funtion_name(p1,p2,p3):

    # function defnition
    # return value


def factorial(num):

    fact=1

    for i in range(1,num+1):

        fact=fact*i


    return fact


result=factorial(3)

# print(result)




# create a function num_chk return odd if number is odd else return even

def num_chk(number):

   return "even" if number%2==0 else "odd"
    
# print(num_chk(10))

# q2 create a function max_two with two parameter num1,num2 return largest number
# q3 create a function min_two with two parameter num1,num2 return smallest number

def max_two(num1,num2):

    return num1 if num1>num2 else num2


# print(max_two(100,200))

"""create a function multiplication_table(number,n)
 print multiplication table of number till n"""

# multiplication_table(3,50)

def multiplication_table(number,n=10):#3,5

    for i in range(1,n+1):

        print(f"{i} * {number} = {i*number}")
        


# multiplication_table(5)


# create a function exponent with two parameter num1,n

def expo(number,n=2):

    return number**n

# print(expo(6))


# create a function smart_sub with three parameter num1,num2,reverse
# reverse takes boolean value
# if reverse==True then return num2-num1 else return num1-num2

# def smart_sub(num1,num2,reverse):


# smart_sub(2,10,True)# 10-2
# smart_sub(2,10,False)# 2-10

def smart_sub(num1,num2,reverse=False):#argu,ents

    return num2-num1 if reverse==True else num1-num2

# print(smart_sub(10,20))#parameters




# create a function random_numbers(start,end,step)


# create function 

# def function_name(arg1,arg2,arg3,,,,,arg=defaultvalue):

    # function defnition

    # return 

# function_name(p1,p2)

# is_perfect_number(number)

# is_armstrong_number(number)

# is_palindrome_number(number)

