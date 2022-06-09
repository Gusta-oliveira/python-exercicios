#
num = input('Insira um número inteiro: ')


if int(num) >= 0:
    print(sum(int(i) for i in num))

else:
    print('Número inválido!')

# Metodo sum() usado para soma de uma tupla
