# package/agendamento.py

class Agendamento:
    def __init__(self, cliente, animal, servico, data: str):
        self.cliente = cliente
        self.animal = animal      
        self.data = data
        self.servico = servico
    def __str__(self):
        return f"{self.data} - {self.servico} para {self.animal} (Cliente: {self.cliente})"
