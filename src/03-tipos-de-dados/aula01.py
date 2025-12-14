"""Aula 01 - Tipos de Dados - Listas"""

# lista
# ordenadas
# mutaveis
# indexaveis

nomes = ['Maria', 'Pedro', 'Joao', 1]
print(nomes, type(nomes))
# acessar elementos
print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# modificar elementos

nomes[0] = 'Maria da Silva'
nomes[1:] = ['Pedro da Silva', 'João Santos']
print(nomes)

# tamanho de uma lista

tamanho = len(nomes)
print(tamanho)

# adicionar elementos na lista
# metodo append
nomes.append('Marta Gomes')
print(nomes)

# metodo insert

nomes.insert(0, 'Guilherme Tavares')
print(nomes)


nomes.insert(2, 'Guilherme Tavares')
print(nomes)

# metodo extend

nomes2 = ['Kaio Silva', 'Carlos Gomes']
print(len(nomes))
nomes.extend(nomes2)
print(len(nomes))
print(nomes)

# remover elementos

# metodo remove

nomes.remove('Maria da Silva')
print(nomes)

# del

del nomes[0]
print(nomes)

# remove da memoria

# del nomes
print(nomes)

# limpar a lista
# metodo clear

nomes.clear()
print(nomes)

# iteracao em lista

for nome in nomes:
    print(nome)

print('-----')

for i in range(len(nomes)):
    print(nomes[i])
