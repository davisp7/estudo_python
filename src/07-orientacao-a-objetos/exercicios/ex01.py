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
