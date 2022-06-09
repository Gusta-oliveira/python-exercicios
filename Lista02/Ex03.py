#
num = float(input('Insira um número qualquer: '))

if num > 0:
    raiz = num ** (1/2)
    print(f'A raiz quadrada de {num} é: {raiz}')
else:
    quad = num ** 2
    print(f'O quadrado de {num} é: {quad}')
