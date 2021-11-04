import random

print('='*20)
print('Desafio 020\nO mesmo professor do desafio anterior quer sortear a ordem de\n'
      'apresentação dos trabalhos dos alunos. Faça um programa que leia\n'
      'o nome dos quatro alunos e mostre a orfem de sorteado')
print('='*20)

a1 = str (input('Nome do aluno: '))
a2 = str (input('Nome do aluno: '))
a3 = str (input('Nome do aluno: '))
a4 = str (input('Nome do aluno: '))

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('A ordem de apresentação será: {}'.format(lista))

print('='*20)
