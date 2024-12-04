
lst1=["apple","mango","onion","potatto"]
#      0        1       2        3
#       

lst2=[100,200]
#      0    1
result={}

for i in range(0,len(lst2)):

    list_one_index_element=lst1[i]
    list_two_index_element=lst2[i]

    result[list_one_index_element]=list_two_index_element


balance_elements=lst1[len(lst2):]

for index,element in enumerate(balance_elements):

    result[element]=index+1

print(result)
