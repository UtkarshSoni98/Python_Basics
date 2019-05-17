a=float(input("Enter marks of 1st subject out of 100: "))
b=float(input("Enter marks of 2nd subject out of 100: "))
c=float(input("Enter marks of 3rd subject out of 100: "))
d=float(input("Enter marks of 4th subject out of 100: "))
e=float(input("Enter marks of 5th subject out of 100: "))
if a>=33 and b>=33 and c>=33 and d>=33 and e>=33:
    print("Student is pass")
    s=a+b+c+d+e
    print("Total marks is",s)
    per=(s*100)/500
    print("Percentage is",per)
    if per>30 and per<60:
        print("Divison is 3rd")
    elif per>60 and per<70:
        print("Division is 2nd")
    elif per>70:
        print("Division is 1st")

else:
    print("Student is Fail")
    s=a+b+c+d+e
    print("Total marks is",s)
    per=(s*100)/500
    print("Percentage is",per)
    print("Division is 3rd")
   

