"""Aula 02 - Tipos de Dados - Tuplas"""

# tuplas
# ordenadas
# imutaveis
# indexaveis

# criacao da tupla

nomes = ('Maria', 'Pedro', 'Joao')
print(nomes, type(nomes))

# acessar os elementos

print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# modificar elementos (nao é possivel por ser imutal)

# nomes[0] = 'maria da silva'

# iteracao

for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])

nomes2 = 'Ana', 'Amelia', 'Marcos'
print(nomes2, type(nomes2))

# unpack

# nome1 = nomes2[0]
# nome2 = nomes2[1]
# nome3 = nomes2[2]

nome1, nome2, nome3 = nomes2

print(nome1, nome2, nome3)


# juntar duas tuplas

todos_nomes = nomes + nomes2
print(todos_nomes, type(todos_nomes))
