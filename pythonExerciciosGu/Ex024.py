"""
city = str(input('Digite o nome da cidade: ')).strip()
city = city.split()
city = 'SANTO' in city[0].upper()
print('A cidade começa com Santo? {}'.format(city))

"""
cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')


