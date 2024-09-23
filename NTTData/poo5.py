#atributos de classe e atributos de instância

class Estudande:
    escola = "Porto Digital"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
a1 = Estudande("Bea", 1)
a2 = Estudande("Triz", 2)
mostrar_valores(a1,a2)

a1.matricula = 3
mostrar_valores(a1,a2)

Estudande.escola = "Dio"
mostrar_valores(a1,a2)

#Métodos de classe e métodos estáticos
print("\nMétodos\n")

class Pessoa:
    def __init__(self, nome = None, idade= None):
        self.nome = nome
        self.idade = idade

    #método de classe
    @classmethod
    def criar_idade(cls, ano, mes, dia,nome):
        idade = 2024 - ano
        return cls(nome, idade)

    #função de classe
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    
p1 = Pessoa('Gui', 28)
print(p1.nome,p1.idade)

p2 = Pessoa.criar_idade(2001,13,11,"Bia")
print(p2.nome, p2.idade)

#estático
print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(10))

#classes abstratas e interfaces
print("\nClasses Abstratas\n")

from abc import ABC

class Controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass


class ControleTV(Controle_remoto):
    def ligar(self):
        print("Ligando a tv")

    def desligar(self):
        print("Desligando a tv")

c1 = ControleTV()
c1.ligar()
c1.desligar()