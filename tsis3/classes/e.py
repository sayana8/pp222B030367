#5
class Account:
    balance =0
    def bank(self):
        print(self.balance)
    def deposit(self, In):
        Account.balance += In
    def withdraw(self, out):
        if out > Account.balance: print('Insufficient funds for withdrawal! \n')
        else: Account.balance -= out

owner = input('Enter your name: ')
dis = ''
while dis != '4':
    dis = input('What do you want '+ owner +'''?
1 - show balance
2 - deposit to bank
3 - withdraw from bank
4 - end
I want:  ''')
    if dis == '1': Account().bank()
    elif dis == '2': 
        In = int(input('Enter the amount to deposit: '))
        Account().deposit(In)
    elif dis == '3': 
        out = int(input('Enter the amount to withdraw: '))
        Account().withdraw(out)