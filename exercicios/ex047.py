print (f'{"ESCOLHA UMA OPÇÃO PARA PAR OU IMPAR":=^80}')
print('[ A ] PAR\n[ B ] IMPAR')
opção = str(input('Informe a opção: ').upper())

if opção == 'A':
    for c in range(2,51,2):
        print(c, end=' ')
elif opção == 'B':
    for c in range(1,50,2):
        print(c, end=' ')
else:
    print('OPÇÃO INVÁLIDA! DIGITE NOVAMENTE')

print('Acabou')
