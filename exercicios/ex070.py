total = caro = barato = cont = 0
pBarato = ''
print('--' * 20)
print('           LOJA SUPER BARATÃO')
print('--' * 20)
while True:
    prod = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    cont += 1
    total += preco
    if cont == 1 or barato > preco:
        barato = preco
        pBarato = prod
    continua = ' '
    if preco > 1000:
        caro += 1
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        print('------------------- FIM DO PROGRAMA -------------------')
        print(f'O total da compra foi R${total:.2f}')
        print(f'Temos {caro} produto custando mais de R$1000.00')
        print(f'O produto mais barato foi {pBarato} que custa R${barato}')
        break


