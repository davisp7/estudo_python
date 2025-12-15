""" Aula 01 - Introducao a funções """

# Funcao é um bloco que realiza uma tarefa especifica
# Dividir o problema em pequenas parte
# Evitar duplicação de codigo

# 1. standard Library Functions - built in functions
# ex: print, len

print("Olá", 123, True)

nomes = ['Joao', 'Maria']
tamanho_lista = len(nomes)
print(nomes, tamanho_lista)

# 2. User Defined Functions
# Definidas pelo desenvolver(a)
# Fazerem parte da solução do problema

# declaracao
# nome: saudacoes
# paramentros: nenhum
# retorno : nenhum


def saudacoes():
    print("olá")

# Chamada


saudacoes()
saudacoes()
saudacoes()

# declaracao
# nome: saudacoes
# paramentros: nenhum
# retorno : nenhum


def saudacoes(nome):
    print(f'Olá {nome}')


# Chamada
# valores, variaveis, expressoes => argumentos
# 'Maria' é um argumento passado para o parametro nome
saudacoes('Maria')
saudacoes('Pedro')
nome = 'Carlos'
saudacoes(nome)


def calcular_media(nota1, nota2, nota3):
    media = ((nota1 + nota2 + nota3)/3)
    print(media)


# Chamada
# argumentos literais
calcular_media(10.0, 3.0, 6.0)

n1 = 10.0
n2 = 3.0
n3 = 6.0

# argumento sao variaveis
calcular_media(n1, n2, n3)

# Declaracao
# nome: calcular_media
# parametros: nota1, nota2, nota3
# retorno: media


def calcular_media(nota1, nota2, nota3):
    media = ((nota1 + nota2 + nota3)/3)
    return media


media = calcular_media(10.0, 8.4, 3.2)

print('valor da média ', media)
