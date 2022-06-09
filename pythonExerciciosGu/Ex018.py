import math
a = float(input('Informe um angulo para o cálculo: '))
a = math.radians(a)
print('O ángulo digitado foi {}'.format(a))
print('O seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(math.sin(a), math.cos(a), math.tan(a)))
