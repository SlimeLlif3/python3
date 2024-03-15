salario = float(input('Qual é o salário do Funcionário? '))
aumento = salario * 115 / 100
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, aumento))