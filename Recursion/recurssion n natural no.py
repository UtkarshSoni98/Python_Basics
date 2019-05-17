import sys
sys.setrecursionlimit(1500)
def natural(N, n=0):  
    print(n)
    if n < N:
        natural(N, n + 1)
    
natural(1000)        
