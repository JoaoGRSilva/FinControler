from models.card import Card
from models.account import Account
from models.transaction import Transaction

def run_test():
    acc = Account(balance=4000, user='Eu', bank= 'Mango')
    cardzao = Card(name='Cartao', limit=10000, due_date='10', id=1)
    acc.card.append(cardzao)

    print("Saldo inicial: ", acc.get_balance())

    print("## Antes da compra")
    print("Fatura atual:", cardzao.current_invoice)
    print("Limite: ", cardzao.get_available_limit())

    cardzao.add_to_invoice(local='balada', value=666)

    print("## Depois da compra")
    print("Fatura atual: ", cardzao.current_invoice)
    print("Limite: ", cardzao.get_available_limit())


    print("## Compra débito")
    acc.register_transaction("Mercado -50")
    acc.add_balance(-50)
    print("Saldo após débito:", acc.get_balance())
    print("Transações:", acc.transactions)



if __name__ == "__main__":
    run_test()