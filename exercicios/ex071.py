print('=' * 40)
print('               BANCO CEV')
print('=' * 40)
cinquenta = vinte = dez = um = 0
valor = int(input('Que valor você quer sacar? '))
while valor > 50:
    cinquenta += 1
    valor = valor - 50
if cinquenta == 1:
    print(f'Total de {cinquenta} cédula de R$50')
if cinquenta > 1:
    print(f'Total de {cinquenta} cédulas de R$50')
while valor > 20 and valor < 50:
    vinte += 1
    valor -= 20
if vinte == 1:
    print(f'Total de {vinte} cédula de R$20')
if vinte > 1:
    print(f'Total de {vinte} cédulas de R$20')
while valor > 10 and valor < 20:
    dez += 1
    valor -= 10
if dez == 1:
    print(f'Total de {dez} cédula de R$10')
if dez > 1:
    print(f'Total de {dez} cédulas de R$10')
while valor > 0 and valor < 10:
    um += 1
    valor -= 1
if um == 1:
    print(f'Total de {um} cédula de R$1')
if um > 1:
    print(f'Total de {um} cédulas de R$1')
    
    
    

    



 
