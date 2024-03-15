print('=' * 30)
print('     10 TERMOS DE UMA PA')
print('=' * 30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
soma = termo + (10 - 1) * razao
for c in range(termo, soma + razao, razao):
    print('{}'.format(c), end=' → ')
print('ACABOU')