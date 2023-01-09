print('Para saber quantos litros de tinta precisa para pintar sua parede, informe largura e altura e pressione ENTER')

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))

print(f'Sua parede tem a dimensão de {l}X{a} e sua área é de {l*a:.3f}m².\nPara pintar essa parede, você precisará de {(l*a)/2:.4f}l de tinta.')