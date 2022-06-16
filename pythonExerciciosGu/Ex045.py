from random import randint
from time import sleep
escolha = int(input("""Digite sua escolha:
[0]Pedra
[1]Papel
[2]Tesoura
"""))
itens = ('pedra', 'papel', 'tesoura')
esc = randint(0, 2)

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('{:=^25}'.format('JO-KEN-PO'))
print('Computador jogou {}'.format(itens[esc]))
print('Jogador jogou {}'.format(itens[escolha]))

# Testando condição de escolha ser Pedra
if escolha == 0 and escolha == esc:
    print('EMPATE!')
elif escolha != esc and escolha == 0 and esc == 1:
    print('Computador GANHOU!')
elif escolha != esc and escolha == 0 and esc == 2:
    print('Jogador GANHOU!')

# Testando condição de escolha ser Papel
if escolha == 1 and escolha == esc:
    print('EMPATE!')
elif escolha != esc and escolha == 1 and esc == 0:
    print('Jogador GANHOU!')
elif escolha != esc and escolha == 1 and esc == 2:
    print('Computador GANHOU!')
# Testando condição de escolha ser Tesoura2
if escolha == 2 and escolha == esc:
    print('EMPATE!')
elif escolha != esc and escolha == 2 and esc == 1:
    print('Jogador GANHOU!')
elif escolha != esc and escolha == 2 and esc == 0:
    print('Computador GANHOU!')
print('=' * 25)
