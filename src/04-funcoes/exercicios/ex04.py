def somar_varios(*args):
    total = 0
    for numero in args:
        total += numero
    return total


print(somar_varios(10, 20, 30, 40, 50))
