sal = float(input('Insira o sálario: R$'))
if sal > 1250:
    sal = sal + (sal * 0.1)
else:
    sal = sal + (sal * 0.15)
print('O seu novo sálario é de R${:.2f}'.format(sal))
