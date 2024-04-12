"""
9. Faça um algoritmo que apresente um menu com as opções abaixo. Considere que o saldo deve iniciar em R$
0,00 e a cada saque ou depósito o valor do saldo deve ser atualizado. Após cada operação realizada, o menu
deve ser exibido novamente, e o programa deve ser finalizado apenas quando o usuário selecionar a opção 4.
1 - Consulta Saldo
2 - Realizar Saque
3 - Realizar Depósito
4 – Sair
Escolha uma opção:
"""

saldo = 0
opcao = 0

while True:
    print('--' * 24)
    opcao = int(input('1 - Consulta Saldo\n'
                      '2 - Realizar Saque\n'
                      '3 - Realizar Depósito\n'
                      '4 - Sair\n'
                      'Escolha uma opção: '))
    print('--' * 24)
    match opcao:
        case 1:
            print(f'Saldo: R${saldo:.2f}')
        case 2:
            saque = float(input('Qual valor deseja sacar? R$'))
            if saque > saldo:
                print('Saldo insuficiente!')
            else:
                saldo -= saque
                print('Saque realizado com sucesso!')
        case 3:
            deposito = float(input('Qual valor deseja depositar? R$'))
            saldo += deposito
            print(f'R${deposito:.2f} depositado com sucesso!')
        case 4:
            print('Fim do programa')
            break
        case _:
            print('Escolha uma opção válida!')


