from dataclasses import dataclass

@dataclass(frozen=True)
class ResultadoTrabalhar:
    trabalhou: bool
    estado_atual: str
    dias_trabalhados: int
    deve_folgar: bool
    motivo: str | None = None