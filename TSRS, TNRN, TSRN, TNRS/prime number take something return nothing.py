def prime(num):
    for x in range(0,num):
        for i in range(2,x):
          if x%i==0:
             break
        else:
             print(x, "is prime")
  
prime(10)

