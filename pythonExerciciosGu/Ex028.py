import random
aleatorio = random.randint(0, 5)
num = int(input('Tente acertar o numero sorteado entre 0 e 5: '))

if num == aleatorio:
    print(f'Meus parabéns, você acertou o número {aleatorio}')
else:
    print(f'Você errou, que pena! O número era {aleatorio}')
print('Obrigado por participar!')
