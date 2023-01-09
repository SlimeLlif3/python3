print('Porcentagem de aumento no salário do funcionário')
s = float(input('Qual o salário do Funcionário? R$'))
total = s+(s*0.15)

print(f'Um funcionário que ganhava R${s} , com 15% de aumento, passa a receber R${total:.2f}')