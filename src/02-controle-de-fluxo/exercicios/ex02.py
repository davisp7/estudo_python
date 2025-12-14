lista = input("digite as notas n1, n2, n3, nm\n").split(',')
media = 0
cont = 0
for i in lista:
    cont += 1
    media+= float(i)

media = media/cont
print(f"valor media = {media}")




