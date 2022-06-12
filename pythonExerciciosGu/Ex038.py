print('Digite dois números para comparação!!')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O primeiro número digitado {n1} é maior ')
elif n2 > n1:
    print(f'O segundo número digitado {n2} é maior ')
else:
    print('Os números são iguais!')