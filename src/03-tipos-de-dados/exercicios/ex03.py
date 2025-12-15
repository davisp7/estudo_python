meses = {
    1: 'janeiro',
    2: 'fevereiro',
    3: 'marco',
    4: 'abril',
    5: 'maio',
    6: 'junho',
    7: 'julho',
    8: 'agosto',
    9: 'setembro',
    10: 'outubro',
    11: 'novembro',
    12: 'dezembro'
}

n = int(input("Digite um numero correspondente ao meses do ano: "))

if n in meses:
    print(meses[n])
else:
    print("valor invalido")
