salario = float(input('Qual é o sálario do funcionário? '))
aumentoMenor = salario * 110/100
aumentoMaior = salario * 115/100

if salario <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aumentoMaior))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aumentoMenor))
