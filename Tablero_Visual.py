import pygame
import sys
from pygame.locals import *
from Agente import *
from Puntos import *
from Jugador import *
import time


ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


class Tablero():

    def __init__(self):
        super(Tablero, self).__init__()
        pygame.init()
        self.pantalla = pygame.display.set_mode((700, 650))
        pygame.display.set_caption('Bridg-it')
        self.pantalla.fill(BLANCO)

        self.puntos = []
        self.iniciarlizarPuntos()
        #Puntos(1, 100, 20, self.pantalla), Puntos(3, 220, 20, self.pantalla),
        #Puntos(5, 340, 20, self.pantalla), Puntos(7, 460, 20, self.pantalla),
        #Puntos(9, 580, 20, self.pantalla),

        #Puntos(11, 40, 80, self.pantalla), Puntos(13, 160, 80, self.pantalla),
        #Puntos(15, 280, 80, self.pantalla),Puntos(17, 400, 80, self.pantalla),
        #Puntos(19, 520, 80, self.pantalla), Puntos(21, 640, 80, self.pantalla),

        #Puntos(23, 100, 140, self.pantalla),
        #Puntos(25, 220, 140, self.pantalla),
        #Puntos(27, 340, 140, self.pantalla),Puntos(29, 460, 140, self.pantalla),
        #Puntos(31, 580, 140, self.pantalla),

        #Puntos(33, 40, 200, self.pantalla), Puntos(35, 160, 200, self.pantalla),
        #Puntos(37, 280, 200, self.pantalla),Puntos(39, 400, 200, self.pantalla),
        #Puntos(41, 520, 200, self.pantalla),
        #Puntos(43, 640, 200, self.pantalla),

        #Puntos(45, 100, 260, self.pantalla),
        #Puntos(47, 220, 260, self.pantalla),
        #Puntos(49, 340, 260, self.pantalla),
        #Puntos(51, 460, 260, self.pantalla),
        #Puntos(53, 580, 260, self.pantalla),

        #Puntos(55, 40, 320, self.pantalla), Puntos(57, 160, 320, self.pantalla),
        #Puntos(59, 280, 320, self.pantalla),
        #Puntos(61, 400, 320, self.pantalla),
        #Puntos(63, 520, 320, self.pantalla),
        #Puntos(65, 640, 320, self.pantalla),

        #Puntos(67, 100, 380, self.pantalla),
        #Puntos(69, 220, 380, self.pantalla),
        #Puntos(71, 340, 380, self.pantalla),
        #Puntos(73, 460, 380, self.pantalla),
        #Puntos(75, 580, 380, self.pantalla),

        #Puntos(77, 40, 440, self.pantalla), Puntos(79, 160, 440, self.pantalla),
        #Puntos(81, 280, 440, self.pantalla),
        #Puntos(83, 400, 440, self.pantalla),
        #Puntos(85, 520, 440, self.pantalla),
        #Puntos(87, 640, 440, self.pantalla),

        #Puntos(89, 100, 500, self.pantalla),
        #Puntos(91, 220, 500, self.pantalla),
        #Puntos(93, 340, 500, self.pantalla),
        #Puntos(95, 460, 500, self.pantalla),
        #Puntos(97, 580, 500, self.pantalla),

        #Puntos(99, 40, 560, self.pantalla),
        #Puntos(101, 160, 560, self.pantalla),
        #Puntos(103, 280, 560, self.pantalla),
        #Puntos(105, 400, 560, self.pantalla),
        #Puntos(107, 520, 560, self.pantalla),
        #Puntos(109, 640, 560, self.pantalla),

        #Puntos(111, 100, 620, self.pantalla),
        #Puntos(113, 220, 620, self.pantalla),
        #Puntos(115, 340, 620, self.pantalla),
        #Puntos(117, 460, 620, self.pantalla),
        #Puntos(119, 580, 620, self.pantalla)]

        self.agente = Agente("Azul")
        self.turn = "Rojo"
        self.jugador = Jugador("Rojo")

    def iniciarlizarPuntos(self):
        valor = 1
        x = 100
        y = 20
        while valor <= 119:
            self.puntos.append(Puntos(valor, x, y, self.pantalla))
            valor += 2
            if x == 100 or x == 220 or x == 340 or x == 460:
                x += 120
            elif x == 580:
                x = 40
                y += 60
            elif x == 40 or x == 160 or x == 280 or x == 400 or x == 520:
                x += 120
            elif x == 640:
                x = 100
                y += 60

    def iniciarJuego(self):
        encola = []
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
        self.agente.mundo = tablero
        p1 = None
        p2 = None
        ganador = ""
        #fondo2 = pygame.image.load('perdedor.png').convert()
        while True:
            if self.turn == "Rojo":
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if(ganador == ""):
                            mouse = pygame.mouse.get_pos()
                            for c in self.puntos:
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
                        elif(ganador == "Rojo"):
                            fondo = pygame.image.load('ganador2.png').convert()
                            self.pantalla.blit(fondo, (0, 0))
                            pygame.display.flip()
                            time.sleep(5)
                            pygame.quit()
                            sys.exit()
                        elif(ganador == "Azul"):
                            fondo = pygame.image.load('perdedor.png').convert()
                            self.pantalla.blit(fondo, (0, 0))
                            pygame.display.flip()
                            time.sleep(5)
                            pygame.quit()
                            sys.exit()

                if(len(encola) == 2):
                    ##########
                    result = self.jugador.realizarMov(encola, tablero,
                    self.pantalla)
                    if(result is not None):
                        self.turn = "Azul"  # Si entra aqui significa que
                        #pudo realizar el movimiento
                    encola[0].presionar()
                    encola[1].presionar()
                    encola = []
            elif self.turn == "Azul":
                mov, result = self.agente.escogerMov()
                p1 = None
                p2 = None
                for punt in self.puntos:
                    if punt.valor == mov[0]:
                        p1 = punt
                    elif punt.valor == mov[1]:
                        p2 = punt
                #print(p1.x, p1.y, p2.x, p2.y)
                pygame.draw.line(self.pantalla, NEGRO, (p1.x, p1.y),
                (p2.x, p2.y), 10)
                pygame.display.flip()
                #if result == 100:
                    ##time.sleep(27)
                    ##fondo = pygame.image.load('perdedor.png').convert()
                    ##self.pantalla.blit(fondo, (0, 0))
                    ##pygame.display.flip()
                    ##time.sleep(17)
                    #pygame.quit()
                    #sys.exit()
                self.turn = "Rojo"

            if(ganador == ""):
                verificar = self.agente.fin_del_juego()
                if verificar[0] is not None:

                    #time.sleep(2)
                    #print(verificar[0])
                    if(verificar[0] == "Rojo"):
                        #fondo = pygame.image.load('ganador2.png').convert()
                        #self.pantalla.blit(fondo, (0, 0))
                        #pygame.display.flip()
                        ganador = "Rojo"
                        self.turn = "Rojo"
                    elif(verificar[0] == "Azul"):
                        ganador = "Azul"
                        #time.sleep(200)
                        #time.sleep(40)
                        #fondo = pygame.image.load('perdedor.png').convert()
                        #self.pantalla.blit(fondo, (0, 0))
                        #pygame.display.flip()
                        #time.sleep(32)
                    #pygame.display.flip()
                    #time.sleep(7)
                    #pygame.quit()
                    #sys.exit()
            #else:
            for c in self.puntos:
                c.pintarPunto()

            ##Para actualizar la ventana
            pygame.display.flip()


t = Tablero()
t.iniciarJuego()