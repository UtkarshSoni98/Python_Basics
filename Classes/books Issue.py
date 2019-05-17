class Book:
    def __init__(self,bookid,title,price,author):
     self.bookid=bookid
     self.title=title
     self.price=price
     self.author=author

    def chnge(self,newprice):
        self.price=newprice
        return self.price

    def current(self):
        return self.bookid,self.title,self.price,self.author
q=int(input("Enter Bookid"))
w=input("Enter Title")
e=int(input("Enter Price"))
r=input("Enter Author Name")
mybook=Book(q,w,e,r)
print("Current details:",mybook.__dict__)
ch=int(input("Do you want to chnage the price is yes press 1"))
if ch==1:
  new=int(input("Enter New price"))
  print("new price of book ",mybook.chnge(new))
else:
    pass

l=int(input("Press 1 for see all info "))
if l==1:
    print(mybook.__dict__)
else:
    pass


     
