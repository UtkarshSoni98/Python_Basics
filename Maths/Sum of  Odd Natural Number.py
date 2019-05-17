#This Program work only with odd numbers--

n=int(input("Enter a odd number: "))
sum = 0
while(n > 0):
    sum=sum+n
    n=n-2
print("The sum of first n Odd Numbers is: ",sum)
