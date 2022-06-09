valor = float(input('Qual o valor do produto R$'))
desc = valor - (valor * 0.05)
print('O produto custando R${:.2f} com desconto de 5% fica R${:.2f}'.format(valor, desc))
