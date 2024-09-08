print("hello world!")


#Conversão de tipos

#Float para inteiro 
preco = 10.30
preco = int(preco)
print(preco)

#Numérico para string

data = 2001
idade = 22

print(str(data))
print(str(preco))

print(f"Nasceu em {data}, logo, tem {idade} anos") #exemplo de concatenação str e int


#String para número 
valor="10.50"

print(float(valor))

#Funções de entrada e saída
nome = input("Informe o seu nome: ")
signo = input("Qual o seu signo: ")
print(f"Seu nome é {nome} e seu signo é {signo}")
