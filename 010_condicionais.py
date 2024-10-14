# Simples, Composto e Encadeado
media = n1 = n2 = 0

n1 = int(input('Digite a nota 1: '))
n2 = int(input('Digite a nota 2: '))

media = (n1 + n2) / 2

if (media >= 7):
    print('Resultado: Aprovaddo')
    print('Parabéns')
elif (media >= 5):
    print('Você está de recuperação ...')
else:
    print('Aluno reprovado ...')

print('Sua méddia {}'.format(media))
