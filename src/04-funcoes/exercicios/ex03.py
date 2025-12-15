def somar_elementos(numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


minha_tupla = (10, 20, 30, 5)
resultado = somar_elementos(minha_tupla)

print(resultado)
