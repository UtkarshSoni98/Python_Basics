words={}
l=[]
x=int(input("Enter size of key"))
for i in range(0,x):
    num=int(input("Enter Roll numbers "))
    l.append(num)
for i in l:

    print("Enter the Name for",i)
    words[i]=input()
print("Dictonary is: ",words)
for i in words:
    print("Roll Number is: ",i,"Name of student :",words[i])
