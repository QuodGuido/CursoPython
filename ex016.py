from math import trunc

print('='*20)
print('Desafio 016\nCrie um programa que leia um número Real qualquer pelo teclado e\n'
      'mostre na tela a sua porção Inteira\n'
      '\n'
      'Ex:','\033[1m' + 'Digite um número:' + '\033[0m',
      '\033[1m' + 'O número' + '\033[0m',
      '6,127',
      '\033[1m' + 'tem a parte inteira' + '\033[0m',
      '6')

print('='*20)

n = float (input('Esolha um número para ser escrito inteiro: '))
print('O número {} foi escolhido, dessa forma sua forma inteira é {}'.format(n, trunc(n)))

print('='*20)

