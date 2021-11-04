import pygame
import os

print('='*20)
print('Desafio 021\nFaça um programa em python que abra e reproduza  áudio de um arquivo MP3')
print('='*20)

pygame.init()
if os.path.exists('league-of-legends.mp3'):
  pygame.mixer.music.load('league-of-legends.mp3')
  pygame.mixer.music.play()
  pygame.mixer.music.set_volume(1)
  print('Esta sendo tacado: Warrios')


  clock = pygame.time.Clock()
  clock.tick(10)

  while pygame.mixer.music.get_busy():
     pygame.event.poll()
     clock.tick(3)
else:
  print('O arquivo league-of-legends.mp3 não está no diretório do script Python')



print('=' * 20)
