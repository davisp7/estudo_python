def calcular_volume(dados):
    return (dados['comprimento'] * dados['altura'] * dados['largura']) / 1000


def calcular_potencia_termostato(volume, dados):
    return volume * 0.05 * (dados['temp_desejada'] - dados['temp_ambiente'])


def calcular_filtragem(volume):
    minimo = volume * 2
    maximo = volume * 3
    return minimo, maximo


print("Dados do Aquário")
comprimento = float(input("Digite o comprimento (cm): "))
altura = float(input("Digite a altura (cm): "))
largura = float(input("Digite a largura (cm): "))
temp_desejada = float(input("Digite a temperatura desejada: "))
temp_ambiente = float(input("Digite a temperatura ambiente: "))

aquario = {
    'comprimento': comprimento,
    'altura': altura,
    'largura': largura,
    'temp_desejada': temp_desejada,
    'temp_ambiente': temp_ambiente
}

volume_litros = calcular_volume(aquario)
potencia_watts = calcular_potencia_termostato(volume_litros, aquario)
filtragem_min, filtragem_max = calcular_filtragem(volume_litros)

print(f"Volume do aquário: {volume_litros:.2f} litros")
print(f"Potência do termostato: {potencia_watts:.2f} W")
print(
    f"Filtragem recomendada: de {filtragem_min:.2f} a {filtragem_max:.2f} L/h")
