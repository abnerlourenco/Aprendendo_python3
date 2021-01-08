# Função print()

#declaração das variaveis
dia = 19
mes = 4
ano = 2018
nome = 'José'
sobrenome = 'Silva'
altura = 1.9



print('O aluno ' + nome + ' ' + sobrenome)
print('O aluno', nome, sobrenome)

# quando eu identifico o modo sep='/' diz que esses dados serão exibidos separados por barra.
print(dia, mes, ano, sep='/')


print('Aluno %s foi aprovado ' % nome)
print('Bem vindo %s' % nome)

# O aluno José da Silva tem altura igual a 1.9
# %s para strings (str)
# %d inteiros (int)
# %f decimais (float)
print('O aluno %s %s, tem altura igual a %f ' % (nome, sobrenome, altura))




#Funções de conversão

# int('3')
# float('3.14')
# str(2.3)

print('Aluno ' + nome + ' Tem altura igual a ' + str(altura))

