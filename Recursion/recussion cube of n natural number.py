import sys
sys.setrecursionlimit(1500)
def cube(N,n=0):
 while N>=n:
     print(n*n*n)
     cube(N,n+1)
     break
cube(10)    
