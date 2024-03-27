lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continua = str(input('Quer continuar? [S/N]')).strip().upper()
    while continua not in 'SN':
        print('Opção inválida! Por favor digite [S/N]')
        continua = str(input('Quer continuar? [S/N]')).strip().upper()
    else:
        if continua == 'N':
            print('-=' * 40)
            print(f'Você digitou {len(lista)} elementos')
            print(f'Os valores em ordem descrescente são {sorted(lista,reverse=True)}')
            if 5 in lista:
                print('O valor 5 foi encontrado na lista!')
            else:
                print('O valor 5 não foi encontrado na lista!')
            break
