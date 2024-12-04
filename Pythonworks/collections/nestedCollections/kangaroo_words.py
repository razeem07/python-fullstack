source_word="CHIKENN"

target_word="NIKES"

character_count={ch:source_word.count(ch)  for ch in source_word}

is_kangarro=True

for ch in target_word:

    if ch in character_count and character_count.get(ch)>0:

        character_count[ch]-=1
    else:
        is_kangarro=False
        
        break

print(is_kangarro)



# smaple_input="{}"
# op=>valid

# smaple_input="{()}"
# op=>valid


# smaple_input="{(})"
# op=>valid

# smaple_input="[]("
# op=>valid




