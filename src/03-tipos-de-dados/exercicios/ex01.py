""" Exercicio 1 - S2-A3 """

numeros = []

for i in range(3):
    n = int(input("Digite um numero "))

    numeros.append(n)


print("Maior ", max(numeros))
print("Menor ", min(numeros))
