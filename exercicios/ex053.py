frase = str(input('Digite uma frase: ')).replace(' ','').upper()
inverso = frase[::-1]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == frase:
    print('A frase digitada É um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')