text="ABAABBC"

def get_count(char):

    return text.count(char)

most_frequent_character=max(text,key=get_count)
print(most_frequent_character)

least_recursive_character=min(text,key=get_count)
print(least_recursive_character)

# most recursive character

# non recursive character
# 11
