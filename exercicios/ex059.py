v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))


print('    [ 1 ] Somar\n    [ 2 ] Multiplicar\n    [ 3 ] Maior\n    [ 4 ] Novos Números\n    [ 4 ] Novos Números')
option = int(input('Qual é a sua opção? '))

while option:
    if option == 1:
        print(f'A soma entre {v1} + {v2} é {v1+v2}')
    elif option == 2:
        print(f'O resultado de {v1} x {v2} é {v1*v2}')
    elif option == 3:
        if v1 > v2:
            print(f'Entre {v1} e {v2} o maior valor é {v1}')
        else:
            print(f'Entre {v1} e {v2} o maior valor é {v2}')
    elif option == 4:
        print('Informe os números novamente: ')
        v1 = int(input())  

print('=-==-==-==-==-==-==-==-==-=')