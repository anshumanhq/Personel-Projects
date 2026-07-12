from bank import Bank
from account import Account, SavingAccount, CurrentAccount
from transaction import Transaction

def main():
    print("Welcome to the Banking System")
    bank = Bank()
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Transaction History")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            holder_name = input("Enter account holder's name: ")
            acc_type = input("Enter account type (Saving/Current): ")
            acc_number = bank.create_account(holder_name, acc_type)
            print(f"Account created successfully! Account Number: {acc_number}")
        
        elif choice == '2':
            acc_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(acc_number, amount)
        
        elif choice == '3':
            acc_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(acc_number, amount)
        
        elif choice == '4':
            from_acc_number = input("Enter source account number: ")
            to_acc_number = input("Enter destination account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(from_acc_number, to_acc_number, amount)
        
        elif choice == '5':
            acc_number = input("Enter account number: ")
            acc = bank.find_account(acc_number)
            if acc:
                transactions = acc.get_transaction_history()
                for transaction in transactions:
                    print(transaction)
            else:
                print("Account not found.")
        
        elif choice == '6':
            print("Thank you for using the Banking System!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()