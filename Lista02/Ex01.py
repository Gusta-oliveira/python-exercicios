#
num1 = int(input('Entre com um número: '))
num2 = int(input('Entre com mais um número: '))

if num1 > num2:
    print(f"O primeiro numero é maior {num1}")
elif num1 == num2:
    print(f'Os numeros são iguais')
else:
    print(f'O segundo numero é maior {num2}')
