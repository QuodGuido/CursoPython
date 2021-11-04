print('='*20)
print('Desafio 0015\nEscreva um programa que pergunte a quantidade de Km\n'
      'percorridos por um carro alugado e a quantidade de dias pelos\n'
      'quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro\n'
      'custa RS$60 por dia e RS$0,15 por Km rodado.')
print('='*20)

distancia = float (input('Quantos quilimetros o carro andou ? '))
dias = float (input('Por quantos dias o carro foi alugado ? '))

valor_distancia = distancia * 0.15
valor_dias = dias * 60
total = valor_dias + valor_distancia

print('O carro foi alugado por {} dias e andou por {}km'.format(dias, distancia))
print('Dessa forma o valor a ser pago é: R${:.2f}'.format(total))

print('='*20)
