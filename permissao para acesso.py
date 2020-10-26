# -*- coding: utf-8 -*-


print("OLÁ!! Esse documento só é permitido acima de 18 anos\n\nAntes de proseguir informe sua idade:")

idade = int(input("Digite um número inteiro: "))

if idade >= 18:
	print("\nMuito bem sua idade foi confirmada\n")
	print("Acesso permitido")

elif idade == 0:
	print("Valor digitado nao condiz com uma idade correta")

else:
	print("voce não está permitido a navegar nesse documento")