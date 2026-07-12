from utils import generate_account_number

class Account:
    def __init__(self, holder_name:str):
        self.acc_number=generate_account_number()
        self.holder_name=holder_name
        self.__balance=0
        self.transaction=[]
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self,amount):
        if amount>0:
            if self.__balance>=amount:
                self.__balance-=amount
                print(f"Withdrew {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def get_balance(self):
        return self.__balance
    
    def add_transaction(self,transaction):
        self.transaction.append(transaction)
    
    def get_transaction_history(self):
        return self.transaction

class SavingAccount(Account):
    def __init__(self, holder_name:str):
        super().__init__(holder_name)
        self.deposit(1000)
        self.interest_rate = 0.04
    
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} added. New balance: {self.get_balance()}")
    
    def withdraw(self, amount):
        current_balance = self.get_balance()
        if amount > 0 and current_balance >= amount and current_balance - amount >= 1000:
            super().withdraw(amount)
        else:
            print("Insufficient funds or minimum balance requirement not met.")

class CurrentAccount(Account):
    def __init__(self, holder_name: str):
        super().__init__(holder_name)

    def withdraw(self, amount):
        if amount > 0:
            if self.get_balance() - amount >= -5000:
                super().withdraw(amount)
            else:
                print("Exceeding the maximum allowed overdraft of 5000.")
        else:
            print("Withdrawal amount must be positive.")