segundos = int(input('Digite os segudos: '))

minutos = segundos // 60
horas = minutos // 60
minutos = minutos % 60
segundos = segundos % 60

print(f' {horas}H {minutos}Min {segundos}Seg')
