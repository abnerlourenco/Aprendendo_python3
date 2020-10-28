# -*- coding: utf-8 -*-

import random
import time

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
	tentativa = 7
else:
	print("\nNão entendi...")
	topar = str(input("\nDigite sim ou nao: "))
#Ainda nao aprendi criar um goto para reiniciar o programa em um ponto especifico.

while tentativa <= 7:
	restante = 7 - tentativa
	time.sleep(3)
	if tentativa == 0:
		print("\nOK %s" % nome)
		print("\nCARREGANDO...")
		time.sleep(5)
		palpite = int(input("\n\nDigite seu palpite: "))
		
	elif tentativa > 0 and tentativa <= 5:
		print("\n%i tentativas restantes!" % restante)
		palpite = int(input("\n\nDigite seu palpite: "))
		
	elif tentativa == 6:
		print("\n%i tentativas restantes!" % restante)
		print("\nBem Vindo a sua ultima tentativa!!")
		palpite = int(input("\n\nDigite seu palpite: "))

	elif tentativa == 7:
		print("\nVocê esgotou suas tentativas ")
		print("\n\nObrigado por participar!!")

	time.sleep(3)

	if palpite < bolao:
		print("\nQuase lá!! Chute um número mais alto!\n")

	elif palpite > bolao:
		print("\nQuase lá!! Chute um número mais baixo!\n")

	else:
		print("\nUAU!! Você acertou de primeira!!")
		print("PARABÉNS %s!!!!" % nome)
		tentativa = 8

	tentativa = tentativa + 1