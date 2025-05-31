import os
import pickle

class BancoDados:
    _ARQUIVO = "dados_agendamentos.pkl"
    
    @classmethod
    def salvar_agendamentos(cls, agendamentos):
        with open(cls._ARQUIVO, 'wb') as f:
            pickle.dump(agendamentos, f)
    
    @classmethod
    def carregar_agendamentos(cls):
        try:
            with open(cls._ARQUIVO, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []

    @classmethod
    def limpar_agendamentos(cls):
        if os.path.exists(cls._ARQUIVO):
            os.remove(cls._ARQUIVO)

class CadastroSimulado:
    _ARQUIVO = "dados_clientes.pkl"

    @classmethod
    def adicionar(cls, nome, cpf):
        clientes = cls.carregar()
        clientes.append({"nome": nome, "cpf": cpf})
        cls._salvar(clientes)

    @classmethod
    def existe_cpf(cls, cpf):
        clientes = cls.carregar()
        return any(cliente["cpf"] == cpf for cliente in clientes)

    @classmethod
    def existe_nome(cls, nome):
        clientes = cls.carregar()
        return any(cliente["nome"].lower() == nome.lower() for cliente in clientes)

    @classmethod
    def carregar(cls):
        try:
            with open(cls._ARQUIVO, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []

    @classmethod
    def _salvar(cls, clientes):
        with open(cls._ARQUIVO, 'wb') as f:
            pickle.dump(clientes, f)

    @classmethod
    def limpar_clientes(cls):
        if os.path.exists(cls._ARQUIVO):
            os.remove(cls._ARQUIVO)
