from datetime import date
from time import sleep
ano = int(input('Digite um ano para análise: '))
print('Análisando...')
sleep(3)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
