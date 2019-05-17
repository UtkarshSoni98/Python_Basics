list1=[]
x=int(input("enter size of list"))
for i in range(0,x):
    num=int(input("Enter elemnts"))
    list1.append(num)
print(list1)
z=set(list1)
print("Distinct elemtns in list are",z)
