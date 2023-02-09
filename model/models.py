class Cuenta():
    def __init__(self, saldoInicial):
        self.saldo = saldoInicial

    def transferir(self, monto, cuentaDestino):
        # Validar que el saldo de la cuenta origen sea es suficiente
        # Si el saldo es mayor o igial al monto se debita el monto de la cuenta origen
        # y se deposita el monto de la cuenta destino
        #
        if not self.esMontoValido(monto):
            if not self.tieneSaldoSuficiente(monto):
                return
        self.debitar(monto)
        cuentaDestino.acreditar(monto)

    def tieneSaldoSuficiente(self, monto):
        return self.saldo >= monto

    def debitar(self, monto):
        self.saldo -= monto

    def acreditar(self, monto):
        self.saldo += monto

    def obtenerSaldo(self):
        return self.saldo

    def esMontoValido(self, monto):
        return monto > 0
