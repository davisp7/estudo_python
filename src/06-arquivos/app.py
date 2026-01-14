# open("caminho", "r")

# Mode
# r - Leitura
# a - Append / incrementar
# w - Escrita
# x - Criar arquivo
# r+ - Leitura + escrita

arquivo = open("test2.txt", "a")

# print(arquivo.readable())
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# lista = arquivo.readlines()

# print(lista)

# print(lista[3])

# arquivo.write("\nSQL")
arquivo.write("C\n")
arquivo.write("C++\n")
arquivo.write("TerraForm\n")


arquivo.close()

import os

if os.path.exists("test2.txt"):
    os.remove("test2.txt")
else:
    print("O arquivo não existe")

os.rmdir("nova_pasta")