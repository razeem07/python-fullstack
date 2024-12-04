arr=[100,200,300,400,500,600,700,800,900]
#     0   1   2   3   4   5   6   7   8
#         L                       R

left=1

right=len(arr)-1

if right%2==0:

    right-=1

while(left<right):

    arr[left],arr[right]=arr[right],arr[left]

    left+=2

    right-=2

print(arr)
