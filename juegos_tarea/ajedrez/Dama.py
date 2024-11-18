from piezas.piezas import Pieza
from piezas.Coordenada_Ajedrez import CoordenadaAjedrez

class Dama(Pieza):
    def __init__(self, color, coordenada):
        super().__init__(color, coordenada)

    # Método para comparar damas
    def __eq__(self, otro):
        if isinstance(otro, Dama):
            return self.color == otro.color and self.coordenada == otro.coordenada
        return False

    def __str__(self):
        return f"Dama {self.color} en {self.coordenada}"

    # Método para verificar si el movimiento es válido para una dama
    def mover(self, casilla_destino):
        """
        Verifica si la dama puede moverse a la casilla destino.
        Las reglas básicas del movimiento de la dama:
        - Puede moverse en cualquier dirección: horizontal, vertical o diagonal.
        - Puede avanzar cualquier número de casillas en esas direcciones.
        """
        columna_actual = self.coordenada.columna
        fila_actual = self.coordenada.fila

        columna_destino = casilla_destino.columna
        fila_destino = casilla_destino.fila

        # Cálculo de diferencias entre filas y columnas
        diferencia_filas = abs(fila_destino - fila_actual)
        diferencia_columnas = abs(ord(columna_destino) - ord(columna_actual))

        # Reglas de movimiento para la dama:
        # 1. Movimiento horizontal (misma fila, distinta columna)
        if fila_actual == fila_destino and columna_actual != columna_destino:
            self.set_coordenada(casilla_destino)
            return True

        # 2. Movimiento vertical (misma columna, distinta fila)
        elif columna_actual == columna_destino and fila_actual != fila_destino:
            self.set_coordenada(casilla_destino)
            return True

        # 3. Movimiento diagonal (diferencia de filas y columnas igual)
        elif diferencia_filas == diferencia_columnas:
            self.set_coordenada(casilla_destino)
            return True

        # Si no cumple con las reglas de movimiento, es un movimiento inválido
        return False
