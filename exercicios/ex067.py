cont = 1
valor = int(input('Quer ver a tabuada de qual valor? '))
while True:
    if valor <= -1:
        break
    if cont <= 10:
        print(f'{valor} x {cont} = {valor * cont}')
        cont += 1
    if cont > 10:
        cont = 1
        print('-' * 40)
        valor = int(input('Quer ver a tabuada de qual valor? '))
        print('-' * 40)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')

    

    

    