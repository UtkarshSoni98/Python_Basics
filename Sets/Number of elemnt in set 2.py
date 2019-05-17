list1=[]
x=int(input("enter size of set"))
for i in range(0,x):
    num=int(input("Enter elemnts"))
    list1.append(num)
z=set(list1)
print("set is=",z)
print("Number of elemnts in set are:",len(z))      
