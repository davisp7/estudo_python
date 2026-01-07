class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    def __eq__(self, outro):
        if not isinstance(outro, Aluno):
            return False
        return self.prontuario == outro.prontuario

    def __hash__(self):
        return hash(self.prontuario)

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if not value.strip():
            raise ValueError('O prontuario nao pode estar vazio')
        if not value.isalnum():
            raise ValueError(
                'O prontuario deve conter apenas letras e numeros')
        self._prontuario = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError('o nome deve conter apenas letras')
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value or "." not in value:
            raise ValueError('o email deve conter "@" e "." ')
        self._email = value


"""Exercicio 2"""


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor:
            raise ValueError("O código não pode ser vazio.")
        self._codigo = int(valor)

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor or str(valor).strip() == "":
            raise ValueError("O título não pode ser vazio.")
        self._titulo = valor

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        if not valor or str(valor).strip() == "":
            raise ValueError("O responsável não pode ser vazio.")
        self._responsavel = valor

    @classmethod
    def de_string(cls, dados_str):
        partes = dados_str.split(',')
        if len(partes) != 3:
            raise ValueError(
                "Formato de string inválido. Use: 'codigo,titulo,responsavel'")

        codigo, titulo, responsavel = [p.strip() for p in partes]
        return cls(codigo, titulo, responsavel)

    def __eq__(self, outro):
        if not isinstance(outro, Projeto):
            return False
        return self.codigo == outro.codigo

    def __str__(self):
        return f"Projeto {self.codigo}: {self.titulo} | Responsável: {self.responsavel}"


class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim

        if not isinstance(aluno, Aluno):
            raise TypeError(
                "O atributo aluno deve ser uma instância da classe Aluno")
        if not isinstance(projeto, Projeto):
            raise TypeError(
                "O atributo projeto deve ser uma instância da classe Projeto")

        self.aluno = aluno
        self.projeto = projeto

    def __str__(self):
        return (f"Participação [{self.codigo}]\n"
                f"Período: {self.data_inicio} a {self.data_fim}\n"
                f"Aluno: {self.aluno.nome} ({self.aluno.prontuario})\n"
                f"Projeto: {self.projeto.titulo}")

    def __eq__(self, outro):
        if not isinstance(outro, Participacao):
            return False
        return self.codigo == outro.codigo
