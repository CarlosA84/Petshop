class Cliente:
    def __init__(self, nome: str, cpf: str):
        self._nome = nome
        self._cpf = self._validar_cpf(cpf)  # Valida durante a criação

    # Validação do CPF (11 dígitos numéricos)
    def _validar_cpf(self, cpf: str) -> str:
        cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos
        if len(cpf) != 11:
            raise ValueError("CPF deve conter exatamente 11 dígitos numéricos")
        return cpf

    # Encapsulamento
    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str):
        self._nome = nome

    def get_cpf(self) -> str:
        return self._cpf

    def set_cpf(self, cpf: str):
        self._cpf = self._validar_cpf(cpf)  # Revalida ao alterar

    def __str__(self) -> str:
        return f"{self._nome} (CPF: {self._formatar_cpf(self._cpf)})"

    # Formatação do CPF (XXX.XXX.XXX-XX)
    def _formatar_cpf(self, cpf: str) -> str:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"