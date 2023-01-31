frase = str(input('Digite uma frase: ')).replace(' ','').upper()
reverse = frase[::-1]
print(f'A frase normal fica {frase} e ao contrario fica {reverse}')
if frase == reverse:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')