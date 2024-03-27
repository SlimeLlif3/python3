from random import randint
valores_sorteados = (randint(1,10), randint(1,10), randint(1,10), randint(1,10) , randint(1,10))
print('Os valores sorteados foram: ',end='')
for n in valores_sorteados:
    print(f'{n}', end=' ')
menor = min(valores_sorteados)
maior = max(valores_sorteados)
print(f'\nO maior valor foi {maior}\nO menor valor foi {menor}')
