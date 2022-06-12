print('-=' * 15, 'Escolha de categoria!', '=-' * 15)
idade = int(input('Insira a idade do ATLETA: '))
if idade <= 9:
    print('O atleta está na categoria \033[34mMIRIM!\033[m')
elif 10 <= idade <= 14:
    print('O atleta está na categoria \033[34mINFANTIL!\033[m')
elif 15 <= idade <= 19:
    print('O atleta está na categoria \033[34mJUNIOR!\033[m')
elif idade == 20:
    print('O atleta está na categoria \033[34mSÊNIOR!\033[m')
else:
    print('O atleta está na categoria \033[34mMASTER!\033[m')
9
