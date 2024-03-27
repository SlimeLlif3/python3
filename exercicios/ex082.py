lista_completa = []
lista_par = []
lista_impar = []
while True:
    num = int(input('Digite um número: '))
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    lista_completa.append(num)
    while continua not in 'SN':
        print('Opção inválida! Por favor digite [S/N]')
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    if continua in 'N':
        print('-=' * 40)
        print(f'A lista completa é {lista_completa}')
        print(f'A lista de pares é {lista_par}')
        print(f'A lista de ímpares é {lista_impar}')
        break
    
        
