print('Total a se pagar por dias e km rodados')
day = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
vd= day*60
vkm= km*0.15
total = vd+vkm
print(f'Custo diário R${vd:.2f}\nCusto por km rodados R${vkm:.2f}\nValor total a se pagarR${total:.2f}')