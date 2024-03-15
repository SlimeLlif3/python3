soma = 0
for c in range(1,7):
    valor = int(input('Digite o {} valor: '.format(c)))
    if valor % 2 == 0:
        soma += valor
print('A soma dos números PARES é {}'.format(soma))