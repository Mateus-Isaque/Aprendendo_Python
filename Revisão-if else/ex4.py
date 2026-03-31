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