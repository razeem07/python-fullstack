
arr=[2,3,4,5,7,8,9]
# complexity high
sum=int(input("enter sum"))#80

count=0

for i in range(0,len(arr)-1):

    for j in range(i+1,len(arr)):

        count+=1

        cur_sum=arr[i]+arr[j]

        if sum==cur_sum:
            print(arr[i],arr[j])

            break

print(count)





# T1
# App1 (20mnt) 
# App2(5mnt)


