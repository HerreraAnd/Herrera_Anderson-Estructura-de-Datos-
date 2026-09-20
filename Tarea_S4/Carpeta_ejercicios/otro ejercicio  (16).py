class TransformadorNumeros:
    def __init__(self):
        self.historial ={}
    def transformar_numero(self,numero,desplazamiento):
        resultado= (numero+desplazamiento)%10
        return resultado
    def transformar_lista(self, lista, desplazamiento):
        resultado= []
        for numero in lista:
            nuevo_numero= self.transformar_numero(numero, desplazamiento)
            resultado.append(nuevo_numero)
        self.historial[str(lista)]= resultado
        return resultado
x = TransformadorNumeros()
print(x.transformar_numero(7, 4))
print(x.transformar_lista([1, 5, 8], 3))
print(x.historial)
