import sys
sys.setrecursionlimit(1500)
def cube(N,n=0):
 while n<=N:
     print(N*N*N)
     cube(N-1,n)
     break
cube(10)    
