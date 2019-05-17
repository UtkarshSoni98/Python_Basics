import sys
sys.setrecursionlimit(1500)
def natural(N, n=0): 
 while (n<=N):
        if N%2==0:
            print(N)
        natural(N-1,n)
        break       
natural(10)
