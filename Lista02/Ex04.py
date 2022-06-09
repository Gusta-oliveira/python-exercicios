#

num = float(input('Digite um número: '))

if num > 0:
    quad = num * 2
    raiz = num ** (1/2)
    print(f'O numero digitado foi {num}! \nSeu quadrado é {quad} e sua raiz é {raiz}')
else:
    print('O número digitado é negativo!')
