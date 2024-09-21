'''João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um progama onde joão informe:
cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos
'''

class Bicicleta:
    #construtor
    def __init__(self, cor, modelo, ano, valor):
        #atributos
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    #métodos
    def Buzinar(self):
        print('foooommmm')

    def Parar(self):
        print(f'A bicicleta {self.modelo} parou')

    def Correr(self):
        print (f'A bicicleta {self.modelo} corre muito')

    def __str__ (self):
        return f"Bicicleta: A cor={self.cor}\nO modelo={self.modelo}\nO ano: {self.ano}\nO valor: {self.valor}"
    
    #Faz a mesma coisa do método anterior só que de forma dinâmica
    def __str__ (self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave} = {valor}' for chave, valor in self. 
                                               __dict__.items()])}"
      

bicicleta1 = Bicicleta('rosa', 'caloi', 2015, 600)
bicicleta1.Buzinar()
bicicleta1.Parar()
bicicleta1.Correr()

print(bicicleta1.cor, bicicleta1.modelo, bicicleta1.ano, bicicleta1.valor)
print(bicicleta1)