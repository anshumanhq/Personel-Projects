import random
from datetime import datetime
from transaction import Transaction

def generate_account_number():
    prefix="1001"
    today=datetime.now()
    datepart=today.strftime("%d%m%Y")
    rand_part=''.join([str(random.randint(0,9)) for _ in range(3)])
    acc_num=prefix+datepart+rand_part
    return acc_num

def register_transaction(type,amount,balance_after):
    transaction_id = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    transaction = Transaction(transaction_id, type, amount, balance_after, timestamp)
    return transaction