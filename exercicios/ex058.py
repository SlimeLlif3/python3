from random import randint
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi ?')
pc = randint(0,10)
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez.')
        elif jogador > pc:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpite} tentativas. Parabéns!')



        
        
            

   


        
        

        


