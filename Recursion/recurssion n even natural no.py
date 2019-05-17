import sys
sys.setrecursionlimit(1500)
def nat(N,n=0):
   while (N>=n) :
     if  n%2==0:
         print(n)
     nat(N,n+1)
     break
    
nat(10)
