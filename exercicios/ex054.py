from datetime import datetime
atual = datetime.now().year
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    if atual - ano >= 18:
        maior += 1
    else:
        menor += 1
print('\nAo todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))



