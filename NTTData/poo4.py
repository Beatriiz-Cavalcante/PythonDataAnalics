#polimorfismo
#Mesmo que herança só que com a possibilidade de sobrescrever métodos

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def Voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

def plano_voo(obj):
    obj.voar()

passarinho = Pardal()
passaro = Avestruz()

plano_voo(passarinho)
plano_voo(passaro)