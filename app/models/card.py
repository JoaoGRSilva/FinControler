class Card:
    def __init__(self, name, limit, due_date, id):
        self.name = name
        self.limit = limit
        self.due_date = due_date
        self.current_invoice = 0.0
        self.current_installments = 0.0
        self.id = id

    def add_to_invoice(self, local,value, installmnets = 1):
        if value <= 0:
            return print("Adicione um valor válido")


        if installmnets == 1:
            self.current_invoice += value
            self.limit -= value
            self.local = local
            return self.current_invoice
        else:
            self.local = local
            self.limit -= value
            installments_value = value/installmnets
            self.current_invoice += installments_value
            self.current_installments = installments_value * (installmnets - 1)

    def pay_invoice(self, payament):
        self.current_invoice -= payament
        return payament
    
    def get_available_limit(self):
        return self.limit