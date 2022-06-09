#
print('Digite as informações pedidas!')
nome = input('Informe o nome do aluno: ')
print('Notas validas de 0 à 10!!')
trab_lab = float(input('Nota do Trabalho de Laboratório: '))
av_semestre = float(input('Nota da Avaliação Semestral: '))
exame_final = float(input('Nota do Exame Final: '))

media_final = (trab_lab*0.2) + (av_semestre*0.3) + (exame_final*0.5)

if media_final <= 2.9:
    print(f'A média final do aluno {nome} foi de: {media_final}! \n Situação: Reprovado!')
elif 2.9 < media_final <= 4.9:
    print(f'A média final do aluno {nome} foi de: {media_final}! \n Situação: Recuperação!')
elif 5 <= media_final <= 10:
    print(f'A média final do aluno {nome} foi de: {media_final}! \n Situação: Aprovado!')
else:
    print('Alguma informação incoêrente, favor verificar!')
