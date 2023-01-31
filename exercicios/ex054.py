cont = 0
maior = 0
menor = 0
for i in range(1, 8):
    cont += 1
    ano = int(input(f'Em que ano a {cont}ª pessoa nasceu? '))
    if ano < 2005:
        maior += 1
    else:
        menor += 1
if maior== 1:
    print(f'Ao todo tivemos {maior} pessoa maior de idade\nE também tivemos {menor} pessoas menores de idade')
elif menor == 1:
    print(f'Ao todo tivemos {maior} pessoas maiores de idade\nE também tivemos {menor} pessoa menor de idade')
else:
    print(f'Ao todo tivemos {maior} pessoas maiores de idade\nE também tivemos {menor} pessoas menores de idade')

     