# Dicionários

elemento = {
    'Z': 3,
    'nome': 'Litío',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534,
    'obs' : {
        'a' : 1,
        'b' : {
            'b1': 'a',
            'b2': 'b'
        }
    }
}

print(elemento)
print(f'Elemento: {elemento["nome"]}')
print(f'Tamanho: {len(elemento)}')
print(f'Elemento: {elemento["grupo"]}')
elemento['grupo'] = "Alcaninos"
print(f'Elemento: {elemento["grupo"]}')
elemento['periodo'] = 1
print(elemento)
print(elemento['obs']['b'])
elemento.clear()
print(elemento)