num = int(input('Digite um número [999 para parar]: '))
cont = 1
somar = num
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        cont +=1
        somar += num
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, somar))