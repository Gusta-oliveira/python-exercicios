frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra (A) aparece ', frase.count('a', 0), ' vezes')
print('A primeira letra (A) esta na posição: ', frase.index('a') + 1)
print('A ultima posição em que (A) aparece é: ', frase.rfind('a') + 1)
