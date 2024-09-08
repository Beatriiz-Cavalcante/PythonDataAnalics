#interpolação

#old style

nome = "Bia"
idade = 22
ano = 2001
print("Olá, %s você tem %d anos, logo nasceu %d." %(nome, idade, ano))
#s para string e d pra inteiro

#Método format (tem 4 formas de fazer a interpolação com esse método)

cidade = "Recife"
estado = "Pernambuco"
ddd = 81

print("Vocé é de {} que fica em {}. Logo o seu ddd é {}".format(cidade, estado, ddd))

print("Seu estado é {1}, logo seu ddd é {2}. Sua cidade é {0} mas isso não muda nada".format(estado, ddd, cidade))

#print("O nome do seu {animal} é {nome}".format(animal=cachorro, nome=Koda))

#f-tring

animal = "cachorro"
nome_animal = "Koda"
print(f"O nome do seu {animal} é {nome_animal}") 

# formatando strings com f string
pi = 3.14159

print(f"Valor de pi: {pi:.2f}")

print(f"Valor de pi: {pi:10.2f}") #10 nesse caso equivale a espaços
                     