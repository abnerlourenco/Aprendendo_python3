# -*- coding: utf-8 -*-

import math

a = int(input("Digite o valor de A: "))
b = int(input("\nDigite o valor de B: "))
c = int(input("\nDigite o valor de C: "))


# duas formas de representar potencia (x**2 ou math.pow(x,2))
delta = math.pow(b,2) - 4*a*c
print("\ndelta", delta)



if delta > 0:
	raiz = math.pow(delta,1/2)
	x1 = (-b + raiz)/(2*a)
	x2 = (-b - raiz)/(2*a)
	print("\nAs raízes são", x1, "e", x2)

elif delta < 0:
    print("\nDelta negativo")

else :
	raiz = math.sqrt(delta)

	print("\nRaiz quadrada de delta: ", raiz_delta)