print('='*20)
print('Desafio 0011\nFaça um programa que leia a largura e a altura de uma parede em metros,\n'
      'calcule a sua área e a quantidade de tinta necessária para pintá-la,\n'
      'sabendo que cada litro de tinta, pinta uma área de 2m²')
print('='*20)

largura = float (input('Qual a largura da parede? '))
altura = float (input('Qual a altura da parede ? '))

area = largura * altura
tinta = area / 2

print(f'Para pintar uma parede com {area}m², é necessário {tinta}L de tinta')

print('='*20)
