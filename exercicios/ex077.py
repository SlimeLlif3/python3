palavras = ('APRENDER' , 'PROGRAMAR' , 'LINGUAGEM' , 'PYTHON' , 'CURSO' , 'GRATIS' , 'ESTUDAR', 'PRATICAR' , 'TRABALHAR' , 'MERCADO' , 'PROGRAMADOR' , 'FUTURO')
cont = ('')
for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')

    