class Number(int):
    @property
    def number_of_digits(self):
        numero = str(self)
        return len(numero)

