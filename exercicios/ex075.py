valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores: {valores}',end='')
print(f'\nO número 9 apareceu {valores.count(9)} vezes')
print('Os valores PARES digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(f'{n}',end=' ')
    if n == 3:
        print(f'\nO número 3 apareceu na posição {valores.index(3) + 1}')
    






