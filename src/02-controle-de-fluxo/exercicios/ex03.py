""" S2.A2 - Exercicio 3"""

TAMANHO = 7

codigo_identificador = input("Digite um codigo identificador ")

if len(codigo_identificador) == TAMANHO:
    if (codigo_identificador[0] == 'B' and codigo_identificador[1] == 'R'):

        meio = codigo_identificador[2:5]

        if meio.isdigit():

            if meio == "0000":
                print("invalido")

        if codigo_identificador[6] == 'X':
            print("valido")
        else:
            print("Invalido")
    else:
        print("invalido")
