# Exemplo 1
# num =  1
# while (num <= 10):
#     print(num)
#     num += 1
# print('Laço encerrado !!!')

# Exemplo 2
nome = None

while True:
    print('Digite o seu nome, ou x para parar: ')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem-Vindo, {nome}')
print('Até logo !!!')