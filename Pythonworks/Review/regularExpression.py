

from re import finditer,findall

text="PINGping20pongpingpongping10@#"

matcher=finditer("[0-9]{2}",text) #[objects]

for m in matcher:

    print(m.start(),m.group())



# [0-9] digit
# [a-z]
# [A-Z]

# [a-zA-Z]

# [a-zA-Z0-9] alphanumerics
# [^a-zA-Z0-9]
# [0-9]{2}
# (91)? 91 is optional
# (91)* zero or more occuranc 
# (91)+


