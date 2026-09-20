class Tareas:
    def __init__(self):
        self.tareas=[]
    def agregar_tareas(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))
        return self.tareas
    def tareas_prioritarias(self):
        tareas_de_prioridad={}
        for descripcion, prioridad in self.tareas:
            if prioridad=="alta":
                tareas_de_prioridad[descripcion]=prioridad
        return tareas_de_prioridad
x=Tareas()
x.agregar_tareas("Tarea", "baja")
x.agregar_tareas("Leer", "alta")
print(x.tareas_prioritarias())