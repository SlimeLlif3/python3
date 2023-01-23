inteiro = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha uma da bases para conversão:\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL\nSua opção: '))

if escolha == 1:
    print(f'{inteiro} convertido para BINÁRIO é igual a {bin(inteiro)[2:]}')

elif escolha == 2:
    print(f'{inteiro} convertido para OCTAL é igual a {oct(inteiro)[2:]}')

elif escolha == 3:
    print(f'{inteiro} convertido para HEXADECIMAL é igual a {hex(inteiro)[2:]}')    

else:
    print('O número digitado é inválido, por favor digite um número de 1 a 3.')