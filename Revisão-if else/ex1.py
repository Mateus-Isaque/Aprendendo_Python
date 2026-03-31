horas_trabalhadas = int(input('Informe suas horas trabalhadas nesse mês: '))
salario_hora = float(input('Informe seu salario por hora: '))

if horas_trabalhadas > 160:
    horas_extras = horas_trabalhadas - 160
    salario_normal = 160 * salario_hora
    salario_extra = horas_extras * (salario_hora * 1.5)
    salario_final = salario_normal + salario_extra
else:
    salario_final = horas_trabalhadas * salario_hora

print(f'O seu salário total nesse mês é R$ {salario_final:.2f}')