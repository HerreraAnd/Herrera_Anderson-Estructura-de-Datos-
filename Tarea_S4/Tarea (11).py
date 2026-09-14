class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}
    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1
    def elemento_mas_frecuente(self):
        return max(self.frecuencias, key=self.frecuencias.get)
    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)
cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
cf.agregar_elemento("a")
cf.agregar_elemento("a")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))
