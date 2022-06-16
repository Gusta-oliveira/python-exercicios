l1 = float(input('Entre com um lado: '))
l2 = float(input('Entre com outro lado: '))
l3 = float(input('Entre com outro lado: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Os lados informados formam um TRIÂNGULO! ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')

else:
    print('Com os lados informados não é possivel criar um triângulo!')
