print(f'{" LOJAS CAROLINA ":=^40}')
compras = float(input('Preço das compras: R$ '))
opção = int(input('FORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão\nQual é a opção? '))

if opção == 1:
    print(f'Sua compra de R${compras:.2f} vai custar R${compras-(compras*0.10):.2f} no final.')
elif opção == 2:
    print(f'Sua compra de R${compras:.2f} vai custar R${compras-(compras*0.05):.2f} no final.')
elif opção == 3:
    print(f'Sua compra será parcelada em 2x de R${compras:.2f}')
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${(compras+(compras*0.2))/parcelas:.2f} COM JUROS\nSua compra de R${compras:.2f} vai custar R${compras+(compras*0.2):.2f} no final.')
else:
    print('Forma de pagamente INVÁLIDA, Tente novamente.')