from random import randint
from time import sleep

itens = ('Pedra','Papel','Tesoura')
pc = randint(0,2)

print(f'{" JO KEN PO!!! ":=^40}')
print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-='*10)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*10)

if jogador == pc:
    print('DEU EMPATE! JOGUE OUTRA VEZ')

elif jogador == 0 and pc == 1 or jogador == 1 and pc == 2 or jogador == 2 and pc == 0:
    print('JOGADOR PERDE')
elif jogador == 1 and pc == 0 or jogador == 2 and pc == 1 or jogador == 2 and pc == 0:
    print('JOGADOR GANHA')
else:
    print('OPÇÃO INVÁLIDA! DIGITE NOVAMENTE')




 
