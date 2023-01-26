print('='*40)
print(f'{"10 TERMOS DE UMA PA":^40}')
print('='*40)

termo = int(input('Primero termo: '))
razão = int(input('Razão: '))

for c in range(termo, razão*10, razão):
    print (c, end=' → ')
print('ACABOU')