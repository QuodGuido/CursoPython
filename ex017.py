from math import hypot

print('='*20)
print('Desafio 017\nFaça um programa que leia o comprimento do\n'
      'Cateto oposto e do cateto adjacente de um\n'
      'triângulo retângulo, calcule e mostre o\n'
      'comprimento da hipotenusa')
print('='*20)

n = float (input('Cateto oposto: '))
n2 = float (input('Cateto adjacente: '))

print('Hipotenusa: {:.2f}'.format(hypot(n, n2)))

print('='*20)
