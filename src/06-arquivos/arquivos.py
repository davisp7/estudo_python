"""Arquivos em Python - Escrita"""

# arq = open('arquivo.txt', 'w')

# x = ['Caio\n', 'Joao\n', 'Marcos\n']
# arq.writeLines(x)

# for nome in x:
#     arq.write(nome)

# arq.close()

# with open('arquivo.txt', 'rb') as arq:
#     x = arq.read()
#     print(type(x.decode()))

with open('arquivo.txt', 'rb') as arq:
    print(next(arq))
    print(next(arq))
