from math import log
num = int(input('Informe um número inteiro: '))

if num < 0:
    print('Número inválido!!')
else:
    num = log(num)
    print(f'O logaritimo do numero é: {num}')
