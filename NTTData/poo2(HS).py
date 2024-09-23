# herança simples

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando o motor')


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self,  cor, placa, numero_rodas, carga):
        # o método super é usado para chamar a implementação da classe base
        super().__init__(cor, placa, numero_rodas)
        self.carga = carga

    def verifica_carga(self):
        print(f"{'Sim' if self.carga else 'Não'} estou carregado")

    def __str__(self):
        return self.cor

moto = Motocicleta('preta', 'bla12', 2)
moto.ligar_motor()

carro = Carro('Cinza', 'blu098', 4)
carro.ligar_motor()

caminhao = Caminhao('branco', 'pipi786', 8, False)
caminhao.ligar_motor()
caminhao.verifica_carga()
print(caminhao)