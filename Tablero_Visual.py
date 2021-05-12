import pygame
import sys
from pygame.locals import *
from Agente import *
import time

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


class Puntos(pygame.sprite.Sprite):

    def __init__(self, valor, x, y):
        super(Puntos, self).__init__()
        self.valor = valor
        self.presionada = False
        self.x = x
        self.y = y
        if(valor == 1 or valor == 3 or valor == 5 or valor == 7 or valor == 9
        or valor == 23 or valor == 25 or valor == 27 or valor == 29
        or valor == 31 or valor == 45 or valor == 47 or valor == 49
        or valor == 51 or valor == 53 or valor == 67 or valor == 69
        or valor == 71 or valor == 73 or valor == 75 or valor == 89
        or valor == 91 or valor == 93 or valor == 95 or valor == 97
        or valor == 111 or valor == 113 or valor == 115 or valor == 117
        or valor == 119):
            self.color = ROJO
        else:
            self.color = AZUL
        self.circulo = pygame.draw.circle(PANTALLA, self.color,
        (self.x, self.y), 15)

    def presionar(self):
        self.presionada = not self.presionada

    def pintarPunto(self):
        if(self.presionada is True):
            self.circulo = pygame.draw.circle(PANTALLA, NEGRO, (self.x, self.y),
            15)
        else:
            self.circulo = pygame.draw.circle(PANTALLA, self.color,
            (self.x, self.y), 15)

pygame.init()

PANTALLA = pygame.display.set_mode((700, 650))
pygame.display.set_caption('Bridg-it')
PANTALLA.fill(BLANCO)
#fondo = pygame.image.load('espacio.png').convert()

"""Puntos(0, 40, 20), Puntos(1, 100, 20), Puntos(2, 160, 20),
    Puntos(3, 220, 20), Puntos(4, 280, 20), Puntos(5, 340, 20),
    Puntos(6, 400, 20), Puntos(7, 460, 20), Puntos(8, 520, 20),
    Puntos(9, 580, 20), Puntos(10, 640, 20), """
puntos = [
    Puntos(1, 100, 20), Puntos(3, 220, 20), Puntos(5, 340, 20),
    Puntos(7, 460, 20), Puntos(9, 580, 20),

    Puntos(11, 40, 80), Puntos(13, 160, 80), Puntos(15, 280, 80),
    Puntos(17, 400, 80), Puntos(19, 520, 80), Puntos(21, 640, 80),

    Puntos(23, 100, 140), Puntos(25, 220, 140), Puntos(27, 340, 140),
    Puntos(29, 460, 140), Puntos(31, 580, 140),

    Puntos(33, 40, 200), Puntos(35, 160, 200), Puntos(37, 280, 200),
    Puntos(39, 400, 200), Puntos(41, 520, 200), Puntos(43, 640, 200),

    Puntos(45, 100, 260), Puntos(47, 220, 260), Puntos(49, 340, 260),
    Puntos(51, 460, 260), Puntos(53, 580, 260),

    Puntos(55, 40, 320), Puntos(57, 160, 320), Puntos(59, 280, 320),
    Puntos(61, 400, 320), Puntos(63, 520, 320), Puntos(65, 640, 320),

    Puntos(67, 100, 380), Puntos(69, 220, 380), Puntos(71, 340, 380),
    Puntos(73, 460, 380), Puntos(75, 580, 380),

    Puntos(77, 40, 440), Puntos(79, 160, 440), Puntos(81, 280, 440),
    Puntos(83, 400, 440), Puntos(85, 520, 440), Puntos(87, 640, 440),

    Puntos(89, 100, 500), Puntos(91, 220, 500), Puntos(93, 340, 500),
    Puntos(95, 460, 500), Puntos(97, 580, 500),

    Puntos(99, 40, 560), Puntos(101, 160, 560), Puntos(103, 280, 560),
    Puntos(105, 400, 560), Puntos(107, 520, 560), Puntos(109, 640, 560),

    Puntos(111, 100, 620), Puntos(113, 220, 620), Puntos(115, 340, 620),
    Puntos(117, 460, 620), Puntos(119, 580, 620)]

encola = []
turn = "Rojo"
a = Agente("Azul")
tablero = {
0: ' ', 1: '1', 2: ' ', 3: '1', 4: ' ', 5: '1', 6: ' ', 7: '1', 8: ' ', 9: '1', 10: ' ',
11: '2', 12: ' ', 13: '2', 14: ' ', 15: '2', 16: ' ', 17: '2', 18: ' ', 19: '2', 20: ' ', 21: '2',
22: ' ', 23: '1', 24: ' ', 25: '1', 26: ' ', 27: '1', 28: ' ', 29: '1', 30: ' ', 31: '1', 32: ' ',
33: '2', 34: ' ', 35: '2', 36: ' ', 37: '2', 38: ' ', 39: '2', 40: ' ', 41: '2', 42: ' ', 43: '2',
44: ' ', 45: '1', 46: ' ', 47: '1', 48: ' ', 49: '1', 50: ' ', 51: '1', 52: ' ', 53: '1', 54: ' ',
55: '2', 56: ' ', 57: '2', 58: ' ', 59: '2', 60: ' ', 61: '2', 62: ' ', 63: '2', 64: ' ', 65: '2',
66: ' ', 67: '1', 68: ' ', 69: '1', 70: ' ', 71: '1', 72: ' ', 73: '1', 74: ' ', 75: '1', 76: ' ',
77: '2', 78: ' ', 79: '2', 80: ' ', 81: '2', 82: ' ', 83: '2', 84: ' ', 85: '2', 86: ' ', 87: '2',
88: ' ', 89: '1', 90: ' ', 91: '1', 92: ' ', 93: '1', 94: ' ', 95: '1', 96: ' ', 97: '1', 98: ' ',
99: '2', 100: ' ', 101: '2', 102: ' ', 103: '2', 104: ' ', 105: '2', 106: ' ', 107: '2', 108: ' ', 109: '2',
110: ' ', 111: '1', 112: ' ', 113: '1', 114: ' ', 115: '1', 116: ' ', 117: '1', 118: ' ', 119: '1'}
a.mundo = tablero
p1 = None
p2 = None
while True:
    if turn == "Rojo":
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                for c in puntos:
                    if(mouse[0] > c.circulo.topleft[0] and
                    mouse[1] > c.circulo.topleft[1] and
                    mouse[0] < c.circulo.bottomright[0] and
                    mouse[1] < c.circulo.bottomright[1]):
                        c.presionar()
                        if(len(list(filter(lambda i:
                        i.valor == c.valor, encola))) <= 0):
                            encola.append(c)
                        else:
                            encola.remove(c)

        if(len(encola) == 2):
            if(encola[0].valor > encola[1].valor and (encola[0].color == ROJO
            and encola[1].color == ROJO)):
                if(encola[0].valor - 1 == encola[1].valor + 1):
                    if(tablero[encola[0].valor - 1] != "-"):
                        pygame.draw.line(PANTALLA, NEGRO, (encola[0].x, encola[0].y), (
                        encola[1].x, encola[1].y), 10)
                        tablero[encola[0].valor - 1] = "-"
                        turn = "Azul"
                elif(encola[0].valor - 11 == encola[1].valor + 11):
                    if(tablero[encola[0].valor - 11] != "|"):
                        pygame.draw.line(PANTALLA, NEGRO, (encola[0].x, encola[0].y), (
                        encola[1].x, encola[1].y), 10)
                        tablero[encola[0].valor - 11] = "|"
                        turn = "Azul"
            elif(encola[0].valor < encola[1].valor and (encola[0].color == ROJO
            and encola[1].color == ROJO)):
                if(encola[0].valor + 1 == encola[1].valor - 1):
                    if(tablero[encola[0].valor + 1] != "-"):
                        pygame.draw.line(PANTALLA, NEGRO, (encola[0].x, encola[0].y), (
                        encola[1].x, encola[1].y), 10)
                        tablero[encola[0].valor + 1] = "-"
                        turn = "Azul"
                elif(encola[0].valor + 11 == encola[1].valor - 11):
                    if(tablero[encola[0].valor + 11] != "|"):
                        pygame.draw.line(PANTALLA, NEGRO, (encola[0].x, encola[0].y), (
                        encola[1].x, encola[1].y), 10)
                        tablero[encola[0].valor + 11] = "|"
                        turn = "Azul"
            encola[0].presionar()
            encola[1].presionar()
            encola = []
        """v = eg.msgbox(msg='Caja de mensaje simple',
        title='Control: msgbox',
        ok_button='Continuar', image=None)
        """
    elif turn == "Azul":
        mov = escogerMov(a)
        p1 = None
        p2 = None
        for punt in puntos:
            if punt.valor == mov[0]:
                p1 = punt
            elif punt.valor == mov[1]:
                p2 = punt
        pygame.draw.line(PANTALLA, NEGRO, (p1.x, p1.y), (p2.x, p2.y), 10)
        pygame.display.flip()
        print(mov)
        turn = "Rojo"

    verificar = a.fin_del_juego()
    if verificar[0] is not None:

        time.sleep(2)
        if(verificar[0] == "Rojo"):
            fondo = pygame.image.load('ganador2.png').convert()
            PANTALLA.blit(fondo, (0, 0))
            pygame.display.flip()
        elif(verificar[0] == "Azul"):
            fondo = pygame.image.load('perdedor.png').convert()
            PANTALLA.blit(fondo, (0, 0))
            pygame.display.flip()
            #print(verificar[0])
        pygame.display.flip()
        time.sleep(7)
        pygame.quit()
        sys.exit()
    else:

        #PANTALLA.fill(BLANCO)
        for c in puntos:
            c.pintarPunto()

    ##Para actualizar la ventana
    pygame.display.flip()