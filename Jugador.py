import pygame
from pygame.locals import *
from Puntos import *


class Jugador():

    def __init__(self, color):
        super(Jugador, self).__init__()
        self.color = color

    def conectar(self, pantalla, x1, y1, x2, y2):
        pygame.draw.line(pantalla, (0, 0, 0),
        (x1, y1), (x2, y2), 10)

    def realizarMov(self, encola, tablero, pantalla):
        if(encola[0].valor > encola[1].valor
        and (encola[0].color == (255, 0, 0)
        and encola[1].color == (255, 0, 0))):
            if(encola[0].valor - 1 == encola[1].valor + 1):
                if(tablero[encola[0].valor - 1] != "-"):
                    self.conectar(pantalla, encola[0].x, encola[0].y,
                    encola[1].x, encola[1].y)
                    tablero[encola[0].valor - 1] = "-"
                    return "Azul"
            elif(encola[0].valor - 11 == encola[1].valor + 11):
                if(tablero[encola[0].valor - 11] != "|"):
                    self.conectar(pantalla, encola[0].x, encola[0].y,
                    encola[1].x, encola[1].y)
                    tablero[encola[0].valor - 11] = "|"
                    return "Azul"
        elif(encola[0].valor < encola[1].valor
        and (encola[0].color == (255, 0, 0)
        and encola[1].color == (255, 0, 0))):
            if(encola[0].valor + 1 == encola[1].valor - 1):
                if(tablero[encola[0].valor + 1] != "-"):
                    self.conectar(pantalla, encola[0].x, encola[0].y,
                    encola[1].x, encola[1].y)
                    tablero[encola[0].valor + 1] = "-"
                    return "Azul"
            elif(encola[0].valor + 11 == encola[1].valor - 11):
                if(tablero[encola[0].valor + 11] != "|"):
                    self.conectar(pantalla, encola[0].x, encola[0].y,
                    encola[1].x, encola[1].y)
                    tablero[encola[0].valor + 11] = "|"
                    return "Azul"