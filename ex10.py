"""
10. Faça um algoritmo para uma eleição entre três candidatos. Deve ser exibido um menu com as opções abaixo.
1 - Candidato 1
2 - Candidato 2
3 - Candidato 3
4 - Voto em Branco
5 - Finalizar
Informe o seu voto:
Quando for escolhida a opção 5, a eleição deve ser finalizada e as informações abaixo devem ser exibidas:
a) A quantidade de votos de cada candidato
b) A porcentagem de votos brancos
c) O candidato vencedor
"""

cand1, cand2, cand3, branco = 0, 0, 0, 0

while True:
    eleicao = int(input('1 - Candidato 1\n'
                        '2 - Candidato 2\n'
                        '3 - Candidato 3\n'
                        '4 - Voto em Branco\n'
                        '5 - Finalizar\n'
                        'Informe seu voto: '))
    print('--' * 24)

    match eleicao:
        case 1:
            cand1 += 1
        case 2:
            cand2 += 1
        case 3:
            cand3 += 1
        case 4:
            branco += 1
        case 5:
            break
        case _:
            print('Opção inválida!')

somatotal = cand1 + cand2 + cand3 + branco
porcbranco = branco / somatotal * 100
vencedor = 'Empate'

if cand1 > cand2 and cand1 > cand3:
    vencedor = 'Candidato 1'
elif cand2 > cand1 and cand2 > cand3:
    vencedor = 'Candidato 2'
elif cand3 > cand1 and cand3 > cand2:
    vencedor = 'Candidato 3'


print(f'Candidato 1: {cand1} votos\n'
      f'Candidato 2: {cand2} votos\n'
      f'Candidato 3: {cand3} votos\n'
      f'Votos brancos: {branco}\n'
      f'Porcentagem de votos brancos: {porcbranco:.2f}%\n'
      f'Vencedor: {vencedor}')
