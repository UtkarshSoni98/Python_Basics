a=float(input("Enter side 1: "))
b=float(input("Enter side 2: "))
c=float(input("Enter side 3: "))
#semi perimeter s
s=(a+b+c) / 2
#area of traingle
area=(s*(s-a)*(s-b)*(s-c)) **0.5
print("Area of Traingle: ",area)

