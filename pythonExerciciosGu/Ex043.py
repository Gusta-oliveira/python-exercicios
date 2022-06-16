alt = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
massa = peso / (alt ** 2)
print('Com o IMC em: {:.2f}'.format(massa))
if massa < 18.5:
    print('Você está abaixo do peso!')
elif massa <= 25:
    print('Você está no peso ideal!')
elif massa <= 30:
    print('Você está com sobre peso!')
elif massa <= 40:
    print('Você esta com obesidade!')
elif massa > 40:
    print('Você está como obesidade morbida!')
