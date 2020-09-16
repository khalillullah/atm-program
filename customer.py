from atm_card import ATMCard


class Customer:
    def __init__(self, id, custPin=1234, custBalance=10000):
        self.id = id
        self.pin = custPin
        self.balance = custBalance

    def cekId(self):
        return self.id

    def cekPin(self):
        return self.pin

    def cekBalance(self):
        return self.balance

    def withdrawBalance(self, nominal):
        self.balance -= nominal

    def depositBalance(self, nominal):
        self.balance += nominal
