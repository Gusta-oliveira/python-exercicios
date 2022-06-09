#
num = int(input('Digite um número: '))

if num > 0:
    raiz = num ** (1/2)
    print(f'A raiz quadrada de {num} é {raiz}')
else:
    print('O número é negativo!')
