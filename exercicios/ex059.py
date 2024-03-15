from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
print('''
        [ 1 ] SOMAR    
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NÚMEROS
        [ 5 ] SAIR DO PROGRAMA''')
opcao = int(input('>>>>>> Qual é a sua opção? '))
while opcao != 5:
    if opcao == 1:
        soma = v1 + v2
        print('A soma entre {} + {} é {}'.format(v1, v2, soma))
        sleep(2)
        print('==-'*15)
    elif opcao == 2:
        multiplica = v1 * v2
        print('A multiplicação entre {} e {} é {}'.format(v1, v2, multiplica))
        sleep(2)
        print('==-'*15)
    elif opcao == 3:
        if v1 > v1:
            print('Entre {} e {} o maior valor é {}'.format(v1, v2, v1))
        else:
            print('Entre {} e {} o maior valor é {}'.format(v1, v2, v2))
        sleep(2)
        print('==-'*15)
    elif opcao == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opcao > 5:
        print('Opção inválida. Tente novamente')
        sleep(2)
        print('==-'*15)
    print('''
        [ 1 ] SOMAR    
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NÚMEROS
        [ 5 ] SAIR DO PROGRAMA
        ''')
    opcao = int(input('>>>>>> Qual é a sua opção? '))
print('Finalizando...')
sleep(2)
print('Fim do programa! Volte sempre! ')
    

    



    
   
