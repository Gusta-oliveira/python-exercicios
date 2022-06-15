from datetime import date
print('-=' * 15, 'Escolha de categoria!', '=-' * 15)
ano = int(input('Insira o ano de nascimento do ATLETA: '))
idade = date.today().year - ano
if idade <= 9:
    print('O atleta está na categoria \033[34mMIRIM!\033[m')
elif idade <= 14:
    print('O atleta está na categoria \033[34mINFANTIL!\033[m')
elif idade <= 19:
    print('O atleta está na categoria \033[34mJUNIOR!\033[m')
elif idade <= 25:
    print('O atleta está na categoria \033[34mSÊNIOR!\033[m')
else:
    print('O atleta está na categoria \033[34mMASTER!\033[m')
print(idade)
