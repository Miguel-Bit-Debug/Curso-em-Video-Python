from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que voce deseja: '))

sen = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sen))

cos = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))

tan = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))
