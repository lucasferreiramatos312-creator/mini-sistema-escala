from enum import Enum

class EstadoFuncionario(Enum):
    NORMAL = 1
    ALERTA = 2
    BLOQUEADO = 3

    def __str__(self):
        return self.name.replace("_", " ").lower().title()