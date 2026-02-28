from domain.funcionario import Funcionario

func = Funcionario(1, "Lucas", 3)

for _ in range(5):
    resultado = func.trabalhar()
    print(resultado)