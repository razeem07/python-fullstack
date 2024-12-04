


users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followers=["sanju","rohit","kohli"]

mutual_friends=set(rahul_followers).intersection(set(sanju_followers))

print(mutual_friends)
# follow_sugestions ["sanju","pandya","siraj"]


# rahul_follow_suggestion=set(users).difference(set(rahul_followers))

# print(rahul_follow_suggestion)

