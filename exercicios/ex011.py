larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}X{} e sua àrea é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede você precisará de {} litros de tinta.'.format(tinta))