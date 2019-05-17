x=int(input("Enter 1st number"))
y=int(input("Enter 2nd Number"))
z=int(input("Enter 3rd Number"))
if x>y>z:
    print(f"{x} is Greatest")
elif x>z>y:
     print(f"{x} is Greatest")
elif y>x>z:
    print(f"{y} is Greatest")
elif y>z>x:
    print(f"{y} is Greatest")

elif z>x>y:
    print(f"{z} is Greatest")
elif z>y>x:
    print(f"{z} is Greatest")
