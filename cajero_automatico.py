from cuenta_bancaria import CuentaBancaria

class CajeroAutomatico:
    def __init__(self):
        self.cuentas = {}

    def agregar_cuenta(self, cuenta, persona):
        self.cuentas[persona] = cuenta

    def consultar_saldo(self, persona):
        return self.cuentas[persona].consultar_saldo()

    def realizar_deposito(self, persona, cantidad):
        self.cuentas[persona].realizar_deposito(cantidad)

    def realizar_retiro(self, persona, cantidad):
        return self.cuentas[persona].realizar_retiro(cantidad)