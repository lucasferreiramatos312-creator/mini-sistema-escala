from .estado_funcionario import EstadoFuncionario
from .resultado_trabalhar import ResultadoTrabalhar


class Funcionario:
    def __init__(self, id, nome, limite_dias):
        if limite_dias <= 0:
            raise ValueError("limite_dias deve ser maior que zero")

        self.id = id
        self.nome = nome
        self._limite_dias = limite_dias
        self._dias_trabalhados = 0

    @property
    def dias_trabalhados(self):
        return self._dias_trabalhados

    def _calcular_estado(self):
        if self._dias_trabalhados < self._limite_dias:
            return EstadoFuncionario.NORMAL
        elif self._dias_trabalhados == self._limite_dias:
            return EstadoFuncionario.ALERTA
        else:
            return EstadoFuncionario.BLOQUEADO

    def trabalhar(self):
        estado_atual = self._calcular_estado()

        if estado_atual == EstadoFuncionario.BLOQUEADO:
            return ResultadoTrabalhar(
                trabalhou=False,
                estado_atual=str(estado_atual),
                dias_trabalhados=self._dias_trabalhados,
                deve_folgar=True,
                motivo="Limite atingido"
            )

        self._dias_trabalhados += 1
        novo_estado = self._calcular_estado()

        return ResultadoTrabalhar(
            trabalhou=True,
            estado_atual=str(novo_estado),
            dias_trabalhados=self._dias_trabalhados,
            deve_folgar=novo_estado == EstadoFuncionario.BLOQUEADO,
            motivo=None
        )