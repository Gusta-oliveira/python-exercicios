#

print('Informe as duas notas do aluno: ')
nota1 = float(input())
nota2 = float(input())

if nota1 <= 10 and nota2 <= 10:
    media = (nota1 + nota2) / 2
    print(f"A média do aluno é: {media}")
else:
    print('As notas não foram inseridas corretamente!')
