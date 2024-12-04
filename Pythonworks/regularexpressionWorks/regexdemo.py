

from re import finditer

text="fat cat runs very fast to catch the rat"


matcher=finditer("(at)",text)# [(start,gruop),(),(),]


for obj in matcher:

    print(obj.groups())  
    
    print(obj.start(),obj.group())





text="I have 3 cars,2 bike and 1 Cycle"

