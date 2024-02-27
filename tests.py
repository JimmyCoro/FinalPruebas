import unittest
from cuenta_bancaria import CuentaBancaria
from cajero_automatico import CajeroAutomatico

class TestCajeroAutomatico(unittest.TestCase):
    def setUp(self):
        self.cuenta1 = CuentaBancaria("Jimmy", 1000)
        self.cuenta2 = CuentaBancaria("Mario", 2000)
        self.cajero = CajeroAutomatico()
        self.cajero.agregar_cuenta(self.cuenta1, "Jimmy")
        self.cajero.agregar_cuenta(self.cuenta2, "Mario")

    def test_consultar_saldo(self):
        self.assertEqual(self.cajero.consultar_saldo("Jimmy"), 1000)
        self.assertEqual(self.cajero.consultar_saldo("Mario"), 2000)

    def test_realizar_deposito(self):
        self.cajero.realizar_deposito("Jimmy", 500)
        self.assertEqual(self.cajero.consultar_saldo("Jimmy"), 1500)

    def test_realizar_retiro_saldo_suficiente(self):
        self.assertEqual(self.cajero.realizar_retiro("Mario", 1000), 1000)
        self.assertEqual(self.cajero.consultar_saldo("Mario"), 1000)
        #self.assertEqual(self.cajero.consultar_saldo("Mario"), 100, "El saldo real debe ser 1000")


    def test_realizar_retiro_saldo_insuficiente(self):
        self.assertEqual(self.cajero.realizar_retiro("Jimmy", 1500), "Saldo insuficiente")

if __name__ == "__main__":
    unittest.main()
