from datetime import date
print('Alistamento para o Exército!!')
ano = int(input('Insira o ano de nascimento do candidato: '))
data = date.today()
idade = data.year - ano
if idade == 18:
    print('Este ano é o ano de se alistamento! Fique atento.')
elif idade < 18:
    print('Você ainda não precisa se alistar. Seu alistamento deve ser feito hein {}'.format(ano + 18))
elif idade > 18:
    print('Já passou o tempo para alistamento! O ano de alistamento foi {}'.format(ano + 18))

