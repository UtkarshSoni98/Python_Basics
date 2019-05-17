words={}
l=[]
x=int(input("Enter size of key"))
for i in range(0,x):
    num=int(input("Enter key "))
    l.append(num)
for i in l:

    print("Enter the values")
    words[i]=input()
print("Dictonary is: ",words)
for i in words:
    print("KEy is: ",i,"Value is :",words[i])
