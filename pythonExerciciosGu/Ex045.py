from random import randint
from time import sleep
jogador = int(input("""Digite sua escolha:
[0]Pedra
[1]Papel
[2]Tesoura
"""))
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('{:=^25}'.format('JO-KEN-PO'))

# Testando condição de computador ser Pedra
if computador == 0:
    if jogador == 0:
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('EMPATE!')
    elif jogador == 1:
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('Jogador GANHOU')
    elif jogador == 2:
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('Computador GANHOU!')
    else:
        print('Jogada inválida!')
# Testando condição de computador ser Papel
if computador == 1:
    if jogador == 0:
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('Computador GANHOU!')
    elif jogador == 1:
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('EMPATE!')
    elif jogador == 2:
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('Jogador GANHOU!')
    else:
        print('Jogada inválida!')

# Testando condição de computador ser Tesoura
if computador == 2:
    if jogador == 0:
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('Jogador GANHOU!')
    elif jogador == 1:
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('Computador GANHOU!')
    elif jogador == 2:
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('EMPATE!')
    else:
        print('Jogada inválida!')
print('=' * 25)

