"""
5. Fazer um algoritmo que solicite um número indeterminado de idades de um grupo de indivíduos. A última idade,
que não entrará nos cálculos, contém o valor da idade igual a zero. Calcule a média de idade deste grupo de
indivíduos.
"""

cont, i, soma = 1, 1, 0

while True:
    i = int(input(f'{cont}a idade: [0 para] '))
    if i != 0:
        soma += i
        cont += 1
    else:
        break

cont -= 1
media = soma / cont
print(f'Média de todas as {cont} idades: {media}')
