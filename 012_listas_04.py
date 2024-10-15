# Exercicio
# Criem um script que peça para o usuário digitar o nome
# de 5 bebidas favoritas dele, armazenando esses valores 
# em uma lista.
# Na sequencia, exiba na tela os elementos da lista em 
# ordem alfabética, um por linha, usando um laço de repetição for
pergunta = 1
bebidas = []

while pergunta <=5:
    bebida = input('Digite o nome da bebida:')
    bebidas.append(bebida)
    pergunta = pergunta + 1

bebidas_ordenadas = sorted(bebidas)

for bebida in bebidas_ordenadas:
    print(bebida)
