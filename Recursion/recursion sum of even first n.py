def sum(n):
   if n==0:
       return n
   else:
        
         return 2*n-2+sum(n-1)
  
x=sum(10)
print(x)
