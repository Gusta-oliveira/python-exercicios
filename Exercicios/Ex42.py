# Calulo sálario base funcionario

sal_base = float(input('Informe o sálario base do funcionário: '))
sal_desc = sal_base-(sal_base*0.07)
sal_grati = sal_desc+(sal_base*0.05)

print(f'O sálario a receber: {sal_grati}')
