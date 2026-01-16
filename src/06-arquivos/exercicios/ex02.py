"""Exercicio 02"""

def carregar_dados_projetos(nome_arquivo):
    lista_projetos = []

    arquivo = open(nome_arquivo, 'r')

    for linha in arquivo:
        linha_limpa = linha.strip()

        if not linha_limpa:
            continue

        campos = linha_limpa.split(',')

        projeto = {
            'codigo': int(campos[0]),
            'titulo': campos[1],
            'responsavel': campos[2]
        }

        lista_projetos.append(projeto)

    arquivo.close()

    return tuple(lista_projetos)
