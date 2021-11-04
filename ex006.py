from math import pow

print('='*20)
print('Desafio 005\nCrie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada')
print('='*20)

n = float (input('Meu número é: '))
print('Meu número é {} \nSeu dobro é: {} \nSeu triplo é: {} \nSua raiz quadrada é: {:.2f}'.format(n, n*2, n*3, pow(n, 1/2)))

print('='*20)
