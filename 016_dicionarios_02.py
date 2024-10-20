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

print("exemplo 1:")
for item in elemento:
    print(item)

print("exemplo 2:")
for item in elemento.items():
    print(item)

print("exemplo 3:")
for item in elemento.keys():
    print(item)

print("exemplo 4:")
for item in elemento.values():
    print(item)
