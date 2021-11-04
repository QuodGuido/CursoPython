print('='*20)
print('Desafio 007\nDesenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.')
print('='*20)

nome_aluno = input('Qual o nome do aluno? ')
nota_1 = float(input('Nota do primeiro periodo é: '))
nota_2 = float(input('Nota do segundo perido é: '))

print (f'O aluno {nome_aluno} tirou {nota_1} no primeiro periodo e {nota_2} no segundo periodo, dessa forma sua média é '
       f'{(nota_1+nota_2)/2}')
print('='*20)
