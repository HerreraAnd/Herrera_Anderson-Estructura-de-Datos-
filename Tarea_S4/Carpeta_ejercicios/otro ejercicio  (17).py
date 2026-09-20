class AgrupadorTemperaturas:
    def __init__(self):
        self.temperaturas = {}
    def clasificar_temperatura(self, temperatura):
        if temperatura<15:
            return "fria"
        elif temperatura<25:
            return "templada"
        elif temperatura<35:
            return "caliente"
        else:
            return "muy_caliente"
    def agrupar_por_categoria(self, *temperaturas):
        self.temperaturas = {
            "fria": [],
            "templada": [],
            "caliente": [],
            "muy_caliente": []
        }
        for temperatura in temperaturas:
            categoria = self.clasificar_temperatura(temperatura)
            self.temperaturas[categoria].append(temperatura)
        return self.temperaturas
    def promedio_categoria(self, categoria):
        valores=self.temperaturas.get(categoria, [])
        if len(valores)==0:
            return 0
        return sum(valores)/len(valores)
x = AgrupadorTemperaturas()
print(x.agrupar_por_categoria(10, 20, 30, 40, 12, 28))
print(x.promedio_categoria("caliente"))
