'''
Faça um programa que receba 5 números inteiros e mostre se ele é par ou ímpar, um a um. Ou seja, conforme o usuário digita o número seu programa deverá informar se o número digitado é par ou ímpar.
'''

for cont in range(5):
    num1 = int(input('Digite um número: '))
    if num1 % 2 == 0:
        print('O número é Par!')
    else:
        print('O número é Ímpar!')