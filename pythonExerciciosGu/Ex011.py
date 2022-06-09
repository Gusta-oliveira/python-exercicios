alt = float(input('Qual altura da parede? '))
larg = float(input('E qual a largura? '))

área = alt * larg
tinta = área / 2

print('As dimenções {}x{} tem uma área de: '.format(alt, larg), end="")
print('{}m²\nSerão necessários {}L de tinta apra pinta-la'.format(área, tinta))
