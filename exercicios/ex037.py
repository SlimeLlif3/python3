num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
option = int(input('Sua opção: '))
if option == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num) [2:]))
elif option == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num) [2:]))
elif option == 3: 
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num) [2:]))
else:
    print('Número inválido, digite por favor um número entre 1 e 3')



