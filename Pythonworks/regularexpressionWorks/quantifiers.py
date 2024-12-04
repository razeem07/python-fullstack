
from re import finditer

text="abbbababbabaaaab"
#     0123456789012345

# pattern="a{2}"

# pattern="a{1,3}"

pattern="a*" #* any number including 0 

"[a-z]{2} [0-9]{2} [a-z]{1,2}[0-9]*"
# kl08bn4970
# kl08bn49706789000
# kl08bn


matcher=finditer(pattern,text)

for obj in matcher:
    print(obj.start(),obj.group())