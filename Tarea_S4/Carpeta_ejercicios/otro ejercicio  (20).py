#validador de precios
class calificador:
    def __init__(self):
        self.precios=[]
    def validar_precio(self, precio):
        if 0<precio<=10000:
            return True
        else:
            return False
    def cargar_precios(self, *args):
        for precio in args:
            if self.validar_precio(precio):
                self.precios.append(precio)
        return self.precios
    def cargar_promedio(self):
        if len(self.precios)==0:
            return 0
        return sum(self.precios)/len(self.precios)
c=calificador()
print(c.cargar_precios(500, 300, 400))
print(c.cargar_promedio())