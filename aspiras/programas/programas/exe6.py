class Hora(int):

    def converter(self, minuto):
        hora = self
        self.minuto = minuto
        if hora < 12:
            return hora + 12, self.minuto
        return hora - 12, ':', self.minuto

