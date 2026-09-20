
##Ej. 4 — Básico — Agenda de contactos
class Agenda:
    def __init__(self):
        self.contactos={}
    def agregar_contactos(self, nombre, numero):
        self.contactos[nombre]=numero
    def buscar_contactos(self, nombre):
        return self.contactos[nombre]
    def contactos_por_prefijo(self, prefijo):
        lista=[]
        for nombre, numero in self.contactos.items():
            if numero.startswith(prefijo):
                lista.append(nombre)
        return lista
C=Agenda()
C.agregar_contactos("Nombre_1", "953301942")
C.agregar_contactos("Nombre_2", "312312312312")
print(C.contactos_por_prefijo("9"))