words={}
l=[1,2,3,4,5]
for i in l:
    print("Enter value for",i)
    words[i]=input()
print("Dictonary elemnts is",words)
for i in words:
    print("key is",i,"value is",words[i])
