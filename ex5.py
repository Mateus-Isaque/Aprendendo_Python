# Exercício 05
nome = input('Digite seu nome: ')
salario = float(input('Informe seu salário: '))

if (salario <= 1100.00):
    desc_INSS = salario * 0.075
elif (salario > 1100.00 and salario <= 2203.48):
    desc_INSS = salario * 0.09
elif (salario > 2203.48 and salario <= 3305.22):
    desc_INSS = salario * 0.12
elif (salario > 3305.22 and salario <= 6433.57):
    desc_INSS = salario * 0.14

print(f'O desconto do INSS é R${desc_INSS:.2f}')