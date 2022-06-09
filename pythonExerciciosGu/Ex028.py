from random import randint
from time import sleep

print('-='*28)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-='*28)
aleatorio = randint(0, 5)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if num == aleatorio:
    print(f'Meus parabéns, você GANHOU o número {aleatorio}')
else:
    print(f'Você errou, que pena! O número era {aleatorio}')
print('\nObrigado por participar!')
