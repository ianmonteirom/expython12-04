"""
2. Fazer um algoritmo que solicite um número inteiro N qualquer e exiba a tabuada de N.
"""

n = int(input('Digite um número: '))
cont = 1

while cont <= 10:
    print(f'{n} x {cont} = {n * cont}')
    cont += 1
