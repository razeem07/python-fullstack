arr=[2,3,4,5,6,8,9]

left=0

right=len(arr)-1

sum=8

while(left<right):

    cur_sum=arr[left]+arr[right]

    if cur_sum==sum:

        print(arr[left],arr[right])

        left=left+1

        right=right-1

    elif cur_sum >sum:

        right-=1
    
    elif cur_sum<sum:

        left+=1



