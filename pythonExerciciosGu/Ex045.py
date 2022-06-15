from random import choice
from time import sleep
escolha = str(input("""Digite sua escolha:
[1]Pedra
[2]Papel
[3]Tesoura
""")).strip().upper()
mac = ['pedra', 'papel', 'tesoura']
esc = choice(mac)
print('Pedra, Papel, Tesoura')
sleep(2)

# Testando condição de escolha ser Pedra
if escolha == 'PEDRA' and escolha == esc.upper():
    print('A máquina escolheu Pedra e vocês emparatam, muito bem!')
elif escolha != esc and escolha == 'PEDRA' and esc == 'papel':
    print('Que pena, a máquina escolheu Papel e você perdeu!')
elif escolha != esc and escolha == 'PEDRA' and esc == 'tesoura':
    print('Meus Parabéns, a máquina escolheu Tesoura, você foi o vencedor!')

# Testando condição de escolha ser Papel
if escolha == 'PAPEL' and escolha == esc.upper():
    print('A maquina escolheu Papel e vocês emparataram, muito bem!')
elif escolha != esc and escolha == 'PAPEL' and esc == 'pedra':
    print('Meus parabéns, a máquina escolheu Pedra e você ganhou!')
elif escolha != esc and escolha == 'PAPEL' and esc == 'tesoura':
    print('Que pena, a máquina escolheu Tesoura e você perdeu!')

# Testando condição de escolha ser Tesoura
if escolha == 'TESOURA' and escolha == esc.upper():
    print('A máquina escolheu Tesoura e vocês empataram, muito bem!')
elif escolha != esc and escolha == 'TESOURA' and esc == 'papel':
    print('Meus parabéns, a máquina escolheu Papel e você ganhou!')
elif escolha != esc and escolha == 'TESOURA' and esc == 'pedra':
    print('Que pena, a máquina escolheu Pedra e você perdeu!')
