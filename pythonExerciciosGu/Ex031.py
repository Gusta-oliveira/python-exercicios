distancia = float(input('Informe a distancia da viagem em Km: '))
print(f'A distancia a viajar é {distancia}Km')
if distancia <= 200:
    valor = 0.5 * distancia
else:
    valor = 0.45 * distancia
print('O valor a pagar é: R${:.2f}'.format(valor))
