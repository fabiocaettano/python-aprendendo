# # Exemplo 01
# lista = [3,6,1,8,8,9,2,3,0]
# for item in lista:
#     print(item)

# # Exexmpplo 2
# palavra = 'Corinthians'
# for letra in palavra:
#     print(letra)

# Exemplo 3
# nome = input('Digite o seu nome:')
# for x in range(4):
#     print(f'{x+1} {nome}')

# Exemplo 4
# print("Crescente:")
# for x in range(2,10,2):
#     print(x)

# print('\nDecrescente:')
# for x in range(10,2,-2):
#     print(x)

# Exemplo 5
pedras = ('Rubi','Esmeralda','Quartzo','Safira','Diamante','Turmalina')
for pedra in pedras:
    if pedra == "Quartzo":
        continue
    print(pedra)