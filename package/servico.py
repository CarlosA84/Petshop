# servico.py

from abc import ABC, abstractmethod

class Servico(ABC):
    @abstractmethod
    def realizar_atendimento(self, animal):
        pass


class Banho(Servico):
    def realizar_atendimento(self, animal):
        print(f"[✔] Banho realizado no {animal.get_nome()}")


class Tosa(Servico):
    def realizar_atendimento(self, animal):
        print(f"[✔] Tosa realizada no {animal.get_nome()}")


class Vacina(Servico):
    def realizar_atendimento(self, animal):
        print(f"[✔] Vacinação feita no {animal.get_nome()}")


class Passeio(Servico):
    def realizar_atendimento(self, animal):
        print(f"[✔] Passeio concluído com {animal.get_nome()}")
