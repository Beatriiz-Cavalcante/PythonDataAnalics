''' 1
Você está trabalhando em um projeto de Power BI onde precisa analisar dados de vendas mensais de uma empresa. Em Power BI, os dados são frequentemente representados em tabelas, e você precisa calcular alguns indicadores básicos. Sua tarefa é calcular o total de vendas e a média mensal de vendas que serão usados para gerar relatórios e gráficos no Power BI, além de criar uma lista em Python para calcular o total de vendas e a sua média mensal.

Detalhamento:

Na função obter_entrada_vendas() você deverá:

Utilizar o método split(',') para dividir a string de entrada em elementos separados por vírgula, criando assim uma lista de strings.

Aplique a função map(int, ...) para converter cada elemento dessa lista de strings em um inteiro.

Usar a função list() para converter o objeto map resultante em uma lista de inteiros.

Essa lista de inteiros representará os valores de vendas que serão utilizados para calcular o total e a média mensal de vendas em outra função.
'''

def analise_vendas(vendas):
    # Calcule o total de vendas
    total_vendas = sum(vendas)
    # Calcule a média mensal de vendas
    media_vendas = total_vendas / len(vendas) if vendas else 0
    # Formate a saída como uma string
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("Digite as vendas separadas por vírgula: ")
    # Converta a entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split(',')))
    return vendas

# Obtém a lista de vendas do usuário
vendas = obter_entrada_vendas()
# Imprime a análise das vendas
print(analise_vendas(vendas))


'''2
Você está gerando um relatório de vendas em Power BI e deseja identificar quais produtos foram mais vendidos durante um dia específico. Os dados dos produtos vendidos são frequentemente armazenados em listas. Sua tarefa é usar uma lista em Python para contar a frequência de cada produto e determinar o produto mais vendido, que será usado para destacar produtos populares no relatório do Power BI.

Detalhamento:

Encontre o produto com a maior contagem:

Itere sobre o dicionário contagem, que contém a contagem de cada produto.

Compare a contagem atual com a contagem máxima armazenada em max_count.

Se a contagem atual for maior que max_count, atualize max_count e defina max_produto como o produto atual.

Converter a entrada em uma lista de strings, removendo espaços extras:

Use o método split(',') para dividir a string de entrada em uma lista de strings, separando pelo caractere vírgula.

Utilize uma list comprehension para remover espaços em branco extras ao redor de cada string, usando o método strip().
'''

def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
        # TODO: Encontre o produto com a maior contagem:
        if count > max_count:
          max_count = count
          max_produto = produto
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    produtos = [produto.strip() for produto in entrada.split(',')]
      
    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))