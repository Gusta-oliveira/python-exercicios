num = int(input('Digite um número inteiro de 0 a 9999: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000

print(f'Unidade: {u}')
print(f'Dezena:  {d}')
print(f'Centena: {c}')
print(f'Milhar:  {m}')
