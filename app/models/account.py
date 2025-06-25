class Account:
    def __init__(self, balance, user, bank):
        self.balance = balance
        self.user = user
        self.card = []
        self.bank = bank
        self.transactions = [] 
        
    def add_balance(self, value):
        self.balance += value
        return self.balance

    def register_transaction(self, movement):
        self.transactions.append(movement)
        return movement

    def get_balance(self):
        return self.balance