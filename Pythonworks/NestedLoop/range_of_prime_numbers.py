# read start,end
# print prime numbers from start to end

start=int(input("enter start"))#5

end=int(input("enter limt"))#10
#                                        
for num in range(start,end+1): #[5,6,7,8,9,10]

    is_prime=True

    for i in range(2,num):# [2,5]

        if num%i==0:#6%2==0

            is_prime=False

            break
    
    if is_prime==True:

        print(num) #5   

