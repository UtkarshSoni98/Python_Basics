import sys
sys.setrecursionlimit(1500)
def square(N,n=0):
    while n<=N:
        print(N*N)
        square(N-1,n)
        break
square(10)    
    
