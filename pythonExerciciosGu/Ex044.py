produto = float(input('Valor do produto: R$'))
op = int(input("""Selecione a forma de pagamento:
[1] À vista Dinheiro'
[2] À vista Cartão'
[3] 2x cartão'
[4] 3x + no cartão
"""))
if op == 1:
    produto_desc = produto - (produto * 10 / 100)
    print("""Com o pagamento à vista no dinheiro, ganha-se 10% de desconto
O produto de R${:.2f} passa a ser R${:.2f}""".format(produto, produto_desc))
elif op == 2:
    produto_desc = produto - (produto * 5 / 100)
    print("""Com o pagamento à vista no cartão, ganha-se 5% de desconto
O produto de R${:.2f}, passa a ser R${:.2f}""".format(produto, produto_desc))
elif op == 3:
    p = produto / 2
    print('O produto foi parcelado em 2x sem juros!\nO produto foi parcelado em 2x, cada parcela fica R${:.2f}'.format(p))
elif op == 4:
    parcelas = int(input('Quantas vezes: '))
    produto_ac = produto + (produto * 20 / 100)
    p = produto_ac / parcelas
    print("""Com o parcelamento em 3x ou mais o valor acrescenta 20% de juros!
O Produto de R${:.2f}, passa a ser R${:.2f}
O produto foi parcelado em {}x, ficando cada parcaela em R${:.2f}""".format(produto, produto_ac, parcelas, p))
