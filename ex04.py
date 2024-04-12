"""
4. Fazer um algoritmo que leia um número inteiro positivo, calcule e escreva se o número lido é um número
perfeito ou não. Número perfeito é aquele cuja soma de seus divisores, exceto ele próprio, é igual ao próprio
número. Exemplo: 6 é um número perfeito porque 1 + 2 + 3 = 6.
"""

n = -1
while n <= 0:
    n = int(input('Digite um número inteiro positivo: '))

cont = 1
soma = 0

while cont < n:
    if n % cont == 0:
        print(f'{cont} + ', end='')
        soma += cont
    cont += 1
print(f'= {n}')

if soma == n:
    print(f'{n} é um número perfeito.')
else:
    print(f'{n} não é um número perfeito.')
