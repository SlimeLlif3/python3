produto = float(input('Qual é o preço do produto? '))
porcentagem = produto * 95 / 100
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(produto, porcentagem))