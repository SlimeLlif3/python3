from math import radians, sin, cos, tan
print('Calculadora de SENO, COSSENO E TANGENTE')
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
print(f'O ângulo de {an} tem o SENO de {seno:.2f}')
cosseno = cos(radians(an))
print(f'O ângulo de {an} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(an))
print(f'O ângulo de {an} tem a TANGENTE de {tangente:.2f}')