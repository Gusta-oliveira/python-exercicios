alt = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
massa = peso / (alt * alt)
if massa < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= massa < 25:
    print('Você está no peso ideal!')
elif 25 <= massa < 30:
    print('Você está com sobre peso!')
elif 30 <= massa < 40:
    print('Você esta com obesidade!')
elif massa > 40:
    print('Você está como obesidade morbida!')
