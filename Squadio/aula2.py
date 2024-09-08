#Operadores aritméticos

produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_2 / produto_1)
print(produto_2 // produto_1)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

#operadores condicionais

saldo = 300
saque = 200

print(saldo > saque)
print(saque >= saldo)
print(saque <= saldo)
print(saldo == saque)
print(saldo != saque)

#operadores identidade

curso = "curso de python"
nome_curso = curso
print(curso is nome_curso)
print(curso is not nome_curso)


#operadores de associação
frutas = ["limão","uva", "laranja"]
print("laranja" in frutas)