velocidade = int(input('Qual é a velocidade atual do carro? '))
multa = float(velocidade - 80) * 7
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite de velocidade da via que é 80Km/h\nVocê deve pagar uma multa no valor de R${:.2f}'.format(multa))
    