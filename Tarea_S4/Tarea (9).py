class AnalizadorString:
    def __init__(self):
        self.string=""
    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"
    def contar_por_tipo(self, texto):
        conteo = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }
        for letra in texto:
            if letra.isdigit():
                conteo["digitos"]+=1
            elif letra.isalpha():
                if self.solo_vocales(letra):
                    conteo["vocales"]+=1
                else:
                    conteo["consonantes"]+=1
        self.string=texto
        return conteo

analizador=AnalizadorString()
print(analizador.contar_por_tipo("Pruebadetexto13123123"))