class User:
    bank_name = 'First National Dojo'
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"Name : {self.name} Account Balance: {self.account_balance}")
        return self

    def tansfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)
        return self , other_user


reza = User('Reza', "amraeireza@gmail.com")
nima = User('Nima', "amraeinima@gmail.com")
amir = User('Amir', "amraeiamir@gmail.com")

reza.make_deposit(100).make_deposit(1000).make_deposit(300).make_withdrawl(500).display_user_balance()

nima.make_deposit(100).make_deposit(200).make_withdrawl(50).make_withdrawl(100).display_user_balance()

amir.make_deposit(100).make_withdrawl(50).make_withdrawl(50).make_withdrawl(100).display_user_balance()

reza.tansfer_money(amir,500)
reza.display_user_balance()
amir.display_user_balance()