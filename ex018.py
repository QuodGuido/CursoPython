from math import sin, cos, tan

print('='*20)
print('Desafio 017\nFaça um programa que leia um ângulo qualquer e\n'
      'mostre na tela o valor do seno, cosseno e\n'
      'tangente desse ângulo')
print('='*20)

s = float (input('Qual o sen ? '))
c = float (input('Qual o cos? '))
t = float (input('Qual a tang? '))

print('O sen é igual a: {:.2f}\nO cos é igual a: {:.2f}\nA tang é igual a: {:.2f}'. format(sin(s), cos(c),tan(t)))

print('='*20)
