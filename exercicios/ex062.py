print('Gerador de PA')
print('-=' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total = total  + mais
    while c <= total:
        print(primeiro,end=' → ')
        primeiro += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais ? '))
print('FIM')
print('Progressão finalizou com {} números'.format(total))



