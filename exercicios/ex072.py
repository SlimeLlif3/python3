num = ('Zero', 'Um' , 'Dois', 'Três' , 'Quatro',
       'Cinco' , 'Seis' , 'Sete' , 'Oito' , 'Nove',
       'Dez' , 'Onze' , 'Doze' , 'Treze' , 'Catorze',
       'Quinze' , 'Dezesseis' , 'Dezessete' , 'Dezoito',
       'Dezenove' , 'Vinte')

while True:
    num2 = int(input('Digite um número entre 0 e 20: '))
    if num2 > 20:
        print('Tente novamente', end=' ')
    else:
        print(f'Você digitou o número {num[num2]}')
        continua = str(input('Você deseja continuar? [S/N]')).strip().upper()
        if continua == 'N':
            break
        
            

        
        
    
