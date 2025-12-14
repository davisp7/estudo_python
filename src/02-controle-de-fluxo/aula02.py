""" Aula 02 - instrução if"""

# if condicao
#     instrução
#     instrução
#     instrução

# C, Java, C#, outras
# if(){
#     instrução
# }

codigo_cliente = 32
valor_desconto = 23.0
DESCONTO_ESPECIAL = valor_desconto >= 20.0

if DESCONTO_ESPECIAL:
    print('Desconto Especial')
    print(codigo_cliente)
else:
    print('Sem desconto especial')

# Nome tem que ter pelo menos 3 caracteres
nome = 'Lo'

print(len(nome), type(len(nome)))

NOME_INVALIDO = len(nome) < 3

if NOME_INVALIDO:
    print('Nome deve ter pelo menos 3 caracteres')
else:
    print('Nome válido')

NOME_VALIDO = len(nome) >= 3
if NOME_VALIDO:
    print('Nome válido')
else:
    print('Nome deve ter pelo menos 3 caracteres')

if not NOME_INVALIDO:
    print('Nome válido')
else:
    print('Nome deve ter pelo menos 3 caracteres')

# nome tem que ter pelo menos 3 caracteres
# idade tem que ser maior ou igual a 18
# exibir todos os erros no final apenas
nome = 'Lo'
idade = 18
erros = []
NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    erros.append('Nome deve ter pelo menos 3 caracteres')

IDADE_INVALIDA = idade < 18
if IDADE_INVALIDA:
    erros.append('Idade deve ser maior ou igual a 18 anos')
# False: False, None, 0, 0.0, string vazia '', lista, tuple, set vazio
# True: todo o resto
if len(erros) != 0:
    print(erros)
else:
    print('Dados válidos')

# if elif else

# Verifica se um numero é positivo ou negativo ou zero
numero = 3
# _____________ _ _________
# -N -4 -3 -2 -1 0 1 2 3 4 N
if numero > 0:
    print('Maior que zero')
elif numero == 0:
    print('zero')
else:
    print('Menor que zero')

# Calcule a media e verifique se as duas notas sao validas antes do calculo

n1 = 5.6
n2 = 10.0
NOTA1_VALIDA = 0 <= n1 <= 10.0
NOTA2_VALIDA = 0 <= n2 <= 10.0

if NOTA1_VALIDA and NOTA2_VALIDA:
    media = (n1 + n2) / 2
    if media >= 6.0:
        print('Aprovado')
    elif 4.0 <= media < 6.0:
        print('Recuperação')
    else:
        print('Reprovado')

else:
    print('Reprovado')
