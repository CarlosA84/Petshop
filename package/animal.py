from __future__ import annotations


class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf

    def get_nome(self) -> str:
        return self.__nome

    def get_cpf(self) -> str:
        return self.__cpf

    def __str__(self):
        return f"{self.__nome} (CPF: {self.__cpf})"


class Animal:
    def __init__(self, tipo_animal: str, especie: str, idade: int, dono: Cliente):
        self.__tipo_animal = self._validar_tipo(tipo_animal)
        self.__especie = especie
        self.__idade = self._validar_idade(idade)
        self.__dono = dono

    def _validar_tipo(self, tipo: str) -> str:
        tipos_validos = ["gato", "cachorro", "hamster"]
        if tipo.lower() not in tipos_validos:
            raise ValueError(f"Tipo de animal inválido. Use: {', '.join(tipos_validos)}")
        return tipo.lower()

    def _validar_idade(self, idade: int) -> int:
        if not isinstance(idade, int) or idade < 0:
            raise ValueError("Idade deve ser um número inteiro não negativo.")
        return idade

    def get_tipo_animal(self) -> str:
        return self.__tipo_animal

    def get_especie(self) -> str:
        return self.__especie

    def get_idade(self) -> int:
        return self.__idade

    def get_dono(self) -> Cliente:
        return self.__dono

    def __str__(self) -> str:
        return (f"{self.__tipo_animal.capitalize()} ({self.__especie}, "
                f"{self.__idade} anos) - Dono: {self.__dono.get_nome()}")
