dinheiro = float(input('Quanto dinheiro você tem na carteira? '))
dolar = float(4.94)
euro = float(5.35)
converte = dinheiro / dolar
converte2 = dinheiro / euro
print('Com R${} você pode comprar US{:.2f} e EUR{:.2f}'.format(dinheiro, converte, converte2))
