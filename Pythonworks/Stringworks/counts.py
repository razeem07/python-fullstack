text="pneumonoultramicroscopicsilicovolcanoconiosis"
v_count=0

c_count=0

vowel_sequence=("a","e","i","o","u")

for ch in text:

    if ch in vowel_sequence:

        v_count=v_count+1
    else:
        c_count+=1


print("vowel count=",v_count)

print("consonant count",c_count)