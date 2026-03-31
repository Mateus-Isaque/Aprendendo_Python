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