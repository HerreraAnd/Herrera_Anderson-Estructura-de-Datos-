class Encontrador_Divisor:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)
    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = 0
        for divisor in divisores:
            if divisor != numero:
                suma += divisor
        return suma == numero
    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado
encontrador = Encontrador_Divisor()
print(encontrador.encontrar_divisores(12))
print(encontrador.es_perfecto(6))
print(encontrador.encontrar_multiples_divisores(6, 10, 12))
