# Tabela Verdade
# x = 1 e  y = 1
# x = 1 e y = 1, True
# x = 1 e y = 3, False
# x = 2 e y = 1, False
# x = 2 e y = 3, False


idade = 49
altura = 1.69
resultado = (idade >= 18) and (altura >= 1.70)
msg = 'Pode participar deste evento :'  + str(resultado)
print(msg)