print('=================================== Loja do Yanzin ===================================')
compra = float(input('Preço das compras : R$ '))
print('''
[ 1 ] à vista dinheiro/PIX
[ 2 ] à vista cartão
[ 3 ] 2X no cartão
[ 4 ] 3X no cartão
''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    dinheiro = compra - (compra * 10/100)
    print('Pagando à vista no dinheiro/PIX você tem 10% de desconto')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, dinheiro))
elif opcao == 2:
    cartaoAvista = compra - (compra * 5/100)
    print('Pagando à vista no cartão você tem 5% de desconto')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, cartaoAvista))
elif opcao == 3:
    parcela2 = compra / 2
    print('Sua compra será parcelada em 2X de R${:.2f}'.format(parcela2))
    print('O total da sua compra deu R${:.2f}'.format(compra))
elif opcao == 4:
    vezes = int(input('Quantas parcelas?'))
    total = (compra * 120/100)                                                                               
    parcela = total / vezes
    print('A compra será parcelada em {}X de R${:.2f} COM JUROS'.format(vezes, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, total))
else:
    print('Opção inválida, por favor escolha uma das opções de 1 a 4')