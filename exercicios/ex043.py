p = float(input('Qual é o seu peso ? (Kg) '))
a = float(input('Qual é a sua altura? (m) '))
imc = p/(a**2)

print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc <= 18.5 :
    print('Você está ABAIXO do Peso!')
elif imc <= 25:
    print('PARABÉNS, Você está com o PESO IDEAL!')
elif imc <= 30:
    print('Você está com SOBREPESO!')
elif imc <= 40:
    print('Você está com OBESIDADE!') 
else:
    print('Você está com OBESIDADE MÓRBIDA!')