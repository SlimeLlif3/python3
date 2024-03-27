expressao = str(input('Digite a expressão:'))
ocorrencias = expressao.count('(')
if expressao.count('(') == expressao.count(')'):
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')