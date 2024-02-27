class CuentaBancaria:
    def __init__(self, persona, saldo=0):
        self.persona = persona
        self.saldo = saldo

    def consultar_saldo(self):
        return self.saldo

    def realizar_deposito(self, cantidad):
        self.saldo += cantidad

    def realizar_retiro(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return cantidad
        else:
            return "Saldo insuficiente"