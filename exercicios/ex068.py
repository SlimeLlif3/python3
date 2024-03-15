from random import randint
cont = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    computador = randint(1,10)
    valor = int(input('Diga um valor: '))
    soma = computador + valor
    pi = str(input('Par ou ímpar/ [P/I] ')).strip().upper()
    print('==' * 20)
    if pi != 'P' and pi != 'I':
        print('Essa opção não existe, por favor digite [P/I]')
    else:
        if valor > 10:
            print('Você só tem 10 dedos nas mãos seu paspalho, digite novamente a não ser que seja um mutante.')
        else:
            if soma % 2 == 0:
                print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU PAR')
                if pi == 'P':
                    print('==' * 20)
                    print('Você VENCEU!\nVamos jogar novamente...')
                    print('==' * 20)
                    cont += 1
                else:
                    print('==' * 20)
                    print('Você PERDEU!')
                    print('=-' * 20)
                    print(f'GAME OVER! Você venceu {cont} vezes.')
                    break
            if soma % 2 != 0:
                print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU IMPAR')
                if pi == 'I':
                    print('==' * 20)
                    print('Você VENCEU!\nVamos jogar novamente...')
                    print('==' * 20)
                    cont += 1
                else:
                    print('==' * 20)
                    print('Você PERDEU!')
                    print('=-' * 20)
                    print(f'GAME OVER! Você venceu {cont} vezes.')
                    break

                 

            
            
