nome = str(input('Digite seu nome completo: ')).strip()

print(nome.upper())
print(nome.lower())
nome = nome.split()
n = "".join(nome)
print('Seu nome tem {} letras'.format(len(n)))
print('O primeiro nome tem {} letras'.format(len(nome[0])))
