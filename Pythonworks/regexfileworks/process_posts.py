
from re import finditer

f=open("C:\\Users\\Luminar\\Desktop\\Pythonworks\\regexfileworks\\social_posts.txt")

for line in f:

    words=line.rstrip("\n")#Check out my new blog post! #blog #webdevelopment

    pattern="#\w+"

    macther=finditer(pattern,words)

    for obj in macther:

        print(obj.group())

