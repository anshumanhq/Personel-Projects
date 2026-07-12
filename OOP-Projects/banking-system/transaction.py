class Transaction:
    def __init__(self, transaction_id, type, amount, balance_after, timestamp):
        self.transaction_id = transaction_id
        self.type = type
        self.amount = amount
        self.date = balance_after
        self.description = timestamp

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Amount: {self.amount}, Date: {self.date}, Description: {self.description}"

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "type": self.type,
            "amount": self.amount,
            "balance_after": self.date,
            "timestamp": self.description
        }