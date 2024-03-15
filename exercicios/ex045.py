import random
import time
item = ('PEDRA','PAPEL','TESOURA')
maquina = random.randint(0,2)

print('Suas opções: ')
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
      ''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('-=' * 10)
print('Computador jogou {}'.format(item[maquina]))
print('Jogador jogou {}'.format(item[jogador]))
print('-=' * 10)
if jogador == maquina:
    print('Empatou')
elif jogador == 0:
    if maquina == 1:
        print('JOGADOR PERDEU')
    elif maquina == 2:
        print('JOGADOR GANHOU')
elif jogador == 1:
    if maquina == 2:
        print('JOGADOR PERDEU')
    elif maquina == 0:
        print('JOGADOR GANHOU')
elif jogador == 2:
    if maquina == 0:
        print('JOGADOR PERDEU')
    elif maquina == 1:
        print('JOGADOR GANHOU')
