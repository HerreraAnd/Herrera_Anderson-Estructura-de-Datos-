class Gestor_temperatura:
    def __init__(self):
        self.temperatura=[]
    def registrar_temperatura(self, temperatura):
        self.temperatura.append(temperatura)
    def minima(self):
        return min(self.temperatura)
    def maxima(self):
        return max(self.temperatura)
    def promedio(self):
        return sum(self.temperatura)/len(self.temperatura)
    def registrar_multiples(self, *temperaturas):
        for temperatura in temperaturas:
            self.registrar_temperatura(temperatura)
gestor=Gestor_temperatura()
gestor.registrar_multiples(20,30,40,50)
print("minima", gestor.minima())
print("maxima", gestor.maxima())
print("promedio", gestor.promedio())