from math import sqrt
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))

h = pow(ca, 2) + pow(co, 2)
print('O valor da hipotenusa é: {}'.format(sqrt(h)))
