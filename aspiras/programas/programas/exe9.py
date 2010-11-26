class Number(int):
    @property
    def inverter(self):
        numero = self
        return str(numero)[::-1]

