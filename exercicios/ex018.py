from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
radiante = radians(angulo) 
seno = sin(radiante)
cosseno = cos(radiante)
tangente = tan(radiante)
print('O ângulo de {} tem o SENO de {:.2f}\nO ângulo de {} tem o COSSENO de {:.2f}\nO ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, seno, angulo, cosseno, angulo, tangente ))
