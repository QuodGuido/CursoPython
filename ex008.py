print('='*20)
print('Desafio 008\nEscreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.')
print('='*20)

valor = float (input('Qual a metragem? '))
dm = valor * 10
cm = valor * 100
mm = valor * 1000
dam = valor / 10
hm = valor / 100
km = valor / 1000
print('{:.0f}m são:\n{}dm\n{}cm\n{}mm\n{}dam\n{}hm\n{}km'.format(valor, dm, cm, mm, dam, hm, km))

print('='*20)
