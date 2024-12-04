
import time
text1="PQRST"

text2="ABC"


smallest_text=text1 if len(text1)< len(text2)  else text2

largest_text=text1 if len(text1)>len(text2) else text2

result=""

for i in range(0,len(smallest_text)):

    result+=text1[i]+text2[i]

balance_text=largest_text[len(smallest_text):]


result+=balance_text

print(result)

# data types
# int,float,str,
# sequence =>str
# boolean>bool

# collection type
# list
# tuple
# set
# dictionary

# shirts store (5000 shirts)
# size organise L M XL  color price

# medicine 500medice A=>a b=>b