#
nome = input('Informe o nome do aluno: ')
nota1 = float(input('Informe a nota da primeira prova: '))
nota2 = float(input('Informe a nota da segunda prova: '))
nota3 = float(input('Informe a nota da terceira prova: '))

media_p = (1*nota1)+(1*nota2)+(2*nota3)/1+1+2

if media_p >= 60:
    print(f'O aluno {nome} teve {media_p} pontos! Situação APROVADO!')
else:
    print(f'O aluno {nome} teve {media_p} pontos! Situação REPROVADO!')
