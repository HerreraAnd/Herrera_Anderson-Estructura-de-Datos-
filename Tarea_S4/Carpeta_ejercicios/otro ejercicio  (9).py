class Analizador_Strings:
    def __init__(self):
        self.texto_mas_largo=""
    def solo_vocales(self, letra):
        return letra in "AEIOUaeiou"
    def contar_por_tipo(self, texto):
        if len(texto)>len(self.texto_mas_largo):
            self.texto_mas_largo=texto
        conteo={"vocales":0, "consonantes": 0, "digitos": 0}
        for caracter in texto:
            if caracter.isdigit():
                conteo["digitos"]+=1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):
                    conteo["vocales"]+=1
                else:
                    conteo["consonantes"]+=1
        return conteo
x=Analizador_Strings()
print(x.contar_por_tipo("Prueba213124"))