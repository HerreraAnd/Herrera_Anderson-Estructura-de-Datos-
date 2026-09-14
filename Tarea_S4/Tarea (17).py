class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}
    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 60:
            return "adulto"
        else:
            return "mayor"
    def agrupar_por_categoria(self, *edades):
        self.grupos = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            if categoria not in self.grupos:
                self.grupos[categoria] = []
            self.grupos[categoria].append(edad)
        return self.grupos
    def edad_promedio_categoria(self, categoria):
        edades = self.grupos.get(categoria, [])
        if len(edades) == 0:
            return 0
        return sum(edades) / len(edades)
edades = AgrupadorEdades()
resultado = edades.agrupar_por_categoria(5, 15, 30, 70)
print(resultado)
