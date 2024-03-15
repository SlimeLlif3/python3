casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = casa / (12 * anos)
if parcela >= salario * 30 / 100:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}\nEmpréstimo NEGADO'.format(casa, anos, parcela))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}\nEmspréstimo CONCEDIDO'.format(casa, anos, parcela))
