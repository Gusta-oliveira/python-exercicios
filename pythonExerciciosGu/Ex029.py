vel = float(input('Qual a velocidade do carro?: '))
if vel > 80:
    multa = 7 * (vel - 80)
    print('Você estava a mais de 80 e por isso foi multado')
    print('O valor a pagar na multa é: R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
