#faça um programa que abra e execute um arquivo mp3
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex0021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()



