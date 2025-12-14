""" S2.A2 - Exercicio 3"""

TAMANHO = 7
erro = []
codigo_identificador = input("Digite um codigo identificador ")

if len(codigo_identificador) == TAMANHO:
    if (codigo_identificador[0] == 'B' and codigo_identificador[1] == 'R'):
        print('')
    else:
        erro.append("O identificador não inicia com a sequência BR")

    meio = codigo_identificador[2:6]

    if meio.isdigit():

        if meio == "0000":
            erro.append(
                "O identificador não apresenta número inteiro entre 0001 e 9999 ")

    else:
        erro.append(
            "O identificador não apresenta número inteiro entre 0001 e 9999 ")

    if codigo_identificador[6] == 'X':
        print("valido")
    else:
        erro.append("O identificador não finaliza com o caractere X.")

    if len(erro) == 0:
        print("valido")
    else:
        print("invalido, erros encontrados:")
        print(erro)
else:
    print("invalido")
