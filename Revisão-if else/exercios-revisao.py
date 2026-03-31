# Exercício 01
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


# Exercício02
nome1 = input("Digite seu nome: ")
altura1 = float(input('Informe sua altura: '))
nome2 = input("Digite seu nome: ")
altura2 = float(input('Informe sua altura: '))

if (altura1 > altura2):
    print(f'A pessoa mais alta é o(a) {nome1}')
elif (altura2 > altura1):
    print(f'A pessoa mais alta é o(a) {nome2}')
else:
    print('As alturas são iguais')


# Exercício 03
salario = float(input('Informe seu salário: '))
total_vendas = float(input('Informe o total vendido: '))

if (total_vendas <= 5000):
    salario_bonus = salario * 1.10
    print(f'Com {total_vendas} vendas nesse mês, o seu salário é R${salario_bonus:.2f}')
else:
    salario_bonus = salario * 1.20
    print(f'Com {total_vendas} vendas nesse mês, o seu salário é R${salario_bonus:.2f}')


# Exercício 04
quantidade_pessoas = int(input('Quantas pessoas estão na mesa?: '))
quantidade_porcoes_fritas = int(input('Quantas porções de fritas vocês consumiram?: '))
quantidade_porcoes_pasteis = int(input('Quantas porções de pasteis vocês consumiram?: '))
quantidade_cerveja = int(input('Quantas cervejas vocês consumiram?: '))

porcoes_fritas = quantidade_porcoes_fritas * 35.00
porcoes_pasteis = quantidade_porcoes_pasteis * 25.00
cerveja = quantidade_cerveja * 18.00

valor_total = porcoes_fritas+porcoes_pasteis+cerveja
valor_pessoa = valor_total / quantidade_pessoas

print(f'O valor total do seu consumo foi de R${valor_total:.2f}. Divido em {quantidade_pessoas} pessoas, ficou R${valor_pessoa:.2f} para cada pessoa.')


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