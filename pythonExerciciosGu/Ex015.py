dias = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('Quantos Km foram percurridos: '))

dias_p = dias * 60
km_p = km * 0.15
total = km_p + dias_p

print('O carro foi alugado por {} dias e andou {}km'.format(dias, km))
print('O valor do aluguel dia do carro é R${:.2f} e por Km rodados é R${:.2f}'.format(dias_p, km_p))
print('O total a pagar é R${:.2f}'.format(total))
