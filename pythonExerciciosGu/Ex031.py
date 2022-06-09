distancia = float(input('Informe a distancia da viagem em Km: '))
if distancia <= 200:
    valor = 0.5 * distancia
    print(f'A distancia viajada foi de {distancia}Km')
    print('E valor a pagar é: R${:.2f}'.format(valor))
else:
    valor = 0.45 * distancia
    print(f'A distancia viajada foi de {distancia}Km')
    print('O valor a pagar é: R${:.2f}'.format(valor))