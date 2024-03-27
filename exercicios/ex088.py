from time import sleep
from random import sample
print('-' * 40)
print('JOGA NA MEGA SENA'.center(40))
print('-' * 40)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=  SORTEANDO {jogos} JOGOS  -=-=-=')
lista = []
for c in range(1,jogos+1):
    print(f'Jogo {c}: ',end='')
    ale = sorted(sample(range(1,61),6)) 
    print(lista[0],end=' ')
    lista.clear()
    sleep(0.5)
    print()

       
        
