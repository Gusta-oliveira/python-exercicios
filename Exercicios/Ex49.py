print('Informe o horario de inicio!!')
h = int(input('Horas: '))
m = int(input('Minutos: '))
s = int(input('Segundos '))

print(f'Hora de inicio informada \n {h}H: {m}Min: {s}Seg')

add = int(input('Informe em segundos a duração: \n'))
m = m + (add // 60)
h = h + (m // 60)
s = s + (add % 60)
m = m % 60

print(f'Horario de término: {h}H {m}Min {s}Seg')
