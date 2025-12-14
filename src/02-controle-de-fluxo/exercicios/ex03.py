""" S2.A2 - Exercicio 3"""

TAMANHO = 7

codigo_identificador = input("Digite um codigo identificador")
flag = 0

if len(codigo_identificador) == TAMANHO:
    if (codigo_identificador.startswith("BR") and codigo_identificador.endswith("X")):

        meio = codigo_identificador[2:6]

        if meio.isdigit():

            if meio != "0000":
                flag = 1

if flag == 1:
    print("valido")
else:
    print("Invalido")
