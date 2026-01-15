"""Exercício 01"""

conteudo = (
    "SP000001,Maria da Silva,maria@email.com\n"
    "SP000002,Pedro Gomes,pedro@email.com\n"
    "SP000003,João Santos,joao@email.com"
)

arquivo = open('alunos.txt', 'w')
arquivo.write(conteudo)
arquivo.close()


def carregar_dados_alunos(alunos):

    lista_alunos = []

    arquivo = open('alunos.txt', 'r')

    for linha in arquivo:

        linha_limpa = linha.strip()

        if linha_limpa == "":
            continue

        campos = linha_limpa.split(',')

        aluno = {
            'prontuario': campos[0],
            'nome': campos[1],
            'email': campos[2]
        }

        lista_alunos.append(aluno)

    arquivo.close()

    return tuple(lista_alunos)


dados = carregar_dados_alunos('alunos.txt')
print(dados)
