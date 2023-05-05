import requests
import json

url = 'https://api.npoint.io/c9ae384c310642b48190'

x = requests.get(url)



dicionario = {"BMT":{"week_1":{"MOB":15,"Atividades Gerais":3},"week_2":{"MOB":12,"Atividades Gerais":1}},"CDF":{"week_1":{"MOB":16,"Atividades Gerais":6},"week_2":{"MOB":14,"Atividades Gerais":2}},"FBT":{"week_1":{"C127":7,"E122":5,"Atividades Gerais":5},"week_2":{"MOB":2,"C127":6,"E122":5}},"GDP":{"week_1":{"T013":11,"W124":4,"Atividades Gerais":2},"week_2":{"T013":12,"W124":5}},"GRC":{"week_1":{"AGDP":13,"L002":8},"week_2":{"AGDP":11,"L002":6}},"GWL":{"week_1":{"E127":5,"Funil":12,"Atividades Gerais":8},"week_2":{"E127":12,"Funil":11,"Atividades Gerais":5}},"IBZ":{"week_1":{"T013":10,"W124":9,"Atividades Gerais":3},"week_2":{"T013":9,"W124":12}},"JPT":{"week_1":{"MOB":12,"Atividades Gerais":7},"week_2":{"MOB":18,"Atividades Gerais":3}},"JVM":{"week_1":{"MOB":8,"Atividades Gerais":2},"week_2":{"MOB":14,"Atividades Gerais":6}},"LBC":{"week_1":{"FIN":5,"C126":8,"Atividades Gerais":11},"week_2":{"FIN":3,"MOB":5,"C126":10}},"LGK":{"week_1":{"E127":5,"AGMKT":10},"week_2":{"E127":6,"AGMKT":8,"Atividades Gerais":2}},"LGT":{"week_1":{"C127":12,"Capacitação":10},"week_2":{"C127":10,"Capacitação":11}},"LNU":{"week_1":{"MOB":13,"Atividades Gerais":0},"week_2":{"MOB":9,"Atividades Gerais":7}},"MJL":{"week_1":{"L004":12,"Capacitação":11},"week_2":{"L004":14,"Capacitação":8,"Atividades Gerais":3}},"NLC":{"week_1":{"C126":10,"W122":6,"Processos":3},"week_2":{"C126":8,"W122":8,"Processos":3}},"VSE":{"week_1":{"E122":12,"W124":7},"week_2":{"E122":10,"W124":12}}}
horas_totais = {}


# for neoson, semanas in dicionario.items():  #accessing keys
#     print(neoson)


class Intranet:
    def __init__(self, Sigla):
       self.Sigla = Sigla
       self.nome = []
       self.NEOson = NEOson


    
    def addNEOson(self, Sigla):
        self.NEOson.__add__(Sigla)
        return f'Neoson {NEOson.Sigla} adicionado!'
    
    def __del__ (self, Sigla):
         self.sigla.remove(Sigla)
         return f'Neoson {Sigla} removido!'
    
    def __str__(self):
         return str(self.membros)
    


class NEOson:
    def __init__(self, Nome, Sigla, Projetos, Meta_de_PREP, CEP):
        self.Nome = Nome
        self.Sigla = Sigla
        self.Projetos = Projetos
        self.Meta_de_PREP = Meta_de_PREP
        self.CEP = CEP
    
    
    
    def cálculo_prep(self):
        horas_projeto = 0
        horas_totais = 0
        for semana, projetos in dicionario[input("sigla: ")].items():
            print()
            # print(semana)
            for a, b in projetos.items():
                # print(a)   
                # a, b = atividades
                s = a
                if s[0].isalpha() and len(s) == 4 and s[1].isalnum():
                    horas_projeto += b
                    # print(s, b)

            horas_totais += b


        prep = (horas_projeto) / (horas_totais) * 100
        print(f'O prep foi: {prep}%')

        if prep > self.Meta_de_PREP:
             print(f'parabéns, seu prep {prep} superou a meta de {self.Meta_de_PREP}!')
        elif prep == self.Meta_de_PREP:
             print(f'Seus prep e sua meta se igualaram em {prep}')
        elif prep < self.Meta_de_PREP:
             print(f'O seu prep {prep} ficou abaixo da sua meta {self.Meta_de_PREP}')

    # def __add__(self):
    #     if self.Horas < 20:
    #          self.Horas = self.Horas + 1 
    #             print (f'Hora extra adicionada, seu tempo total essa semana será de {self.Horas} horas')
    #     else:
    #         return 'Limite de horas extras cadastrados'


    def folga(self):
        if self.Horas > 15:
            self.Horas = self.Horas - 1
            print (f'Folga registrada, se tempo total de trabalho na semana será de {self.Horas} horas')
        else:
            return 'Limite de folgas cadastrados'




class Project(NEOson):
    def __init__(self, Nome, Sigla, Projetos, Meta_de_PREP, CEP, Horas, Equipe, Empresa):
                super().__init__(Nome, Sigla, Projetos, Meta_de_PREP, CEP, Horas)
                self.Equipe = Equipe
                self.Empresa = Empresa

        
    def addEmpresa(self):
        nova_empresa = str(input('Nome da nova EP: '))
        nova_equipe = str(input('Integrantes da equipe: '))
        return f'A {nova_empresa} foi associada a {nova_equipe} com sucesso!'
        

lnu = NEOson('Leonardo', 'LNU', 'C126', 60, 12234334 )

ibz = NEOson('Isadora', 'IBZ', ('T013', 'W124'), 40, 1234345)
print(ibz.Nome)
print(ibz.Meta_de_PREP)

NEOson.cálculo_prep(ibz)        

# lnu.info()

Intranet.addNEOson(ibz, ibz)