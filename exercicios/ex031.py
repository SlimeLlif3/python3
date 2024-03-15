distancia = float(input('Qual é a distância da viagem? '))
preco = distancia / 2
promocao = preco * 90/100
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(promocao))
