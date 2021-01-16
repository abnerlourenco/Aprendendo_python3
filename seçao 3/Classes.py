# -*- coding: utf -8 -*-

"""classe é uma estrutura que abstrai um 
conjunto de objetos com caracteristicas similares
"""

# classe serve para criação de objetos

# os atributos e metodo(funções) das classes vem abaixo do nome

class livro:

	def __init__(self, titulo, autor, editora, isbn, ano):
		self.titulo = titulo
		self.autor = autor
		self.editora = editora
		self.isbn = isbn
		self.ano = ano

	def __str__(self):
		return 'Titulo: %s, Autor: %s, Editora: %s, ISBN: %s, Ano: %s' % \
				(self.titulo, self.autor, self.editora, self.isbn, self.ano)

# agora cria-se uma instancia da classe livro

livro1 = livro('Curso de Python em 6h', 'Alcimar Costa', 'Udemy', '878-98-9988-988-9', 2018)

print(livro1.titulo)
print(livro1.autor)
print(livro1.editora)
print(livro1.isbn)
print(livro1.ano)

print(livro1)