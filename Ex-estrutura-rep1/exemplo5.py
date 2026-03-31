# Exemplo 5: Calcular e exibir as medias de 3 avaliações para 5 alunos

for cont in range(5):
    av1 = float(input('Digite a nota da primeira avalição: '))
    av2 = float(input('Digite a nota da segunda avalição: '))
    av3 = float(input('Digite a nota da terceira avalição: '))
    media = (av1 + av2 + av3) / 3
    print(f'A media do aluno é {media:.2f}')