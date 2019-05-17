import sys
sys.setrecursionlimit(1500)
def natural(N, n=0): 
    print(N)
    if N>=0:
        natural(N-1, n)
    
natural(10)        
