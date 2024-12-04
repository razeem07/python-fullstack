

arr=[1,2,2,2,1,4,5]
# duplicate numbers 
arr=[1,2,4,5]


#    0 1 2 3
#      i j

arr.sort()

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[j]-arr[i]

    if result!=1:

        print(arr[i]+1,"is missing")
        
        break



