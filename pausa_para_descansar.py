'''
Criar uma função que me lembre a parar de estudar e fazer uma pausa a cada 2h
Trabalho inicia de 8h as 12
'''
import webbrowser
import time


intervalos = 2
contador = 0
print('SUA PROGRAMÇÃO DE DESCANÇO ESTÁ ATIVADA ')

while contador < intervalos:
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=JRVD-pndqY0')
    contador = contador + 1

# a função sleep da biblioteca time concede um tempo para executar uma função( contado em segundos)