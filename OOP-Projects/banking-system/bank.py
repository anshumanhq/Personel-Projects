from account import Account, SavingAccount, CurrentAccount
from utils import register_transaction

class Bank:
    def __init__(self):
        self.accounts=[]
    
    def create_account(self, holder_name, acc_type):
        if 'saving' in acc_type.lower():
            acc=SavingAccount(holder_name)
            self.accounts.append(acc)
            return acc.acc_number
        elif 'current' in acc_type.lower():
            acc=CurrentAccount(holder_name)
            self.accounts.append(acc)
            return acc.acc_number
    
    def find_account(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number==acc_number:
                return acc
        return None
    
    def deposit(self, acc_number, amount):
        acc=self.find_account(acc_number)
        if acc:
            acc.deposit(amount)
            transaction = register_transaction("Deposit", amount, acc.get_balance())
            acc.add_transaction(transaction)
        else:
            print("Account not found.")

    def withdraw(self, acc_number, amount):
        acc=self.find_account(acc_number)
        if acc:
            acc.withdraw(amount)
            transaction = register_transaction("Withdrawal", amount, acc.get_balance())
            acc.add_transaction(transaction)
        else:
            print("Account not found.")
    
    def transfer(self, from_acc_number, to_acc_number, amount):
        from_acc=self.find_account(from_acc_number)
        to_acc=self.find_account(to_acc_number)
        if from_acc and to_acc:
            if from_acc.get_balance()>=amount:
                from_acc.withdraw(amount)
                to_acc.deposit(amount)
                transaction_from = register_transaction("Transfer Out", amount, from_acc.get_balance())
                transaction_to = register_transaction("Transfer In", amount, to_acc.get_balance())
                from_acc.add_transaction(transaction_from)
                to_acc.add_transaction(transaction_to)
                print(f"Transferred {amount} from {from_acc_number} to {to_acc_number}.")
            else:
                print("Insufficient funds in the source account.")
        else:
            print("One or both accounts not found.")