# Calcular e imprimir a quantia para os vencedores do concurso

n1 = input('Nome primeiro ganhador: ')
n2 = input('Nome segundo ganhador: ')
n3 = input('Nome terceiro ganhador: ')

p = 780_000.00

g1 = (p * 0.46)
g2 = (p * 0.32)
g3 = p - (g1+g2)

print(f'O Ganhador {n1} recebeu o total de: {g1}')
print(f'O Ganhador {n2} recebeu o total de: {g2}')
print(f'O Ganhador {n3} recebeu o total de: {g3}')
