from re import findall


f=open("C:\\Users\\Luminar\\Desktop\\Pythonworks\\regexfileworks\\urls.txt")

content=f.read()

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)
