class Bank_Account:
    def __init__(self):
        self.balance=0
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")
    def display(self):
        print("\n Net Available Balance=",self.balance)
s = Bank_Account()
print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
while(1):
    print("1.Deposit \n2.Withdraw \n3.Display \n4.Exit")
    x=int(input("Enter the Choice:(1,2,3,4)"))
    if(x==1):
        s.deposit()
    elif(x==2):
        s.withdraw()
    elif(x==3):
        s.display()
    elif(x==4):
        break
    else:
        print("Wrong choice!!")