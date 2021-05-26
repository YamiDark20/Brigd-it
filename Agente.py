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

    def mover(self, mov):
        if(mov[0] + 1 == mov[1] - 1):
            self.mundo[mov[0] + 1] = "-"
        elif(mov[0] + 11 == mov[1] - 11):
            self.mundo[mov[0] + 11] = "|"
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
                    if(self.mundo[mov - 1] == '-'):
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
                    if(self.mundo[mov - 1] == '-'):
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
                    if(self.mundo[mov - 1] == '-'):
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
                    if(self.mundo[x + 1] == '-'):
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

    def escogerMov(self):
        agente2 = Agente(self.color)
        agente2.mundo = copy.copy(self.mundo)
        agente2 = self.alfa_beta(agente2, self.color, {"Azul": "Rojo", "Rojo": "Azul"},
        maxProf=3)
        movVal = self.movValidos(self.color)
        verificar = True
        while(agente2.mejorEstado is not None):
            if(agente2.color == self.color):
                for elem in movVal:
                    if elem == agente2.mejorEstado:
                        verificar = False
                if(verificar is True):
                    pass
                elif(verificar is False):
                    self.mover(agente2.mejorEstado)
                    #print(agente2.valor)
                    return agente2.mejorEstado, agente2.valor
                    #break
            agente2 = agente2.siguienteEstado

    def alfa_beta(self, agente, jugador, oponente, maxProf=3):
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
                if(ganador[0] == "Azul"):
                    nextAgente.valor = ganador[1]
                    agente.valor = nextAgente.valor
                    agente.siguienteEstado = nextAgente
                    agente.mejorEstado = move
                    return agente
                else:
                    nextAgente.valor = ganador[1]
                nextAgente.alpha = alpha
                nextAgente.beta = beta

                self.alfa_beta(nextAgente, jugador, oponente, maxProf)

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