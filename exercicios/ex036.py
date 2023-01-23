casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = (casa/anos)/12

if prestacao <= salario*0.30:
    print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}\nEmpréstimo pode ser CONCEDIDO!')
else:
    print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}\nEmpréstimo NEGADO!')

