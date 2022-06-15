from datetime import date
print('Alistamento para o Exército!!')
sexo = str(input('Digite o sexo H/M: ')).strip().upper()

if sexo == 'M':
    print('Você é mulher e não precisa se alistar.')

if sexo == 'H':
    ano = int(input('Insira o ano de nascimento do candidato: '))
    data = date.today().year
    idade = data - ano
    print('Você nasceu em {} e tem {} anos em {}'.format(ano, idade, data))
    if idade == 18:
        print('Este é o ano de seu alistamento')
    elif idade < 18:
        print('Ainda faltam {} anos para o alistamento!'.format(18 - idade))
        print('Seu alistamento será em {}'.format(ano + 18))
    elif idade > 18:
        print('Você deveria ter se alistado há {}'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(ano + 18))
