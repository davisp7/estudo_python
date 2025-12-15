""" Exercicio 2 - S2 A3"""

meses = ('janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
n = int(input("Digite um numero correspondente ao meses do ano "))

if 0 < n <= 12:
    mes_correspondente = meses[n-1]
    print(f"O mes e: {mes_correspondente}")
else:
    print("valor invalido")
