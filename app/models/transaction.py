from datetime import datetime
from .card  import Card
from .account import Account

class Transaction:
    def __init__(self, local, value, installmnets):
        self.local = local
        self.value = value
        self.date = datetime.today('%d-%m-%Y')
        self.installmnets = installmnets

    def new_credit_transaction(self, local, value, installmnets):
        limit = Card.get_available_limit()
        if value > limit:
            return print("Valor acima do limite disponivel")
        
        else:
            Card.add_to_invoice(local, value, installmnets)
            
    def new_debit_transaction(self, local, value):
        balance = Account.get_balance()
        if value > balance:
            return print("Valor acima do saldo em conta")
        
        else:
            balance -= value
            movement = local + value
            Account.register_transaction(movement) 