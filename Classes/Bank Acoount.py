class BankAccount:
    roi=5.56
    def __init__(self, initial_balance):
        """Creates 200an account with the given balance."""
        self.money = initial_balance 
    
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.money += amount
        return self.money

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
       
        if self.money - amount < 0:
            print("No money")
        else:
            self.money -= amount
        return self.money


    def get_balance(self):
        """Returns the current balance in the account."""
        return self.money
    def r_oi(self):
        return BankAccount.roi
    
my_account = BankAccount(1000)
print("Current balance:",my_account.get_balance())
amt_withdraw=int(input("Enter the amount to withdraw the money"))
print("Money withdraw: ",my_account.withdraw(amt_withdraw))
print("Current balance",my_account.get_balance())
dep=int(input("Do you want to deposite money press 1 and enter"))
if dep==1:
    dep_amt=int(input("Enter the amount to deposite"))
    print("Deposite value:",my_account.deposit(dep_amt))
    print("Thankyou")
else:
    print("Wrong choice")

print("Rate of intrest",my_account.r_oi())    

