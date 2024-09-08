capacidade_atual, aumento_percentual = map(int, input().split())

#TODO: Calcule a nova capacidade do disco de Mithril
capacidade_atual *= (1 + aumento_percentual / 100)
#TODO: Imprima a nova capacidade
print(int(capacidade_atual))