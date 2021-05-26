import pygame
from pygame.locals import *


class Puntos(pygame.sprite.Sprite):

    def __init__(self, valor, x, y, pantalla):
        super(Puntos, self).__init__()
        self.valor = valor
        self.presionada = False
        self.x = x
        self.y = y
        self.pantalla = pantalla
        if(valor == 1 or valor == 3 or valor == 5 or valor == 7 or valor == 9
        or valor == 23 or valor == 25 or valor == 27 or valor == 29
        or valor == 31 or valor == 45 or valor == 47 or valor == 49
        or valor == 51 or valor == 53 or valor == 67 or valor == 69
        or valor == 71 or valor == 73 or valor == 75 or valor == 89
        or valor == 91 or valor == 93 or valor == 95 or valor == 97
        or valor == 111 or valor == 113 or valor == 115 or valor == 117
        or valor == 119):
            self.color = (255, 0, 0)  # Rojo
        else:
            self.color = (0, 0, 255)  # Azul
        self.circulo = pygame.draw.circle(self.pantalla, self.color,
        (self.x, self.y), 15)
        print(self.circulo)

    def presionar(self):
        self.presionada = not self.presionada

    def pintarPunto(self):
        if(self.presionada is True):
            self.circulo = pygame.draw.circle(self.pantalla, (0, 0, 0),
            (self.x, self.y), 15)
        else:
            self.circulo = pygame.draw.circle(self.pantalla, self.color,
            (self.x, self.y), 15)