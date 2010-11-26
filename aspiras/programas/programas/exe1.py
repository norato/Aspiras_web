class Numero(int):
    
    @property
    def programa1(self):
        lista = []
        for i in range(self):
            b = range(self)
            lista.append(b)
        for i in range(self):
            for j in range(self):
                lista[i].remove(j)
        for i in range(1, self + 1):
                lista[i-1].append(str(i) * i)
        return lista

    @property
    def programa2(self):
        lista = []
        for i in range(self):
            c = range(self)
            lista.append(c)
        for i in range(self):
            for f in range(self):
                lista[i].remove(f)
        for i in range(1, self+1):
            for a in range(1, i+1):
                lista[i-1].append(a)
        return lista

    def programa3(self, valor1, valor2, valor3):
        return sum([valor1, valor2, valor3])
    
    @property
    def programa4(self):
        if (self > 0):
            return "Positivo"
        return "Negativo"
 

    def programa6(self, minuto):
        hora = self
        self.minuto = minuto
        if hora < 12:
            return hora + 12, self.minuto
        return hora - 12, self.minuto

    def programa7(self):
        return self

    @property
    def programa8(self):
        numero = str(self)
        return len(numero)

    @property
    def programa9(self):
        numero = self
        return str(numero)[::-1]

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


    def programa10(self, dia, mes, ano):
        relacao_mes_extenso = {1:"Janeiro", 2:"Fevereiro", 3:"Marco", 4:"Abril", 5:"Maio", \
                            6:"Junho", 7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", \
                            11:"Novembro", 12:"Dezembro"}
        if self.validar_data(dia, mes, ano) == True:
            return '%i de %s de %i'%(dia, relacao_mes_extenso[mes], ano)
        return "Data Invalida"

class Dinheiro(float):
    def programa5(self,taxa_imposto, custo):
        self.taxa_imposto = taxa_imposto
        self.custo = custo
        valor_imposto = (taxa_imposto / 100.) * custo
        return self.custo + valor_imposto


