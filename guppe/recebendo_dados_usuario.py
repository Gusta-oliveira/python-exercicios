"""
Recebendo dados do usuário

input -> Todo dado recebido via input é do tipo String

Em python, string é tudo que estiver entre:

- Aspas simples '';
- Aspas duplas "";
- Aspas Simples triplas ''' ''';
- Aspas duplas triplas ;

"""

# Entrada de dados

# print('Qual é seu nome?')
# nome = input()  # Input -> Entrada
nome = input('Qual seu nome?')

# Exemplo antigo
# print('Seja bem-vindo %s' % nome)

# Exemplo moderno
# print('Seja bem-vindo {0}' .format(nome))

# Exemplo de print mais atual
print(f'Seja bem-vindo {nome}')

# print('Qual sua idade?')
# idade = input()

idade = int(input('Qual sua idade?'))
# Processamento

# Saída

# Exemplo antigo
# print('A %s tem %s' % (nome, idade))

# Exemplo moderno
# print('Você {0} tem {1} anos' .format(nome, idade))

# Exemplo de print mais atual
print(f'Você {nome} tem {idade} anos')
print(f'Você {nome} nasceu em {2022 - idade}')
