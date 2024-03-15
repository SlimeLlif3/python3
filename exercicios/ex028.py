from random import randint
from time import sleep
ale = randint(0,5)
print('-=--' * 15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=--' * 15)
number = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if number == ale:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('TÚ É BURRO DEMAIS KKKK, TREINA MAIS SEU FRACO.')
