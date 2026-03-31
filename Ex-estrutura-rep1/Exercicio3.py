'''
Escreva um programa que calcule a soma de todos os números pares entre 1 e 20.
'''

soma = 0

for cont in range(1, 21):
    if cont % 2 == 0:
        soma += cont
print(f'a soma dos números pares é {soma}')