num = int(input('Um numero inteiro: '))
print('''Escolha uma opção: 
[1] Binário
[2] Octal
[3] Hexadecimal
''')
n = int(input('Digite a opção: '))
if n == 1:
    print('O número {} convertido em binário é {}'.format(num, bin(num)[2:]))
elif n == 2:
    print('O número {} convertido em octal é {}'.format(num, oct(num)[2:]))
elif n == 3:
    print('O número {} convertido em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida!')

