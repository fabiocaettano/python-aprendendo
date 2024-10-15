# Exemplo 1
# notas = [5,6,7]
# print(notas)

# Exemplo 2
# concatenar duas lista
notas1 = [1,3,5,7]
notas2 = [2,4,5,6]
valores = notas1 + notas2
print(valores)
# imprimir posição
print(valores[1])
# imprimir ultimo item da lista
print(valores[-1])
# alterar o indice zero
print(valores)
valores[0] = 9
print(valores)
# imprimir duas posições a partir do indice zero
print(valores[0:2])
print(valores[0:])
print(valores[:4])
print(valores[3:4])
# imprimir tamanho da lista
print(len(valores))

# ordenar a lista de forma crescente
print(sorted(valores))

#  ordernar a lista de forma decrescent
print(sorted(valores,reverse=True))

# operações matemáticas
print(sum(valores))
print(min(valores))
print(max(valores))

# adicionar na lista
valores.append(13)
print(valores)

# remover ultimo item da lista
valores.pop()
print(valores)

# imprimir pelo indice
valores.pop(3)
print(valores)

# inserir no indice definido
valores.insert(2,21)
print(valores)

# localizar na listas
print(21 in valores)
