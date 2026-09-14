class Tareas:
    def __init__(self):
        self.lista_tareas=[]
    def agregar_tarea(self, descripcion, prioridad):
        tarea = (descripcion, prioridad)
        self.lista_tareas.append(tarea)
    def tareas_prioritarias(self):
        tareas_mayores=[]
        for tarea in self.lista_tareas:
            if tarea[1]=="alta":
                tareas_mayores.append(tarea)
        return tareas_mayores
    def eliminar_completas(self, descripcion):
        for tarea in self.lista_tareas:
            if tarea[0] ==descripcion:
                self.lista_tareas.remove(tarea)
                break

tareas=Tareas()
tareas.agregar_tarea("estudiar", "alta")
tareas.agregar_tarea("leer", "baja")
print(tareas.tareas_prioritarias())

tareas.eliminar_completas("Estudiar")
print(tareas.lista_tareas)