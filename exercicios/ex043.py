peso = float(input('Qual é o seu peso?  (Kg) '))
altura = float(input('Qual é a sua altura?  (m) '))
imc = peso / altura ** 2
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Coma mais seu frango, você está ABAIXO do peso.')
elif imc <= 25:
    print('Woow daora, você está com peso NORMAL.')
elif imc < 30:
    print('Cuidado, você está com SOBREPESO.')
elif imc < 35: 
    print('Se cuide melhor gordin, você está com OBESIDADE GRAU I.')
elif imc < 40:
    print('Procurea um médico seu gordo, você está com OBESIDADE GRAU II.')
else: 
    print('Vá ao médico IMEDIATAMENTE gordão, tá maluco???? , você está com OBESIDADE GRAU III(mórbida).')
