class Analizador_Numeros:
    def __init__(self):
        self.numeros_pares=[]
        self.numeros_impares=[]
    def es_par(self, numero):
        return numero%2==0
    def cargar_varios(self, *args):
        for numero in args:
            if self.es_par(numero):
                self.numeros_pares.append(numero)
            else:
                self.numeros_impares.append(numero)
        return self.numeros_pares
    def cantidad_pares(self):
        return len(self.numeros_pares)
    def cantidad_impares(self):
        return len(self.cantidad_impares)
    def diccionario(self):
        return {
            "numero de pares": len(self.numeros_pares),
            "pares": self.numeros_pares,
            "numero de impares": len(self.numeros_impares),
            "impares": self.numeros_impares
        }
    
x=Analizador_Numeros()
print(x.cargar_varios(1,2,3,4,5,6,7,8,9))
print(x.diccionario())