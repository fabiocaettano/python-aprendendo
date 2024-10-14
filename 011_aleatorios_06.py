import random

# O comando shuffle não cria uma nova lista
# ele embaralha a lista existente
L = ['fabio','michele','sophia']
random.shuffle(L)
print(f'Número escolhido: {L}')