

words=["hello","hai","hello","this","is","this","is","hello"]

# word_frequency
word_frequency={w:words.count(w) for w in words }#{'hello': 3, 'hai': 1, 'this': 2, 'is': 2}

print(word_frequency)

recursive_words=[k for k,v in word_frequency.items() if v>1]

print(recursive_words)

# display non_recursive_words


# most_recursive
# get(key)
# pop(key)
# keys()
# values()
# items()