# -*- coding: utf-8 -*-

import random

bolao = random.randint(0,100)
tentativa = 0

print("OLÁ JOGADOR!!\n")
print("VAMOS TESTAR SUA SORTE?\n")
print("AS REGRAS SÃO:")
print("1° Chute um numero qualquer entre 0 e 100")
print("2° Você terá 7 tentativas")
print("3° Você rebeberá dicas para o próximo chute.")

print("\n\nVAI TOPAR O DESAFIO?")
topar = str(input("sim ou nao?: "))


if topar == "sim" or topar == "sin":
	nome = str(input("Digite seu nome: ")) 
	tentativa = 0
elif topar == "nao" or topar == "não" or topar == "not":
	print("Que Pena!!")
	tentativa = 8
else:
	print("\nNão entendi...")
	topar = str(input("\nDigite sim ou nao: "))
#Ainda nao aprendi criar um goto para reiniciar o programa em um ponto especifico.

while tentativa <= 7:
	restante = 7 - tentativa
	if tentativa == 0:
		print("OK %s" % nome)
		print("%i tentativas restantes!" % restante)
		palpite = int(input("Digite seu palpite: "))
		
		if palpite < bolao:
			print("\nQuase lá!! Chute um número mais alto!\n")
			tentativa = tentativa +1

		elif palpite > bolao:
			print("\nQuase lá!! Chute um número mais baixo!\n")

			tentativa = tentativa +1
		else:
			print("\nUAU!! Você acertou de primeira!!")
			print("PARABÉNS %s!!!!" % nome)
			tentativa = 8

	elif tentativa > 0 and tentativa < 5:
		print("%i tentativas restantes!" % restante)
		palpite = int(input("Digite seu palpite: "))

		if palpite < bolao:
			print("\nQuase lá!! Chute um número mais alto!\n")
			
			tentativa = tentativa +1

		elif palpite > bolao:
			print("\nQuase lá!! Chute um número mais baixo!\n")

			tentativa = tentativa +1
		else:
			print("\nUAU!! Você acertou de primeira!!")
			print("PARABÉNS %s!!!!", nome)
			tentativa = 8
	elif tentativa == 5:
		print("Bem Vindo a sua ultima tentativa!!")
		tentativa = tentativa + 1

	elif tentativa == 6:
		print("Você esgotou suas tentativas ")
		print("\n\nObrigado por participar!!")
		tentativa = tentativa + 1

	elif tentativa == 7:
		print("\n\nObrigado por participar!!")
		tentativa = tentativa + 1