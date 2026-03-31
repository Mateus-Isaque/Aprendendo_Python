# Exemplo 3: Somar os números ímpares de 4 até 100

soma_impares = 0

for cont in range(4, 101):
    if cont % 2 != 0:
        soma_impares = soma_impares + cont

print(f'A soma dos impares é {soma_impares}')