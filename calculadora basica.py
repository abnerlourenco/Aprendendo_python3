# -*- coding: utf-8 -*-

n1 = int(input("Digite o primeiro número: "))
sinal = input("Digite um sinal matemático: ")
n2 = int(input("Digite o segundo número: "))
 
if sinal == "+":
    operação = n1 + n2
 
elif sinal == "-":
    operação = n1 - n2
 
elif sinal == "/":
    operação = n1 / n2
 
elif sinal == "*":
    operação = n1 * n2
 
else:
    print("Sinal inválido.")
 
print(operação)