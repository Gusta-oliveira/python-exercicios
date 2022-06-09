from random import choice
aluno1 = input('O nome de um aluno: ')
aluno2 = input('O nome de outro aluno: ')
aluno3 = input('O nome de outro aluno: ')
aluno4 = input('O nome de outro aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
print('O sorteado para apagar o quadro foi: {}'.format(choice(alunos)))
