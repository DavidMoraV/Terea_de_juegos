from piezas.piezas import Pieza
from piezas.Coordenada_Ajedrez import CoordenadaAjedrez

class Rey(Pieza):
    def __init__(self, color, coordenada):
        super().__init__(color, coordenada)

    # Método __eq__ para comparar reyes
    def __eq__(self, otro):
        if isinstance(otro, Rey):
            return self.color == otro.color and self.coordenada == otro.coordenada
        return False

    def __str__(self):
        return f"Rey {self.color} en {self.coordenada}"

    # Método para calcular si el movimiento es válido para un rey
    def mover(self, casilla_destino):
        """
        Verifica si el rey puede moverse a la casilla destino.
        Las reglas básicas del movimiento del rey:
        - El rey se mueve solo una casilla en cualquier dirección (horizontal, vertical o diagonal).
        """
        columna_actual = self.coordenada.columna
        fila_actual = self.coordenada.fila

        columna_destino = casilla_destino.columna
        fila_destino = casilla_destino.fila

        # Calcula la diferencia entre la posición actual y la posición de destino
        diferencia_filas = abs(fila_destino - fila_actual)
        diferencia_columnas = abs(ord(columna_destino) - ord(columna_actual))

        # El rey puede moverse una casilla en cualquier dirección
        if diferencia_filas <= 1 and diferencia_columnas <= 1:
            self.set_coordenada(casilla_destino)
            return True

        # Si no cumple con las reglas de movimiento, es un movimiento inválido
        return False
