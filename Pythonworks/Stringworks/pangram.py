text="The quick brown fox jumps over the lazy dog".casefold()


alphabets="abcdefghijklmnopqrstuvwxyz"

is_pangram=True

for ch in alphabets:

    if ch not  in text:

        is_pangram=False

        break

print(is_pangram)


source_word="silent" #heart

target_word="listen"#earth

# anagarm 

# casefold()
# capitalize()
# isalpha()
# isdigit()
# isalnum()
# startswith()
# endswith()
