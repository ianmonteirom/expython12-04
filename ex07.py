"""
7. Solicite um número inteiro positivo e informe a soma dos algarismos desse número. Por exemplo:
Entrada: 1234 Saída: 10 Entrada: 2182341 Saída: 21 Entrada: 100001 Saída: 2
"""

n = -1
while n <= 0:
    n = int(input('Digite um número inteiro positivo: '))

nstr = str(n)
algarismos = []

cont = 0
while cont < len(nstr):
    algarismos.append(int(nstr[cont]))
    cont += 1

print(f'Soma de {algarismos}: {sum(algarismos)}')
