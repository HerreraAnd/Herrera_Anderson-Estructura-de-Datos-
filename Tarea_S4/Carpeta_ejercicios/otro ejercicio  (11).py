class contador_votos:
    def __init__(self):
        self.votos={}
    def registrar_votos(self, candidato):
        if candidato in self.votos:
            self.votos[candidato]+=1
        else:
            self.votos[candidato]=1
    def candidato_mas_votado(self):
        candidato_con_mas_votos=None
        mayor_votos=0
        for candidato, votos in self.votos.items():
            if votos >  mayor_votos:
                mayor_votos=votos
                candidato_con_mas_votos=candidato
        return candidato_con_mas_votos
    def votos_candidato(self, candidato):
        return self.votos.get(candidato, 0)

x=contador_votos()
x.registrar_votos("Juan")
x.registrar_votos("Juan")
x.registrar_votos("Juan")
x.registrar_votos("Carlos")
x.registrar_votos("Carlos")
print(x.candidato_mas_votado())
print(x.votos_candidato("Juan"))
print(x.votos_candidato("Carlos"))