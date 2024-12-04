
from re import finditer

text="I have 3 cars,2 bike and 1-Cycle "

# pattern=r"\w" #[a-zA-Z0-9] alphanumeric
# pattern="\d"  # "[0-9]" digits
# pattren="\D" #"[^0-9]" exclude digits
# pattern="\W" #special characters [^a-zA-Z0-9]

pattern="\s" #space
pattern="\S" #exclude space



matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())
