class GestorTemperatura:
    def __init__(self):
        self.lista_temperaturas=[]
        self.lista_maxima=[]
        self.lista_minima=[]
    def registrar_temperatura(self, temp):
        self.lista_temperaturas.append(temp)
    def registrar_multiples(self, *args):
        for temp in args:
            self.lista_temperaturas.append(temp)

    def minima(self):
        return min(self.lista_temperaturas)
    def maxima(self):
        return max(self.lista_temperaturas)
    def promedio(self):
        return sum(self.lista_temperaturas)/len(self.lista_temperaturas)

x=GestorTemperatura()
x.registrar_multiples(30,50,70,90,30,40,20)
print({
    "minima": (x.minima()),
    "maxima": (x.maxima()),
    "promedio": (x.promedio())
})