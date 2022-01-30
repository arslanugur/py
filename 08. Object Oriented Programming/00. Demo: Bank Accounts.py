class Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
  
    def   __repr__(self):
         return f"{self.owner} has account          balance of {self.balance}"
    def deposit(self,d_amount):
        self.balance = self.balance + d_amount
        print ("Transaction sucessful")
    def withdraw(self,w_amount):
        if w_amount > self.balance:
            print ("You don't have enough money")
        else:
            self.balance = self.balance - w_amount 
            print ("Transaction sucessful")
acct1 = Account('Jack', 200)
print (acct1)
print (acct1.owner)
print (acct1.balance)
acct1.withdraw(100)
acct1.deposit(50)
acct1.withdraw(400)

print(" ")
print(" ")

acct2= Account('Jones',1000)
print (acct2)
print(acct2.balance)
acct2.withdraw(500)
acct2.deposit(100)


