"""
Escopo de Variaveis

Dois  casos de escopo:

1- variaveis globais:
    - Variaveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa
2- variaveis locais:
    - Variaveis locais são apenas reconhecidadas no bloco onde foram declaradas, ou seja, seu escopo
    esta limitado ao bloco donde foi declarada.

Para declarar variaveis em python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma lingagem de tipagem dinâmica. Isso significa que ao declararmos
uma variavel, nós nao colocamos o tipod de dado dela.
Este tipo é inferido ao atribuirmos o valor a mesma.
"""

numero = True
print(numero)
print(type(numero))
