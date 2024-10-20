email = input('Digite um email: ')

if email.count("@") == 1:
    arroba = email.find("@")
    usuario = email[0:arroba]
    dominio = email[arroba+1:]
    print(usuario)
    print(dominio)