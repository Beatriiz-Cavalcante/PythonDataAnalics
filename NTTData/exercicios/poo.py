# Exercício 1

'''
Você está desenvolvendo um sistema para gerenciar dados de vendas que serão posteriormente importados para o Power BI. 
Você tem a estrutura de duas classes, Venda e Relatorio, já definidas. Sua tarefa é implementar partes específicas do código dentro dessas classes.

Classe Venda:
    Já está definida e contém as informações sobre uma venda, como produto, quantidade e valor.

Classe Relatorio:
    Você precisa implementar o método adicionar_venda, que deve verificar se o objeto passado é uma instância da classe Venda antes de adicioná-lo à lista de vendas.
    Também, no método calcular_total_vendas, você deve calcular o total de vendas multiplicando a quantidade pelo valor de cada venda adicionada ao relatório.

Função main:
    Você deverá implementar a lógica para exibir o total de vendas utilizando o método calcular_total_vendas da classe Relatorio.
'''

class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # TODOS: Verifique se o objeto passado é uma instância da classe Venda.
        # Isso ajuda a garantir que apenas vendas válidas sejam adicionadas ao relatório.
        if isinstance(venda, Venda):
          self.vendas.append(venda)
        

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            # TODOS: Calcule o total de vendas baseado nas vendas adicionadas:
             # O cálculo deve multiplicar a quantidade pelo valor de cada venda e somar ao total.
             total += venda.quantidade * venda.valor
            
        return total


def main():
    relatorio = Relatorio()
    
    for i in range(3):
        produto = input()
        quantidade = int(input())
        valor = float(input())
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    # TODOS: Exiba o total de vendas usando o método calcular_total_vendas.
    # Utilize o método `calcular_total_vendas` da classe `Relatorio` para mostrar o total acumulado das vendas.
    print(f'Total de Vendas: {relatorio.calcular_total_vendas()}')
    

if __name__ == "__main__":
    main()


# Exercício 2

'''
Você está desenvolvendo um sistema para organizar vendas por categorias antes de gerar um relatório. O objetivo é criar uma classe Categoria que gerencie as vendas 
associadas a uma determinada categoria e calcule o total de vendas dessa categoria.

Tarefas:

Método adicionar_venda: Na classe Categoria, crie um método chamado adicionar_venda que adiciona um objeto Venda à lista de vendas da categoria.

Método total_vendas: Na classe Categoria, crie um método chamado total_vendas que calcula e retorna o total das vendas (soma do valor de todas as vendas) para essa categoria.

Na função main:

    Entrada de Dados:
    Leia o nome das categorias e, para cada categoria, leia as vendas associadas.

    Implementação: Adicione cada venda à categoria correspondente usando o método adicionar_venda.

    Exibição dos Resultados:
    Exiba o total de vendas para cada categoria.

    Implementação: Utilize o método total_vendas para calcular e exibir o total das vendas.
'''

class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    # Método para adicionar uma venda à lista de vendas
    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.vendas.append(venda)

    # Método para calcular e retornar o total das vendas
    def total_vendas(self):
        total = 0
        for venda in self.vendas:
            total += venda.valor
        return total

def main():
    categorias = []

    for i in range(2):
        nome_categoria = input()
        categoria = Categoria(nome_categoria)

        for j in range(2): 
            entrada_venda = input()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            # Adiciona a venda à categoria
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        print(f'Vendas em {categoria.nome}: {categoria.total_vendas():.1f}')

if __name__ == "__main__":
    main()
