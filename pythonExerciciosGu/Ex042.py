l1 = float(input('Entre com um lado: '))
l2 = float(input('Entre com outro lado: '))
l3 = float(input('Entre com outro lado: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Os lados informados formam um triângulo!')

if l1 == l2 == l3:
    print('Com os lados informados forma um Equilátero!')
elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
    print('Com os lados informados forma um isósceles!')
elif l1 + l2 > l3 != l2 and l2 + l3 > l1 != l3 and l1 + l3 > l2 != l1:
    print('Com os lados informados forma um Escaleno!')
else:
    print('Com os lados informados não é possivel criar um triângulo!')
