# Tabela Verdade
# x = 1 e y = 1
# x = 1 or y = 1, True
# x = 1 or y = 3, True
# x = 2 or y = 1, True
# x = 2 e y = 3, False

porta = 'f'
janela = 'a'
alarme = (porta == 'a') or (janela == 'a')
msg = ' alarme disparado ? ' + str(alarme)
print(msg)
