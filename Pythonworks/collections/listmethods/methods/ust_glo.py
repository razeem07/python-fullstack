
# spample input

arr=[100,200,300,400,500,600,700,800]
#     0    1   2   3  4   5   6   7
#     i

odd_position_numbers=[num for index,num in enumerate(arr) if index%2!=0]


odd_position_numbers.reverse()

print(odd_position_numbers)#[800, 600, 400, 200]
#                             0    1    2    3

i=1

for index,num in enumerate(odd_position_numbers):#index=0 number=800

    arr[i]=num

    i+=2

print(arr)