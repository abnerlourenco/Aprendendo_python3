# -*- coding utf: -8 -*-

def chamar():
	print("Bem vindo a declaração de uma função")

chamar()



# a função tambem pode receber parametros, com isso podemos inserir dentro do escopo da função

def soma(x,y):
	resultado = x + y
	print(resultado)


soma(8, 9)

# o objetivo da função é retornar algum valor

def subtração(a,b):
	return a - b

resultado = subtração(19, 9)

print(resultado)