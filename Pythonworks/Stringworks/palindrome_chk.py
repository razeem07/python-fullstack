text="malayalam"
#index012345678     
# len 123456789
length=len(text)-1 #9-1

reversed_str=""

for i in range(length,-1,-1):

    reversed_str+=text[i]

print(reversed_str)
