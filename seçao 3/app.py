# -*- coding: utf -8 -*-

""" quando eu preciso importar um escopo
 de um codigo para ser utilizado em 
 outro arquivo utiliza-se"""

"""se utilizar o import para localizar deve ser 
adicionado todo o caminho do pacote para eliminar o erro"""


"""
import funcao_media_escolar

media = funcao_media_escolar.media( 8, 9, 7, 9)
print(media)

"""

# os arquivos sao chamados módulos

from pacote_media_escolar.funcao_media_escolar import media

media = media(8 ,9 , 7, 9)

print(media)