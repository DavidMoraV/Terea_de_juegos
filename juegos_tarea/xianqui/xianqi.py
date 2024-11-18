from piezas.piezas import Pieza

class General(Pieza):
    def mover(self, nueva_coordenada):
        # El General solo puede moverse dentro del palacio
        posiciones_palacio = {
            'rojo': ['d1', 'e1', 'f1', 'd2', 'e2', 'f2', 'd3', 'e3', 'f3'],
            'negro': ['d8', 'e8', 'f8', 'd9', 'e9', 'f9', 'd10', 'e10', 'f10']
        }
        if nueva_coordenada in posiciones_palacio[self.color]:
            self.coordenada = nueva_coordenada
        else:
            raise ValueError("Movimiento inválido para el General")


class Consejero(Pieza):
    def mover(self, nueva_coordenada):
        # El Consejero solo puede moverse dentro del palacio
        posiciones_palacio = {
            'rojo': ['d1', 'e1', 'f1', 'd2', 'e2', 'f2', 'd3', 'e3', 'f3'],
            'negro': ['d8', 'e8', 'f8', 'd9', 'e9', 'f9', 'd10', 'e10', 'f10']
        }
        if nueva_coordenada in posiciones_palacio[self.color]:
            self.coordenada = nueva_coordenada
        else:
            raise ValueError("Movimiento inválido para el Consejero")

class Peon(Pieza):
    def mover(self, nueva_coordenada):
        # Lógica de movimiento del Peón
        fila, columna = int(self.coordenada[1:]), self.coordenada[0]
        nueva_fila, nueva_columna = int(nueva_coordenada[1:]), nueva_coordenada[0]

        if self.color == "rojo":
            if fila <= 5:  # Antes de cruzar el río
                if nueva_fila == fila + 1 and nueva_columna == columna:
                    self.coordenada = nueva_coordenada
                else:
                    raise ValueError("Movimiento inválido para el Peón")
            else:  # Después de cruzar el río
                if (nueva_fila == fila + 1 and nueva_columna == columna) or (nueva_fila == fila and abs(ord(nueva_columna) - ord(columna)) == 1):
                    self.coordenada = nueva_coordenada
                else:
                    raise ValueError("Movimiento inválido para el Peón")
        elif self.color == "negro":
            if fila >= 6:  # Antes de cruzar el río
                if nueva_fila == fila - 1 and nueva_columna == columna:
                    self.coordenada = nueva_coordenada
                else:
                    raise ValueError("Movimiento inválido para el Peón")
            else:  # Después de cruzar el río
                if (nueva_fila == fila - 1 and nueva_columna == columna) or (nueva_fila == fila and abs(ord(nueva_columna) - ord(columna)) == 1):
                    self.coordenada = nueva_coordenada
                else:
                    raise ValueError("Movimiento inválido para el Peón")