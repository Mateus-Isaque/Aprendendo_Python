# Exemplo 4: Somar 10 números digitados pelo usuário

soma = 0

for cont in range(10): # inicio = 0 e fim = 9
    num = int(input('Digite um número inteiro para somar: '))
    soma += num

print(f'A soma dos 10 números é {soma}')