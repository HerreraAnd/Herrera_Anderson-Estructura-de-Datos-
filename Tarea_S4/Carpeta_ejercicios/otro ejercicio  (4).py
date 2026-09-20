class Analizador_Numeros:

    def separar_pares(self, lista):
        pares = []
        for i in range(len(lista)):
            if lista[i] % 2 == 0:
                pares.append(lista[i])
        return pares

    def separar_multiples(self, *args):
        resultado = {}
        for lista in args:
            original = tuple(lista)
            pares = self.separar_pares(lista)
            resultado[original] = pares
        return resultado  # Aquí está el return que cierra el método


X = Analizador_Numeros()
print(
    X.separar_multiples([1, 2, 3, 4, 8, 9, 10], [4, 7, 8, 10, 11, 12])
)