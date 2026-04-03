'''
Ana está desenvolvendo seu portfólio para exibir os projetos de Python que concluiu. Ela organizou uma lista com o nome de cada projeto, mas percebeu que alguns itens podem estar ausentes, aparecendo como None:
'''

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

# Solução
for projeto in projetos:
    if projeto is None:
        print('Projeto Ausente')
    else:
        print(projeto)