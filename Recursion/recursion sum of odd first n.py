def sum(n):
   if n==1:
       return n
   else:
        
         return 2*n-1+sum(n-1)
  
x=sum(5)
print(x)
