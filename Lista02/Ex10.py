#
sexo = input("Informe o sexo(H/M): ")
altura = float(input('Informe a altura: '))

if sexo == 'm' or sexo == 'h':
    sexo = chr(ord(sexo) - 32)

if sexo == 'H':
    h = (72.7 * altura) - 58
    print(f"O peso ideial para você é: {h}")
elif sexo == 'M':
    m = (62.1 * altura) - 44.7
    print(f"O peso ideal para você é: {m}")
else:
    print('Alguma informação foi digitada errada, verificar e tentar novamente!')
