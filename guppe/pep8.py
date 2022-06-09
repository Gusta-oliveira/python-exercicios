"""
PEP8 - Python Enhancement Proposal

São propostas de melhoria para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythonica

(1) - Ultilize Camel Case para nomes de classes;
Ex: class Calculadora:
        pass
    class CalculadoraCientifica:
        pass

(2) - Ultilize nomes em minusculo, separados por underline para funções ou variaveis;
Ex: def soma():
        pass
    def soma_dois():
        pass

    numero = 4
    numero_impar = 5

(3) - Ultilize 4 espaços para identação!! (Não é recomendado utilizar TAB)
Ex: if 'a' in 'banana':
        print('tem')

(4) Linhas em branco
- Separar funções e definições de classes com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma unica linha em branco;

(5) - Imports
- Importes devem ser sempre feitos em linhas separadas;
Ex:
#import errado
import sys, os

#import certo
import sys
import os

#Não há problemas em utilizar:
from types import StringType, ListType

#Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from type import (
    TringType,
    ListType,
    SetType,
    OutroType
)

#Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes de
constantes ou variaveis globais.

(6) - Espaco em expressões e instruções
Ex: #Não faca:
funcao( algo[ 1 ], { outro 2} )

algo (1)

dict ['chave'] = lista [indice]

x              = 1
y              = 3
variavel_longa = 5

#Faça
funcao(algo[1], {outro: 2})

algo(1)

dict['chave] = lista[indice]

x = 1
y = 3
variavel_longa = 5

(7) - Termine sempre uma instrução com uma nova linha
"""
import this
