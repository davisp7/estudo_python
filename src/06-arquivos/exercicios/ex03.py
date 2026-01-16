""" Exercicio 03 """

def linha_para_dict(linha, chaves):
    valores = linha.strip().split(',')
    dicionario = {}
    
    for i in range(len(chaves)):
        dicionario[chaves[i]] = valores[i]
        
    return dicionario


def carregar_dados_alunos(nome_arquivo):
    lista_alunos = []
    chaves = ['prontuario', 'nome', 'email']
    
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')
    for linha in arquivo:
        if linha.strip():
            aluno = linha_para_dict(linha, chaves)
            lista_alunos.append(aluno)
    arquivo.close()
    
    return tuple(lista_alunos)


def carregar_dados_projetos(nome_arquivo):
    lista_projetos = []
    chaves = ['codigo', 'titulo', 'responsavel']
    
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')
    for linha in arquivo:
        if linha.strip():
            projeto = linha_para_dict(linha, chaves)
            
            projeto['codigo'] = int(projeto['codigo'])
            
            lista_projetos.append(projeto)
    arquivo.close()
    
    return tuple(lista_projetos)



arq_alunos = open('alunos.txt', 'w', encoding='utf-8')
arq_alunos.write("SP000001,Maria da Silva,maria@email.com\n"
                 "SP000002,Pedro Gomes,pedro@email.com\n"
                 "SP000003,João Santos,joao@email.com")
arq_alunos.close()

arq_projetos = open('projetos.txt', 'w', encoding='utf-8')
arq_projetos.write("101,Portal do Aluno,Maria da Silva\n"
                   "102,App de Logistica,Pedro Gomes\n"
                   "103,Analise de Dados,João Santos")
arq_projetos.close()

print("--- DADOS DOS ALUNOS ---")
alunos_carregados = carregar_dados_alunos('alunos.txt')
for a in alunos_carregados:
    print(a)

print("\n--- DADOS DOS PROJETOS ---")
projetos_carregados = carregar_dados_projetos('projetos.txt')
for p in projetos_carregados:
    print(p)