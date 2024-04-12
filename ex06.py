"""
6. Número primo é aquele que somente é divisível por 1 e por ele mesmo. Fazer um algoritmo que solicite um
número e informe se esse número é primo ou não.
"""

divs = 0
cont = 1

n = int(input('Digite um número: '))

while cont <= n:
    if n % cont == 0:
        divs += 1
    cont += 1

if divs > 2 or n == 2 or n == 0:
    print(f'O número {n} NÃO é primo.')
else:
    print(f'O número {n} É primo.')
