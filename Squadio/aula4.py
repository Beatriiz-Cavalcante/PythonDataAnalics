#funções

#sintaxe de criação
def exibir_mensagem():
    print("Oi, cara de boi")

#sintaxe de convocação 
exibir_mensagem()    

#em parenteses se coloca o parâmetro a ser usaddo

def exibir_mensagem2(nome):
    print(f"Oi, {nome}! Seja bem vindo :)")

exibir_mensagem2(nome="Bibs")    

#atribuindo valor na criação impede que dê erro caso o valor não seja passado
def exibir_mensagem3(nome="alguem"):
    print(f"{nome}, você foi convocado.")

exibir_mensagem3()

#retornando valores
def soma(numeros):
    return sum(numeros)

print(soma([10, 20, 34]))

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero + 1
    return antecessor, sucessor

print(retorna_antecessor_e_sucessor(10))

#args e kwargs

def exibir_poema(data_extenso, *args, **kwargs):
    texto ="\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor 
                            in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sábado, 16 de março de 2024",
              "Estudando Python",
              "Com Dio e Squadio",
                carga_horaria = 68)    

#função como parâmetro de outra
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado (a, b, funcao):
    resultado = funcao(a , b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10,10, somar)    
exibir_resultado(10, 5, subtrair)    