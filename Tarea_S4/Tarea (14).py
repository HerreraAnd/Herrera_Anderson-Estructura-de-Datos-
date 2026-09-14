class Registro_notas:
    def __init__(self):
        self.notas={}
    def registrar(self, estudiantes, nota):
        self.notas[estudiantes]=nota
    def estudiantes_apr(self, nota_minima):
        aprobados=[]
        for estudiante, nota in self.notas.items():
            if nota>=nota_minima:
                aprobados.append(estudiante)
            return aprobados
    def mejor_estudiante(self):
        self.mejor_nombre=None
        self.mejor_nota=None
        for estudiante, nota in self.notas.items():
            if self.mejor_nota is None or nota>self.mejor_nota:
                mejor_nombre=estudiante
                mejor_nota=nota
        return (mejor_nombre, mejor_nota)

registro=Registro_notas()
registro.registrar("Ana", 80)
registro.registrar("Ana", 80)
print(registro.mejor_estudiante)