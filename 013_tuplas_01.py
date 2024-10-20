# tuplas são imutáveis

halogenios = ('F','C1','Br','I','At')
gases_nobres = ('He','Ne','Ar','Xe','Kr','Rn')
elementos = halogenios + gases_nobres

# exibindo as informações da tupla
print(elementos)

# tentando alterar o indice zero da tuplo, vai gerar uma execeção
# print(elementos[0])
# elementos[0] = 'T'

# tamanho da tupla
# print(len(elementos))

for elemento in elementos:
    print(f'Elemento qumico: {elemento}')