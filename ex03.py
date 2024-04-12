"""
3. Construa um algoritmo que mostre todos os valores ímpares entre X e Y, onde X e Y são fornecidos pelo usuário
"""

x = int(input('Valor de X: '))
y = int(input('Valor de Y: '))
cont, base = 0, 0

if x > y:
    cont += y
    base += x
elif x < y:
    cont += x
    base += y

print(f'Valores ímpares entre {x} e {y}: ', end='')
while cont <= base:
    if cont % 2 != 0:
        print(f'{cont}, ', end='')
    cont += 1
print('Fim')
