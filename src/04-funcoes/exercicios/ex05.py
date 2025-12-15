def calcular_imc(individuo_funcao):
    peso = individuo_funcao['peso']
    altura = individuo_funcao['altura']
    imc = peso / (altura * altura)
    return imc


def obter_classificacao(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25.0 <= imc <= 29.9:
        return "Excesso de peso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"


def situacao_individuo(imc):
    if imc < 18.5:
        return "ganhar peso"
    elif 18.5 <= imc <= 24.9:
        return "normal"
    else:
        return "perder peso"


individuo = {
    'altura': 1.79,
    'peso': 78.5
}

imc_calculado = calcular_imc(individuo)
classificacao = obter_classificacao(imc_calculado)
situacao = situacao_individuo(imc_calculado)

print(f"Altura: {individuo['altura']}m | Peso: {individuo['peso']}kg")
print(f"IMC: {imc_calculado:.2f}")
print(f"Classificação: {classificacao}")
print(f"Situação: {situacao}")
