# Dias trabalhado pelo encanador

diaria = 30.00
dia_t = int(input('Informe os dias trabalhados: '))

sal = diaria * dia_t
sal_liq = sal - (sal*0.08)

print(f'O valor liquido a receber é de: {sal_liq}')
