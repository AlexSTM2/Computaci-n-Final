import pygame
from pygame.locals import *
pygame.init()
music = pygame.mixer.Sound("sounds/big mood.mp3")
music.set_volume(0)
music.play()