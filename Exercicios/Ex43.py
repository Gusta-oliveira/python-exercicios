# Programa valores loja

valor_base = float(input('Informe o valor base: '))

valor_desc = valor_base - (valor_base*0.10)
valor_parcela = valor_base/3
comissao_vista = valor_desc*0.05
comissao_prazo = valor_base*0.05

print(f"Total a pagar R${valor_desc} com desconto de 10%")
print(f"Valor parcelado em 3X: R${valor_parcela}")
print(f"Comissão vendedor pagamento a vista com desconto R${comissao_vista}")
print(f"Comissao vendedor pagamento parcelado R${comissao_prazo}")
