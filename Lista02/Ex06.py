#

print('Informe dois números: ')
num1 = int(input())
num2 = int(input())

dif = num1 - num2

if num1 > num2:
    print(f'O maior numero é: {num1} \nA diferença entre eles é: {dif}')
elif num1 == num2:
    print('Os números são iguais')
else:
    dif = dif * -1
    print(f'O maior número é: {num2} \nA diferença entre eles é: {dif}')
