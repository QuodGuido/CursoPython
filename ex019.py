import random

print('='*20)
print('Desafio 019\nUm professor quer sortear um dos seus quatro alunos para apagar\n'
      'o quadro. Faça um programa que ajude ele, lendo o nome deles e\n'
      'escrevendo o nome do escolhido')
print('='*20)

a1 = str (input('Nome do aluno: '))
a2 = str (input('Nome do aluno: '))
a3 = str (input('Nome do aluno: '))
a4 = str (input('Nome do aluno: '))

lista = random.choice([a1, a2, a3, a4])

print('O sorteado para limpar o quadro hoje será {}'.format(lista))

print('='*20)
