#Find All Square Between Two Number--

a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
s=range(a,b+1)
for i in  s:
    sqr=i*i
    print(sqr)
