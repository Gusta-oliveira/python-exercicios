print('-=' * 8, 'Cálculo de média!', '=-' * 8)
nome = str(input('Nome do aluno: ')).strip().title()
média1 = float(input('Média 1 do aluno: '))
média2 = float(input('Média 2 do alino: '))
mf = (média1 + média2) / 2
if mf < 5.0:
    print('O aluno \033[34m{}\033[m está \033[31mREPROVADO!!!\033[m Sua média foi \033[31m{:.1f}\033[m'.format(nome, mf))
elif 5.0 <= mf < 6.9:
    print('O aluno \033[34m{}\033[m está de \033[33mRECUPERAÇÃO!!!\033[m Sua média foi \033[33m{:.1f}\033[m'.format(nome, mf))
elif mf >= 7:
    print('O aluno \033[34m{}\033[m está \033[32mAPROVADO!!!\033[m Sua média foi \033[32m{:.1f}\033[m'.format(nome, mf))
print('-=' * 11, 'Fim', '=-' * 12)
