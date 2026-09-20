class CalculadorTemperatura:
    def __init__(self):
        self.historial = []
    def diferencia_temperatura(self, t1, t2):
        diferencia =abs(t1-t2)
        self.historial.append(diferencia)
        return diferencia
    def temperatura_mas_cercana(self, referencia, *args):
        temperatura_cercana = None
        menor_diferencia = None
        for temperatura in args:
            diferencia = abs(referencia-temperatura)
            if menor_diferencia is None or diferencia < menor_diferencia:
                menor_diferencia =diferencia
                temperatura_cercana = temperatura
        return temperatura_cercana
x= CalculadorTemperatura()
print(x.diferencia_temperatura(20, 35))
print(x.temperatura_mas_cercana(
    25,
    10,
    22,
    30,
    40
))
print(x.historial)
