num = int(input('Digite um número: '))
continuar = str(input('Quer continuar? [S/N]')).strip().upper()
cont = 1
soma = num
menor = num
maior = num
while continuar == 'S':
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    cont += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if continuar == 'N':
        media = soma / cont
print('Você digitou {} números e a média foi {}\nO maior valor foi {} e o meno foi {}'.format(cont, media, maior, menor))
    
    
    
    
    
