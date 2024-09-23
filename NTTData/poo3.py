#encapsulamento

class Conta:
    def __init__(self, agencia, saldo = 0):
        self._saldo = saldo
        self.agencia = agencia

    def depositar(self, valor):
        self._saldo +=valor

    def sacar(self, valor):
        self._saldo -=valor

    def ver_saldo(self):
        return self._saldo

c1 = Conta("001", 100)
c1.depositar(100)
print(c1.agencia)
print(c1.ver_saldo())

#propeties

#exemplo1
print("\n1-Propeties\n")
class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = -1
    
foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)

#exemplo2
print("\n2-Propeties\n")

class Pessoa:
    def __init__(self, nome, ano_nasc):
        self._nome = nome
        self._ano_nasc = ano_nasc

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nasc
    
p1 = Pessoa("Clara", 1996 )
print(f"Nome: {p1.nome} \tIdade: {p1.idade}")