#
sal_trab = float(input('Insira o sálario: '))
valor_prest = float(input('Informe o valor da prestação: '))

if valor_prest > (sal_trab*0.2):
    print('Emprestimo não consedido!')
else:
    print('Emprestimo concedido!')
