x=input("Enter string: ")
x=x.casefold()
y=x[len(x)::-1]
if x==y:
    print("string is palindrome")
else:
    print("It is not palindrome")
