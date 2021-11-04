print('='*20)
print('Desafio 0012\nFaça um algoritmo que leia o preço de um produto e mostre seu novo preço,\n com 5% de desconto.')
print('='*20)

preço = float (input('O preço do produto é: '))

desconto = preço * 0.05
novo_valor = preço - desconto

print('O novo preço do produto será ${:.2f} reais'.format(novo_valor))
print('='*20)
