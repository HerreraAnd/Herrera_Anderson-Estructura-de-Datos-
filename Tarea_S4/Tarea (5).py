class AnalizadorNumeros:
    def __init__(self):
        self.pares=[]
        self.impares=[]
    def es_par(self, numero):
        return numero%2==0
    def separa(self, *numeros):
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)
        return {
            "pares": self.pares,
            "impares": self.impares
        }
prueba=AnalizadorNumeros()
print(prueba.separa(3,4,8,9,14))



