def cube(n):
    if n==1:
        return 1
    else:
       return n*n*n+cube(n-1)
x=cube(2)
print(x)
