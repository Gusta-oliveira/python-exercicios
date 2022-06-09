"""num = int(input('Digite um numero entre 1000 e 9000: '))
n = str(num)
print(f'Unidade {n[3]}')
print(f'Dezene  {n[2]}')
print(f'Centena {n[1]}')
print(f'Milhar  {n[0]}')
"""
num = int(input('Digite um numero até 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000

print(f'Unidade {u}')
print(f'Dezena  {d}')
print(f'Centena {c}')
print(f'Milhar  {m}')
