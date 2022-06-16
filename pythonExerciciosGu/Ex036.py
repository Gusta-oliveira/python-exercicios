# Programa aprovação emprestimo bancário
sal = float(input('Insira o sálario do solicitante: R$'))
casa = float(input('Insira o valor da casa: R$'))
anos = int(input('Tempo (anos) para quitação: '))

sal_30 = sal * 30 / 100
valor_p = casa / (anos * 12)

if valor_p > sal_30:
    print('O valor das prestações excede o permitido para o salário!')
    print('Pois as prestações ficaram em R${:.2f} passando 30% do salário: R${:.2f}.'.format(valor_p, sal_30))
else:
    print('O empréstimo foi autorizado! Aproveite a aquisição!!')
    print('As prestações ficaram no valor de: R${:.2f}, pelo prazo de {} meses.'.format(valor_p, anos * 12))
