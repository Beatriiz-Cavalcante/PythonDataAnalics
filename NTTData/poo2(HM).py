class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__ (self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave} = {valor}' for chave, valor in self. 
                                               __dict__.items()])}"
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Cachorro(Mamifero):
    str

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, numero_patas, cor_pelo, cor_bico):
        print(Ornitorrinco.__mro__) #mro nos mostra como o python busca a informação de herança das classes
        super().__init__(cor_pelo=cor_pelo, numero_patas = numero_patas, cor_bico=cor_bico)

koda = Cachorro(numero_patas=4, cor_pelo="champagne")
print(koda)

perry = Ornitorrinco(numero_patas=2, cor_pelo='marrom', cor_bico= 'laranja')
print(perry)