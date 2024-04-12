"""
8. Escreva um algoritmo que solicite vários números inteiros e exiba o resultado da multiplicação de todos os
números ímpares e o somatório de todos os números pares. O algoritmo deve ser finalizado quando o usuário
digitar zero.
"""

n = -1
multimp, somapar, cont = 1, 0, 1

while n != 0:
    n = int(input(f'Digite o {cont}o número inteiro [0 para]: '))
    cont += 1
    if n % 2 != 0:
        multimp *= n
    elif n % 2 == 0:
        somapar += n

print(f'Resultado da multiplicação de todos os números ímpares digitados: {multimp}\n'
      f'Resultado da soma de todos os números pares digitados: {somapar}')
