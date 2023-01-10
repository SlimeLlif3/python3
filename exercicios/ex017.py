from math import hypot
print('Calculadora de hipotenusa entre cateto oposto e cateto adjacente')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h1= hypot(co, ca)
print(f'A hipotenusa vai medir {h1:.2f}')