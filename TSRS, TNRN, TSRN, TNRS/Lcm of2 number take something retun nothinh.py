def lcm(a,b):

  if(a>b):
    min1=a
  else:
    min1=b
  while(True):
    if(min1%a==0 and min1%b==0):
       print("lcm is:",min1)
       break
    min1=min1+1
    
lcm(4,3)
lcm(4,4)
