# Lista para armazenar os itens
itens = []

#TODO: Solicite os itens ao usuário
for i in range(3):
    item = input()
    itens.append(item)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")