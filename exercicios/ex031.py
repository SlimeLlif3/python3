dis = int(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {dis:.1f}Km.')
if dis <= 200:
    preço = dis*0.50
else:
    preço = dis*0.45

print(f'E o preço da sua passagem será de R${preço:.2f}')

