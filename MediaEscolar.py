'''
Informar ao aluno que o programa está em execução
Solicitar ao aluno seu nome
Solcitar ao aluno o nome da matéria
Solicitar as 4 notas
Efetuar o calculo da média
obs.: A média para aprovação é 7
informar ao aluno a frase abaixo:
Se a média for menor que 7, imprimir a frase:
Aluno nome_do_aluno, você foi REPROVADO.
Sua média em nome_da_matéria foi valor_da_media.
Se a média foi igual ou maior que 7, imprimir a frase:
PARABENS!! Aluno nome_do_aluno, você foi APROVADO.
Sua média em nome_da_matéria foi valor_da_media.

'''


print('Bem vindo ao programa de cálculo de média escolar')

nome = input('Digite seu nome completo: ')
materia = input('Digite o nome da matéria ')
print('Agora você precisa informar as quatro notas')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4
if media < 7:
    print('Aluno %s, você foi REPROVADO. Sua média em %s foi de %.2f.'
          % (nome, materia, media))
else:
    print('Parabéns!!!!')
    print('Aluno %s, você foi APROVADO. Sua média em %s foi %.2f.'
          % (nome, materia, media))
