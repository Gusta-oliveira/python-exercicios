lado1 = int(input('Digite um valor inteiro para o cálculo: '))
lado2 = int(input('Digite um outro valor inteiro para o cálculo: '))
lado3 = int(input('Difite um outro valor inteiro para o cálculo: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print('\nExiste um triangulo com essas três retas!')
else:
    print('\nNão há como existir um triangulo com essas três retas!')
