arr=[1,2,1,2,3,4,3,2]

arr.sort()

duplicate_numbers=[]

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[j]-arr[i]

    if result==0:
        
        if arr[i] not in duplicate_numbers:

            duplicate_numbers.append(arr[i])

print(duplicate_numbers)

