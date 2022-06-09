n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
n3 = int(input('Digite um número inteiro: '))

if n1 > n2 and n1 > n3:
    print(f'O primeiro número é o maior! {n1}')
if n1 < n2 and n1 < n3:
    print(f'O primeiro número é o menor! {n1}')
if n2 > n3 and n2 > n1:
    print(f'O segundo número é o maior! {n2}')
if n2 < n3 and n2 < n1:
    print(f'O segundo número é o menor! {n2}')
if n3 < n2 and n3 < n1:
    print(f'O terceiro número é o menor! {n3}')

if n3 > n2 and n3 > n1:
    print(f'O terceiro número é o maior! {n3}')
