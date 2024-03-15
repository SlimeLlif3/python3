from random import randint
aleatorio = randint(1,10)
tentativa = 1
print('''
Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?   ''')
palpite = int(input('Qual é seu palpite? '))
while not palpite == aleatorio:
      tentativa += 1
      if palpite > aleatorio:
            print('Menos... Tente mais uma vez') 
            palpite = int(input('Qual é seu palpite? ')) 
      if palpite < aleatorio: 
            print('Mais... Tente mais uma vez')
            palpite = int(input('Qual é seu palpite? '))
print('Acertou com {} tentativas. Parabéns!'.format(tentativa))
