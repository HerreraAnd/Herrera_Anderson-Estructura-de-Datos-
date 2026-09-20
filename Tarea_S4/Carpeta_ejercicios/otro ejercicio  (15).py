#Ejercicio: Analizador de números
class AnalizadorNumeros:
    def encontrar_pares(self, numero):
        resultado =[]
        for numero_actual in range(1, numero+1):
            if numero_actual%2== 0:
                resultado.append(numero_actual)
        return tuple(resultado)
    def es_par(self, numero):
        if numero%2== 0:
            return True
        else:
            return False
    def analizar_multiples(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_pares(numero)
        return resultado
x = AnalizadorNumeros()
print(x.encontrar_pares(10))
print(x.es_par(8))
print(x.analizar_multiples(5, 8, 10))
