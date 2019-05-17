def sum(n):
    if n*n==1:
        return 1
    else:
        return n*n+sum(n-1)
x=sum(4)
print(x)




