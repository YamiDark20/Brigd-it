#import Tablero as mundo
#import time
import copy


class Agente():

    def __init__(self, color):
        super(Agente, self).__init__()
        self.color = color
        self.valor = 0
        self.profundidad = 0
        self.siguienteEstado = None
        self.mejorEstado = None
        self.alpha = -9999
        self.beta = 9999
        self.mundo = None

    def dibujarTablero(self):
        acumulador = ""
        i = 0
        for key in self.mundo.keys():
            if(i < 11):
                acumulador += self.mundo[key]
                i += 1
            else:
                acumulador += "\n"
                i = 1
                acumulador += self.mundo[key]
        print(acumulador)

    def mover(self, mov):
        if(mov[0] + 1 == mov[1] - 1):
            self.mundo[mov[0] + 1] = "-"
        elif(mov[0] + 11 == mov[1] - 11):
            self.mundo[mov[0] + 11] = "|"
        else:
            return "Error"

    def deshacerMov(self, mov):
        if(mov[0] + 1 == mov[1] - 1):
            self.mundo[mov[0] + 1] = " "
        elif(mov[0] + 11 == mov[1] - 11):
            self.mundo[mov[0] + 11] = " "
        else:
            return "Error"

    def busqueda(self, mov, conexiones, jugador):
        if(jugador == "Rojo"):
            if(mov == 1):
                if(len(list(filter(lambda i: i == [mov, mov + 22]
                or i == [mov + 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 11] == '|'):
                        if(mov + 22 == 111 or mov + 22 == 113
                        or mov + 22 == 115 or mov + 22 == 117
                        or mov + 22 == 119):
                            return "Rojo"
                        conexiones.append([mov, mov + 22])
                        result = self.busqueda(mov + 22, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov + 2]
                or i == [mov + 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 1] == '-'):
                        conexiones.append([mov, mov + 2])
                        result = self.busqueda(mov + 2, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
            elif(mov == 9):
                if(len(list(filter(lambda i: i == [mov, mov + 22]
                or i == [mov + 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 11] == '|'):
                        if(mov + 22 == 111 or mov + 22 == 113
                        or mov + 22 == 115 or mov + 22 == 117
                        or mov + 22 == 119):
                            return "Rojo"
                        conexiones.append([mov, mov + 22])
                        result = self.busqueda(mov + 22, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 2]
                or i == [mov - 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 1] == '-'):
                        conexiones.append([mov, mov - 2])
                        result = self.busqueda(mov - 2, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
            elif(mov == 23 or mov == 45 or mov == 67 or mov == 89):
                if(len(list(filter(lambda i: i == [mov, mov + 22]
                or i == [mov + 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 11] == '|'):
                        if(mov + 22 == 111 or mov + 22 == 113
                        or mov + 22 == 115 or mov + 22 == 117
                        or mov + 22 == 119):
                            return "Rojo"
                        conexiones.append([mov, mov + 22])
                        result = self.busqueda(mov + 22, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov + 2]
                or i == [mov + 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 1] == '-'):
                        conexiones.append([mov, mov + 2])
                        result = self.busqueda(mov + 2, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 22]
                or i == [mov - 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 11] == '|'):
                        conexiones.append([mov, mov - 22])
                        result = self.busqueda(mov - 22, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
            elif(mov == 31 or mov == 53 or mov == 75 or mov == 97):
                if(len(list(filter(lambda i: i == [mov, mov + 22]
                or i == [mov + 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 11] == '|'):
                        if(mov + 22 == 111 or mov + 22 == 113
                        or mov + 22 == 115 or mov + 22 == 117
                        or mov + 22 == 119):
                            return "Rojo"
                        conexiones.append([mov, mov + 22])
                        result = self.busqueda(mov + 22, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 2]
                or i == [mov - 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 1] == '-'):
                        conexiones.append([mov, mov - 2])
                        result = self.busqueda(mov - 2, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 22]
                or i == [mov - 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 11] == '|'):
                        conexiones.append([mov, mov - 22])
                        result = self.busqueda(mov - 22, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
            elif(mov == 3 or mov == 5 or mov == 7):
                if(len(list(filter(lambda i: i == [mov, mov + 22]
                or i == [mov + 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 11] == '|'):
                        if(mov + 22 == 111 or mov + 22 == 113
                        or mov + 22 == 115 or mov + 22 == 117
                        or mov + 22 == 119):
                            return "Rojo"
                        conexiones.append([mov, mov + 22])
                        result = self.busqueda(mov + 22, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov + 2]
                or i == [mov + 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 1] == '-'):
                        conexiones.append([mov, mov + 2])
                        result = self.busqueda(mov + 2, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 2]
                or i == [mov - 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 1] == '-'):
                        conexiones.append([mov, mov - 2])
                        result = self.busqueda(mov - 2, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
            ##################################################
            else:
                if(len(list(filter(lambda i: i == [mov, mov + 22]
                or i == [mov + 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 11] == '|'):
                        if(mov + 22 == 111 or mov + 22 == 113
                        or mov + 22 == 115 or mov + 22 == 117
                        or mov + 22 == 119):
                            return "Rojo"
                        conexiones.append([mov, mov + 22])
                        result = self.busqueda(mov + 22, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov + 2]
                or i == [mov + 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 1] == '-'):
                        conexiones.append([mov, mov + 2])
                        result = self.busqueda(mov + 2, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 2]
                or i == [mov - 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 1] == '-'):
                        conexiones.append([mov, mov - 2])
                        result = self.busqueda(mov - 2, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 22]
                or i == [mov - 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 11] == '|'):
                        conexiones.append([mov, mov - 22])
                        result = self.busqueda(mov - 22, conexiones, "Rojo")
                        if(result == "Rojo"):
                            return result

        #############################################################
        ############################################################
        elif(jugador == "Azul"):
            if(mov == 11):
                if(len(list(filter(lambda i: i == [mov, mov + 2]
                or i == [mov + 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 1] == '-'):
                        if(mov + 2 == 21 or mov + 2 == 43
                        or mov + 2 == 65 or mov + 2 == 87
                        or mov + 2 == 109):
                            return "Azul"
                        conexiones.append([mov, mov + 2])
                        result = self.busqueda(mov + 2, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov + 22]
                or i == [mov + 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 11] == '|'):
                        conexiones.append([mov, mov + 22])
                        result = self.busqueda(mov + 22, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
            elif(mov == 99):
                if(len(list(filter(lambda i: i == [mov, mov + 2]
                or i == [mov + 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 1] == '-'):
                        if(mov + 2 == 21 or mov + 2 == 43
                        or mov + 2 == 65 or mov + 2 == 87
                        or mov + 2 == 109):
                            return "Azul"
                        conexiones.append([mov, mov + 2])
                        result = self.busqueda(mov + 2, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 22]
                or i == [mov - 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 11] == '|'):
                        conexiones.append([mov, mov - 22])
                        result = self.busqueda(mov - 22, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
            elif(mov == 13 or mov == 15 or mov == 17 or mov == 19):
                if(len(list(filter(lambda i: i == [mov, mov + 2]
                or i == [mov + 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 1] == '-'):
                        if(mov + 2 == 21 or mov + 2 == 43
                        or mov + 2 == 65 or mov + 2 == 87
                        or mov + 2 == 109):
                            return "Azul"
                        conexiones.append([mov, mov + 2])
                        result = self.busqueda(mov + 2, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov + 22]
                or i == [mov + 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 11] == '|'):
                        conexiones.append([mov, mov + 22])
                        result = self.busqueda(mov + 22, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 2]
                or i == [mov - 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 1] == '|'):
                        conexiones.append([mov, mov - 2])
                        result = self.busqueda(mov - 2, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
            elif(mov == 101 or mov == 103 or mov == 105 or mov == 107):
                if(len(list(filter(lambda i: i == [mov, mov + 2]
                or i == [mov + 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 1] == '-'):
                        if(mov + 2 == 21 or mov + 2 == 43
                        or mov + 2 == 65 or mov + 2 == 87
                        or mov + 2 == 109):
                            return "Azul"
                        conexiones.append([mov, mov + 2])
                        result = self.busqueda(mov + 2, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 22]
                or i == [mov - 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 11] == '|'):
                        conexiones.append([mov, mov - 22])
                        result = self.busqueda(mov - 22, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 2]
                or i == [mov - 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 1] == '|'):
                        conexiones.append([mov, mov - 2])
                        result = self.busqueda(mov - 2, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
            elif(mov == 33 or mov == 55 or mov == 77):
                if(len(list(filter(lambda i: i == [mov, mov + 2]
                or i == [mov + 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 1] == '-'):
                        if(mov + 2 == 21 or mov + 2 == 43
                        or mov + 2 == 65 or mov + 2 == 87
                        or mov + 2 == 109):
                            return "Azul"
                        conexiones.append([mov, mov + 2])
                        result = self.busqueda(mov + 2, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov + 22]
                or i == [mov + 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 11] == '|'):
                        conexiones.append([mov, mov + 22])
                        result = self.busqueda(mov + 22, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 22]
                or i == [mov - 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 11] == '|'):
                        conexiones.append([mov, mov - 22])
                        result = self.busqueda(mov - 22, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
            else:
                if(len(list(filter(lambda i: i == [mov, mov + 2]
                or i == [mov + 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 1] == '-'):
                        if(mov + 2 == 21 or mov + 2 == 43
                        or mov + 2 == 65 or mov + 2 == 87
                        or mov + 2 == 109):
                            return "Azul"
                        conexiones.append([mov, mov + 2])
                        result = self.busqueda(mov + 2, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov + 22]
                or i == [mov + 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov + 11] == '|'):
                        conexiones.append([mov, mov + 22])
                        result = self.busqueda(mov + 22, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 22]
                or i == [mov - 22, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 11] == '|'):
                        conexiones.append([mov, mov - 22])
                        result = self.busqueda(mov - 22, conexiones, "Azul")
                        if(result == "Azul"):
                            return result
                if(len(list(filter(lambda i: i == [mov, mov - 2]
                or i == [mov - 2, mov], conexiones))) <= 0):
                    if(self.mundo[mov - 1] == '|'):
                        conexiones.append([mov, mov - 2])
                        result = self.busqueda(mov - 2, conexiones, "Azul")
                        if(result == "Azul"):
                            return result

    def fin_del_juego(self):
        #Verificacion si gano el Rojo
        conexiones = []
        result = ""
        for x in [1, 3, 5, 7, 9]:
            if(x == 1):
                if(len(list(filter(lambda i: i == [x, x + 22]
                or i == [x + 22, x], conexiones))) <= 0):
                    if(self.mundo[x + 11] == '|'):
                        conexiones.append([x, x + 22])
                        result = self.busqueda(x + 22, conexiones, "Rojo")
                        if(result != "" and result is not None):
                            if(result == "Azul"):
                                return [result, 100]
                            else:
                                return [result, - 100]
                if(len(list(filter(lambda i: i == [x, x + 2]
                or i == [x + 2, x], conexiones))) <= 0):
                    if(self.mundo[x + 1] == '-'):
                        conexiones.append([x, x + 2])
                        result = self.busqueda(x + 2, conexiones, "Rojo")
                        if(result != "" and result is not None):
                            if(result == "Azul"):
                                return [result, 100]
                            else:
                                return [result, - 100]
            elif(x > 1 and x < 9):
                if(len(list(filter(lambda i: i == [x, x + 22]
                or i == [x + 22, x], conexiones))) <= 0):
                    if(self.mundo[x + 11] == '|'):
                        conexiones.append([x, x + 22])
                        result = self.busqueda(x + 22, conexiones, "Rojo")
                        if(result != "" and result is not None):
                            if(result == "Azul"):
                                return [result, 100]
                            else:
                                return [result, - 100]
                if(len(list(filter(lambda i: i == [x, x + 2]
                or i == [x + 2, x], conexiones))) <= 0):
                    if(self.mundo[x + 1] == '-'):
                        conexiones.append([x, x + 2])
                        result = self.busqueda(x + 2, conexiones, "Rojo")
                        if(result != "" and result is not None):
                            if(result == "Azul"):
                                return [result, 100]
                            else:
                                return [result, - 100]
            elif(x == 9):
                if(len(list(filter(lambda i: i == [x, x + 22]
                or i == [x + 22, x], conexiones))) <= 0):
                    if(self.mundo[x + 11] == '|'):
                        conexiones.append([x, x + 22])
                        result = self.busqueda(x + 22, conexiones, "Rojo")
                        if(result != "" and result is not None):
                            if(result == "Azul"):
                                return [result, 100]
                            else:
                                return [result, - 100]

        #Verificacion si gano el Azul
        conexiones = []
        for x in [11, 33, 55, 77, 99]:
            if(x == 11):
                if(len(list(filter(lambda i: i == [x, x + 2]
                or i == [x + 2, x], conexiones))) <= 0):
                    if(self.mundo[x + 1] == '-'):
                        conexiones.append([x, x + 2])
                        result = self.busqueda(x + 2, conexiones, "Azul")
                        if(result != "" and result is not None):
                            if(result == "Azul"):
                                return [result, 100]
                            else:
                                return [result, - 100]
                if(len(list(filter(lambda i: i == [x, x + 22]
                or i == [x + 22, x], conexiones))) <= 0):
                    if(self.mundo[x + 11] == '|'):
                        conexiones.append([x, x + 22])
                        result = self.busqueda(x + 22, conexiones, "Azul")
                        if(result != "" and result is not None):
                            if(result == "Azul"):
                                return [result, 100]
                            else:
                                return [result, - 100]
            elif(x > 11 and x < 99):
                if(len(list(filter(lambda i: i == [x, x + 2]
                or i == [x + 2, x], conexiones))) <= 0):
                    if(self.mundo[x + 1] == '-'):
                        conexiones.append([x, x + 2])
                        result = self.busqueda(x + 2, conexiones, "Azul")
                        if(result != "" and result is not None):
                            if(result == "Azul"):
                                return [result, 100]
                            else:
                                return [result, - 100]
                if(len(list(filter(lambda i: i == [x, x + 22]
                or i == [x + 22, x], conexiones))) <= 0):
                    if(self.mundo[x + 11] == '|'):
                        conexiones.append([x, x + 22])
                        result = self.busqueda(x + 22, conexiones, "Azul")
                        if(result != "" and result is not None):
                            if(result == "Azul"):
                                return [result, 100]
                            else:
                                return [result, - 100]
            elif(x == 99):
                if(len(list(filter(lambda i: i == [x, x + 2]
                or i == [x + 2, x], conexiones))) <= 0):
                    if(self.mundo[x + 1] == '|'):
                        conexiones.append([x, x + 2])
                        result = self.busqueda(x + 2, conexiones, "Azul")
                        if(result != "" and result is not None):
                            if(result == "Azul"):
                                return [result, 100]
                            else:
                                return [result, - 100]
        return [None, 0]

    def movValidos(self, jugador):
        mov = []
        if(jugador == "Azul"):
            i = 12
            while(i <= 108):
                if((self.mundo[i] != "-") and (self.mundo[i] != "|")):
                    if(i != 22 and i != 24 and i != 26 and i != 28 and i != 30
                    and i != 44 and i != 46 and i != 48 and i != 50 and i != 52
                    and i != 32 and i != 54 and i != 66 and i != 68 and i != 70
                    and i != 72 and i != 74 and i != 76 and i != 88 and i != 90
                    and i != 92 and i != 94 and i != 96 and i != 98):
                        mov.append([i - 1, i + 1])
                    if(i != 12 and i != 14 and i != 16 and i != 18 and i != 20
                    and i != 34 and i != 36 and i != 38 and i != 40 and i != 42
                    and i != 56 and i != 58 and i != 60 and i != 62 and i != 64
                    and i != 78 and i != 80 and i != 82 and i != 84 and i != 86
                    and i != 100 and i != 102 and i != 104 and i != 106
                    and i != 108):
                        mov.append([i - 11, i + 11])
                if(i + 2 == 10):
                    i += 4
                else:
                    i += 2
        else:
            i = 2
            while(i <= 118):
                if((self.mundo[i] != "-") and (self.mundo[i] != "|")):
                    if(i != 12 and i != 14 and i != 16 and i != 18 and i != 20
                    and i != 22 and i != 34 and i != 36 and i != 38 and i != 40
                    and i != 42 and i != 44 and i != 56 and i != 58 and i != 60
                    and i != 62 and i != 64 and i != 66 and i != 78 and i != 80
                    and i != 82 and i != 84 and i != 86 and i != 88 and i != 100
                    and i != 102 and i != 104 and i != 106 and i != 108
                    and i != 110):
                        mov.append([i - 1, i + 1])
                    if(i != 2 and i != 4 and i != 6 and i != 8 and i != 22
                    and i != 24 and i != 26 and i != 28 and i != 30 and i != 32
                    and i != 44 and i != 46 and i != 48 and i != 50 and i != 52
                    and i != 54 and i != 66 and i != 68 and i != 70 and i != 72
                    and i != 74 and i != 76 and i != 88 and i != 90 and i != 92
                    and i != 94 and i != 96 and i != 98 and i != 110
                    and i != 112 and i != 114 and i != 116 and i != 118):
                        mov.append([i - 11, i + 11])
                if(i + 2 == 10 or i + 2 == 22 or i + 2 == 44 or i + 2 == 66
                or i + 2 == 88 or i + 2 == 110 or i + 2 == 32 or i + 2 == 54
                or i + 2 == 76 or i + 2 == 98):
                    i += 4
                else:
                    i += 2
        return mov

def escogerMov(agente):
    agente2 = Agente(agente.color)
    agente2.mundo = copy.copy(agente.mundo)
    agente2 = alfa_beta(agente2, agente.color, {"Azul": "Rojo", "Rojo": "Azul"},
    maxProf=3)
    movVal = agente.movValidos(agente.color)
    verificar = True
    while(agente2.mejorEstado is not None):
        if(agente2.color == agente.color):
            for elem in movVal:
                if elem == agente2.mejorEstado:
                    verificar = False
            if(verificar is True):
                pass
            elif(verificar is False):
                agente.mover(agente2.mejorEstado)
                return agente2.mejorEstado
                #break
        agente2 = agente2.siguienteEstado

def alfa_beta(agente, jugador, oponente, maxProf=3):
    alpha, beta = (agente.alpha, agente.beta)
    ganador = agente.fin_del_juego()
    movVal = agente.movValidos(agente.color)

    if(agente.profundidad < maxProf and (ganador[0] is None or movVal != [])):
        for move in movVal:
            nextAgente = Agente(agente.color)
            nextAgente.profundidad = agente.profundidad + 1
            nextAgente.mundo = copy.copy(agente.mundo)
            nextAgente.mover(move)
            nextAgente.color = oponente[agente.color]
            ganador = nextAgente.fin_del_juego()
            if(ganador == jugador):
                nextAgente.valor = ganador[1]
            else:
                nextAgente.valor = ganador[1]
            nextAgente.alpha = alpha
            nextAgente.beta = beta

            alfa_beta(nextAgente, jugador, oponente, maxProf)

            if(agente.color == "Azul"):
                if((agente.siguienteEstado is None) or nextAgente.valor > agente.valor):
                    agente.valor = nextAgente.valor
                    agente.siguienteEstado = nextAgente
                    agente.mejorEstado = move

                    alpha = max(alpha, agente.valor)
                    if(agente.valor >= beta):
                        return agente
            else:
                if((agente.siguienteEstado is None) or nextAgente.valor < agente.valor):
                    agente.valor = nextAgente.valor
                    agente.siguienteEstado = nextAgente
                    agente.mejorEstado = move

                    beta = min(beta, agente.valor)
                    if(agente.valor <= alpha):
                        return agente
    return agente


"""a = Agente("Azul")

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
#print(a.fin_del_juego())
while(True):
    a.dibujarTablero()
    mov1 = int(input("Movimiento de usuario del primer elemento: "))
    mov2 = int(input("Movimiento de usuario del segundo elemento: "))
    a.mover(list(sorted([mov1, mov2])))
    escogerMov(a)"""