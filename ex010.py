print('='*20)
print('Desafio 0010\nCrie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar\n Considere US$1,00 = RS$3,27.')
print('='*20)

reais = float(input('Quantos reais tem na carteira? '))
dolares = reais/3.27

print('Com RS${} é possivel comprar US${:.2f} dólares'.format(reais, dolares))

print('='*20)
