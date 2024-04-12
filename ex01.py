"""
1. Fazer um algoritmo que exiba na tela todos os números ímpares de 1 a n, onde n é fornecido pelo usuário.
"""

n = int(input('Digite um número: '))
cont = 1

while cont <= n:
    if cont % 2 != 0:
        print(f'{cont}, ', end='')
    cont += 1
print('Fim')
