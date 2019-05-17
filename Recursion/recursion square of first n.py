import sys
sys.setrecursionlimit(1500)
def square(N,n=0):
    while N>=n:
        print(n*n)
        square(N,n+1)
        break
square(1000)    
    
