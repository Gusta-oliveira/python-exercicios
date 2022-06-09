sal = float(input('Insira o sálario: '))
if sal > 1250:
    sal = sal + (sal * 0.1)
    print('O seu novo sálario é de R${:.2f}'.format(sal))
else:
    sal = sal + (sal * 0.15)
    print('O seu novo sálario é de R${:.2f}'.format(sal))
