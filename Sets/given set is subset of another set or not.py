list1=[]
x=int(input("enter size of list1"))
for i in range(0,x):
    num=int(input("Enter elemnts"))
    list1.append(num)
list2=[]
x=int(input("enter size of list2"))
for i in range(0,x):
    num=int(input("Enter 2nd set elemnts"))
    list2.append(num)    
z=set(list1)
c=set(list2)
print("set 1=",z)
print("set 2=",c)
if c.issubset(z):
    print("set 2 is subset of set1")
else:
    print("set2 is not subset of set 1")

   
