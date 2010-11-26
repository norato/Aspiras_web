class Data(int):

    def verificar_ano_bissexto(self, ano):
        if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
            return True

    def validar_data(self, dia, mes, ano):
        relacao_numero = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if ano > 0:
            if (mes > 0) and (mes <13):
                if mes == 2:
                    if self.verificar_ano_bissexto(ano) == True:
                        if (dia > 0) and (dia < 30): return True
                    else:
                        if (dia > 0) and (dia < 29): return True
                elif (dia > 0) and (dia <= relacao_numero[mes]): return True


    def data_extenso(self, dia, mes, ano):
        relacao_mes_extenso = {1:"Janeiro", 2:"Fevereiro", 3:"Marco", 4:"Abril", 5:"Maio", \
                            6:"Junho", 7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", \
                            11:"Novembro", 12:"Dezembro"}
        if self.validar_data(dia, mes, ano) == True:
            return '%i de %s de %i'%(dia, relacao_mes_extenso[mes], ano)
        return "Data Invalida"

