# binary search

arr=[10,8,7,12,13,20,25]

# read search element

search_element=int(input("enter number"))

arr.sort()

low=0

upp=len(arr)-1

is_persent=False

while(low<=upp):

    mid=(low+upp)//2

    if search_element==arr[mid]:

        is_persent=True

        break
    
    elif search_element<arr[mid]:

        upp=mid-1

    elif search_element > arr[mid]:

        low=mid+1
        
print(is_persent) 