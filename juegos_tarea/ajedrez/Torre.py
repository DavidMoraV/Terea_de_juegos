from piezas.piezas import Pieza
from piezas.Coordenada_Ajedrez import CoordenadaAjedrez

class Torre(Pieza):
    def __init__(self, color, coordenada):
        super().__init__(color, coordenada)

    # Método para comparar torres
    def __eq__(self, otro):
        if isinstance(otro, Torre):
            return self.color == otro.color and self.coordenada == otro.coordenada
        return False

    def __str__(self):
        return f"Torre {self.color} en {self.coordenada}"

    # Método para calcular si el movimiento es válido para una torre
    def mover(self, casilla_destino):
        """
        Verifica si la torre puede moverse a la casilla destino.
        Las reglas básicas del movimiento de la torre:
        - La torre se mueve en línea recta vertical u horizontal.
        """
        columna_actual = self.coordenada.columna
        fila_actual = self.coordenada.fila

        columna_destino = casilla_destino.columna
        fila_destino = casilla_destino.fila

        # Movimiento en línea recta: misma columna o misma fila
        if columna_actual == columna_destino or fila_actual == fila_destino:
            self.set_coordenada(casilla_destino)
            return True

        # Si no cumple con las reglas de movimiento, es un movimiento inválido
        return False
