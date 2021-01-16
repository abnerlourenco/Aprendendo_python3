# -*- coding: utf-8 -*-

# variaveis dentro uma classe chama-se atributo.
class Livro:

	def __init__(self, titulo, autor):
		self.__titulo = titulo
		self.autor = autor

	@property    #para Get (acessar)
	def titulo(self):
		return self.__titulo

	@titulo.setter    # para set (inserir)
	def titulo(self, x):
		self.__titulo = titulo
	

livro1 = Livro('Curso de Python', 'Alcimar Costa')

livro1.autor = 'Abner Rocha'