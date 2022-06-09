# Valor hora trabalhada

vh = float(input('Informe o valor por hora trabalhada: '))
hm = float(input('Informe a quantidade de horas trabalhadas: '))

sal = vh * hm
sal = sal+(sal*0.10)

print(f"O valor a receber no mês é: {sal}")
