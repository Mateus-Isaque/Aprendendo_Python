# Exercício 03
salario = float(input('Informe seu salário: '))
total_vendas = float(input('Informe o total vendido: '))

if (total_vendas <= 5000):
    salario_bonus = salario * 1.10
    print(f'Com {total_vendas} vendas nesse mês, o seu salário é R${salario_bonus:.2f}')
else:
    salario_bonus = salario * 1.20
    print(f'Com {total_vendas} vendas nesse mês, o seu salário é R${salario_bonus:.2f}')