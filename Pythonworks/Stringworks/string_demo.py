
# capitalize()
# casefold()
# isalpha()
# isdigit()
# isalnum()
# startswith(str)
# endswith(str)

# text="helloPython"

# for ch in text:

#     print(ch)
# print(text.endswith("on"))
# print(text.startswith("he"))
# print(text.capitalize())


# print(text.casefold())

# print(text.isalpha()) #

# print(text.isdigit())

# print(text.isalnum())



# text="hello,world,python"


# words=text.split(",")

# print(words)


text="\t this is \ta line\t"

# remove \n 

new_text=text.strip("\t")

# print(new_text)
# lstrip()
# rstrip()

# text="hello world program"


# text="python programming"
#     # 012345678901234567
#     # string_object[start:end:step] 
# print(text[:6])

# print(text[7:])

# print(text[::2])

# string="hello"

# reversed_text=string[::-1]

# print(reversed_text)



text="helloworld"
#     0123456789

# index of first o

# text.replace()
# text.index("o") => 4

print(text.index('o'))


text="vipinkumar@gamil.com"

# find index of @ 
# slice text from 0:index of slice

print(text[0:text.index("@")])

text="hellopython"
#     012345678910

o_index=text.index("o")

reversed_sub_str=text[o_index-1::-1]

balance_sub_str=text[o_index:]

result=reversed_sub_str+balance_sub_str

print(result)

# smaple input 1
text1="PQRS"

text2="ABCD"
# q) merge two strings
# output  PAQBRCSD


# sample input2

text1="PQRST"
text2="ABC"

# output:PAQBRCST



