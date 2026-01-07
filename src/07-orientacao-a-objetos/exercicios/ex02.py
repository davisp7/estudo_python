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
